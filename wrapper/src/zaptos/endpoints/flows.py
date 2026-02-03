import click
import yaml
import json
import os
from ..cli import echo_output

@click.group()
def flows():
    """Manage chatbot flows"""
    pass

@flows.command('list')
@click.pass_context
def list_flows(ctx):
    """List flows"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._get("/flows")
        echo_output(result)
    except Exception as e:
        click.echo(f"Error listing flows: {str(e)}", err=True)

@flows.command('get')
@click.argument('name')
@click.pass_context
def get_flow(ctx, name):
    """Get flow details"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._get(f"/flows/{name}")
        echo_output(result)
    except Exception as e:
        click.echo(f"Error getting flow: {str(e)}", err=True)

@flows.command('create')
@click.option('--name', required=True, help='Flow name')
@click.option('--file', required=True, help='Flow YAML file')
@click.pass_context
def create_flow(ctx, name, file):
    """Create a flow"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    if not os.path.exists(file):
        click.echo(f"Error: File {file} not found", err=True)
        return

    try:
        with open(file, 'r') as f:
            # Validate YAML
            data = yaml.safe_load(f)

        # Ensure name match
        if 'name' not in data:
            data['name'] = name

        result = client._post("/flows", json=data)
        echo_output(result)
    except yaml.YAMLError as e:
        click.echo(f"Error parsing YAML: {e}", err=True)
    except Exception as e:
        click.echo(f"Error creating flow: {str(e)}", err=True)

@flows.command('update')
@click.argument('name')
@click.option('--file', required=True, help='Flow YAML file')
@click.pass_context
def update_flow(ctx, name, file):
    """Update a flow"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    if not os.path.exists(file):
        click.echo(f"Error: File {file} not found", err=True)
        return

    try:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)

        result = client._put(f"/flows/{name}", json=data)
        echo_output(result)
    except yaml.YAMLError as e:
        click.echo(f"Error parsing YAML: {e}", err=True)
    except Exception as e:
        click.echo(f"Error updating flow: {str(e)}", err=True)

@flows.command('enable')
@click.argument('name')
@click.pass_context
def enable_flow(ctx, name):
    """Enable a flow"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._post(f"/flows/{name}/enable", json={})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error enabling flow: {str(e)}", err=True)

@flows.command('disable')
@click.argument('name')
@click.pass_context
def disable_flow(ctx, name):
    """Disable a flow"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._post(f"/flows/{name}/disable", json={})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error disabling flow: {str(e)}", err=True)

@flows.command('test')
@click.argument('name')
@click.option('--simulate', is_flag=True, help='Simulate locally in CLI')
@click.pass_context
def test_flow(ctx, name, simulate):
    """Test a flow"""
    client = ctx.obj.client

    if simulate:
        # Fetch flow definition (either from file if we supported --file, or from API)
        # Assuming we fetch from API
        if not client:
            click.echo("Error: Zaptos client not initialized.", err=True)
            return

        try:
            flow_data = client._get(f"/flows/{name}")
            # Run simulation
            simulate_flow(flow_data)
        except Exception as e:
            click.echo(f"Error fetching flow for simulation: {str(e)}", err=True)
        return

    # Otherwise server-side test
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._post(f"/flows/{name}/test", json={})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error testing flow: {str(e)}", err=True)

def simulate_flow(flow_data):
    """Run a local CLI simulation of the flow"""
    click.echo(f"--- Simulating Flow: {flow_data.get('name')} ---")
    click.echo(f"Trigger: {flow_data.get('trigger', {}).get('type')}")

    steps = {s['id']: s for s in flow_data.get('steps', [])}
    if not steps:
        click.echo("No steps found.")
        return

    # Start at first step defined in list
    current_step_id = flow_data['steps'][0]['id']

    while current_step_id:
        step = steps.get(current_step_id)
        if not step:
            click.echo(f"Error: Step {current_step_id} not found.")
            break

        click.echo(f"\n[Bot]: {format_message(step.get('message'))}")

        # Determine next step
        # If buttons, user must choose
        msg = step.get('message', {})
        next_step_id = step.get('next')

        if msg.get('type') == 'buttons':
            click.echo("Options:")
            buttons = msg.get('buttons', [])
            for i, btn in enumerate(buttons):
                click.echo(f"{i+1}. {btn['text']} (ID: {btn['id']})")

            choice = click.prompt("Choose an option", type=int, default=1)
            if 0 < choice <= len(buttons):
                selected_btn = buttons[choice-1]
                # Button next overrides step next
                next_step_id = selected_btn.get('next', next_step_id)
            else:
                click.echo("Invalid choice.")
                break

        elif msg.get('type') == 'carousel':
            # Simplified carousel handling
             click.echo("(Carousel displayed)")
             next_step_id = step.get('next')

        # If explicit action like 'assign_conversation'
        if step.get('action'):
            click.echo(f"[Action]: {step['action']}")

        if not next_step_id:
            click.echo("--- End of Flow ---")
            break

        current_step_id = next_step_id

def format_message(msg):
    if not msg: return "(No message)"
    type_ = msg.get('type')
    if type_ == 'text':
        return msg.get('text')
    elif type_ == 'buttons':
        return f"{msg.get('title')} (Buttons)"
    elif type_ == 'carousel':
        return "Carousel"
    return str(msg)
