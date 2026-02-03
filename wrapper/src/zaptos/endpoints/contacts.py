import click
from ..cli import echo_output

@click.group()
def contacts():
    """Manage contacts and GHL sync"""
    pass

@contacts.command('list')
@click.option('--limit', default=20, help='Limit results')
@click.option('--query', help='Search query')
@click.pass_context
def list_contacts(ctx, limit, query):
    """List contacts"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming Zaptos API endpoint for listing contacts
        params = {"limit": limit}
        if query:
            params["query"] = query
        result = client._get("/contacts", params=params)
        echo_output(result)
    except Exception as e:
        click.echo(f"Error listing contacts: {str(e)}", err=True)

@contacts.command('get')
@click.argument('number')
@click.pass_context
def get_contact(ctx, number):
    """Get contact details"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming Zaptos API endpoint for getting contact
        # NOTE: API Spec in AGENTS.md only lists POST /contacts and GET /contacts
        # But logically there should be a way to get a specific one, or filter by number in list.
        # I'll try getting by number as a path param if supported or query param.
        # For now I'll assume GET /contacts/<number> is valid or I filter the list.
        # Let's try to fetch it specifically or filter.
        # API spec says: GET /contacts # List contacts
        # I'll use a filter on the list endpoint if no specific endpoint exists.

        # Checking AGENTS.md again:
        # GET  /contacts            # List contacts
        # POST /contacts            # Create/update contact

        # CLI design section says: zaptos contacts get <number>

        # I will attempt GET /contacts?number=<number> or similar.
        result = client._get(f"/contacts", params={"number": number})
        # If result is a list, take the first one?
        if isinstance(result, list) and len(result) > 0:
             echo_output(result[0])
        else:
             echo_output(result)

    except Exception as e:
        click.echo(f"Error getting contact: {str(e)}", err=True)

@contacts.command('create')
@click.option('--number', required=True, help='Phone number')
@click.option('--name', required=True, help='Contact name')
@click.pass_context
def create_contact(ctx, number, name):
    """Create or update contact"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._post("/contacts", json={
            "number": number,
            "name": name
        })
        echo_output(result)
    except Exception as e:
        click.echo(f"Error creating contact: {str(e)}", err=True)

@contacts.command('sync-ghl')
@click.option('--tag', help='Filter GHL contacts by tag')
@click.option('--since', help='Filter by date')
@click.pass_context
def sync_ghl(ctx, tag, since):
    """Sync contacts from GoHighLevel"""
    client = ctx.obj.client
    ghl_client = ctx.obj.ghl_client

    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return
    if not ghl_client:
        click.echo("Error: GHL client not initialized. Check GHL_API_KEY.", err=True)
        return

    try:
        click.echo("Fetching contacts from GHL...", err=True)
        if tag:
            ghl_contacts = ghl_client.get_contacts_by_tag(tag)
        else:
            ghl_contacts = ghl_client.get_contacts()

        synced_count = 0
        for contact in ghl_contacts:
            # Normalize phone
            phone = contact.get('phone')
            name = contact.get('name') or f"{contact.get('firstName', '')} {contact.get('lastName', '')}".strip()

            if phone and name:
                 # Create in Zaptos
                 # We can store GHL ID in metadata if Zaptos supports it, or just sync basic info
                 try:
                     client._post("/contacts", json={
                         "number": phone,
                         "name": name,
                         # "metadata": {"ghl_id": contact.get('id')} # If supported
                     })
                     synced_count += 1
                 except Exception as e:
                     click.echo(f"Failed to sync contact {name} ({phone}): {e}", err=True)

        click.echo(f"Synced {synced_count} contacts from GHL.", err=True)
        echo_output({"synced": synced_count, "total_ghl": len(ghl_contacts)})

    except Exception as e:
        click.echo(f"Error syncing contacts: {str(e)}", err=True)

@contacts.command('push-ghl')
@click.argument('number')
@click.pass_context
def push_ghl(ctx, number):
    """Push a contact to GoHighLevel"""
    client = ctx.obj.client
    ghl_client = ctx.obj.ghl_client

    if not client or not ghl_client:
        click.echo("Error: Clients not initialized.", err=True)
        return

    try:
        # Get contact from Zaptos
        # Assuming we can fetch by number as per 'get' command logic
        zaptos_contact = client._get(f"/contacts", params={"number": number})
        # Handle list vs dict response
        if isinstance(zaptos_contact, list):
            if not zaptos_contact:
                click.echo("Contact not found in Zaptos", err=True)
                return
            zaptos_contact = zaptos_contact[0]

        name = zaptos_contact.get('name', 'Unknown')
        phone = zaptos_contact.get('number', number)

        # Create in GHL
        ghl_data = {
            "name": name,
            "phone": phone
        }

        result = ghl_client.create_contact(ghl_data)
        echo_output(result)

    except Exception as e:
        click.echo(f"Error pushing contact: {str(e)}", err=True)
