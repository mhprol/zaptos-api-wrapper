import click
import json
import csv
import time
import uuid
import os
from datetime import datetime
from ..cli import echo_output
from ..config import config

def get_campaigns_file():
    app_dir = click.get_app_dir('zaptos')
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
    return os.path.join(app_dir, 'campaigns.json')

def load_campaigns():
    filepath = get_campaigns_file()
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}

def save_campaigns(data):
    filepath = get_campaigns_file()
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

@click.group()
def campaigns():
    """Manage bulk messaging campaigns"""
    pass

@campaigns.command('create')
@click.option('--name', required=True, help='Campaign name')
@click.option('--contacts', help='CSV file with contacts (header: number,name,...)')
@click.option('--ghl-tag', help='GHL Tag to fetch contacts from')
@click.option('--template', required=True, help='Template name or message content')
@click.pass_context
def create(ctx, name, contacts, ghl_tag, template):
    """Create a new campaign"""
    # Verify inputs
    if not contacts and not ghl_tag:
        click.echo("Error: Must provide --contacts or --ghl-tag", err=True)
        return

    campaign_id = str(uuid.uuid4())[:8]
    campaign = {
        "id": campaign_id,
        "name": name,
        "created_at": datetime.now().isoformat(),
        "status": "created",
        "template": template,
        "source": "csv" if contacts else "ghl",
        "source_config": contacts if contacts else ghl_tag,
        "stats": {"total": 0, "sent": 0, "failed": 0}
    }

    data = load_campaigns()
    data[campaign_id] = campaign
    save_campaigns(data)

    echo_output({"id": campaign_id, "status": "created", "message": f"Campaign '{name}' created."})

@campaigns.command('list')
@click.option('--status', help='Filter by status')
def list_campaigns(status):
    """List all campaigns"""
    data = load_campaigns()
    result = []
    for cid, camp in data.items():
        if status and camp.get('status') != status:
            continue
        result.append(camp)
    echo_output(result)

@campaigns.command('start')
@click.argument('id')
@click.pass_context
def start(ctx, id):
    """Start a campaign"""
    data = load_campaigns()
    if id not in data:
        click.echo(f"Error: Campaign {id} not found", err=True)
        return

    campaign = data[id]
    if campaign['status'] == 'completed':
        click.echo("Campaign already completed", err=True)
        return

    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized", err=True)
        return

    click.echo(f"Starting campaign {campaign['name']}...", err=True)
    campaign['status'] = 'running'
    save_campaigns(data)

    # Fetch contacts
    target_contacts = []
    if campaign['source'] == 'csv':
        try:
            with open(campaign['source_config'], 'r') as f:
                reader = csv.DictReader(f)
                target_contacts = list(reader)
        except Exception as e:
            click.echo(f"Error reading CSV: {e}", err=True)
            campaign['status'] = 'failed'
            save_campaigns(data)
            return

    elif campaign['source'] == 'ghl':
        ghl_client = ctx.obj.ghl_client
        if not ghl_client:
            click.echo("Error: GHL client not initialized", err=True)
            return
        target_contacts = ghl_client.get_contacts_by_tag(campaign['source_config'])

    # Send messages
    total = len(target_contacts)
    campaign['stats']['total'] = total
    sent = campaign['stats'].get('sent', 0)
    failed = campaign['stats'].get('failed', 0)

    # Simple loop (blocking)
    # In a real app this might be backgrounded or resumed
    for contact in target_contacts:
        # Check if already processed (naive check, assumes generic run)
        # For robustness we'd need a per-contact status in DB

        number = contact.get('number') or contact.get('phone')
        if not number:
            continue

        # Basic template rendering
        msg_text = campaign['template']
        # Replace placeholders like {{name}}
        name = contact.get('name') or contact.get('firstName', '')
        msg_text = msg_text.replace("{{name}}", name)

        try:
            client.send_text(number, msg_text)
            sent += 1
            click.echo(f"Sent to {number}", err=True)
        except Exception as e:
            failed += 1
            click.echo(f"Failed to send to {number}: {e}", err=True)

        campaign['stats']['sent'] = sent
        campaign['stats']['failed'] = failed
        save_campaigns(data) # Save progress

        time.sleep(2) # Rate limiting

    campaign['status'] = 'completed'
    save_campaigns(data)
    echo_output(campaign)

@campaigns.command('pause')
@click.argument('id')
def pause(id):
    """Pause a campaign (Not fully implemented in blocking CLI)"""
    # Since 'start' blocks, pause from another terminal would require updating the file
    # and 'start' loop checking it.
    data = load_campaigns()
    if id in data:
        data[id]['status'] = 'paused'
        save_campaigns(data)
        echo_output({"status": "paused"})
    else:
         click.echo("Campaign not found", err=True)

@campaigns.command('status')
@click.argument('id')
def status(id):
    """Get campaign status"""
    data = load_campaigns()
    if id in data:
        echo_output(data[id])
    else:
        click.echo("Campaign not found", err=True)

@campaigns.command('delete')
@click.argument('id')
def delete(id):
    """Delete a campaign"""
    data = load_campaigns()
    if id in data:
        del data[id]
        save_campaigns(data)
        echo_output({"status": "deleted"})
    else:
        click.echo("Campaign not found", err=True)
