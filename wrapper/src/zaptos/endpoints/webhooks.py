import click
from ..cli import echo_output

@click.group()
def webhooks():
    """Manage webhooks"""
    pass

@webhooks.command('list')
@click.pass_context
def list_webhooks(ctx):
    """List webhooks"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._get("/webhooks")
        echo_output(result)
    except Exception as e:
        click.echo(f"Error listing webhooks: {str(e)}", err=True)

@webhooks.command('create')
@click.option('--url', required=True, help='Webhook URL')
@click.option('--events', required=True, help='Comma-separated events')
@click.pass_context
def create_webhook(ctx, url, events):
    """Create a webhook"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        event_list = [e.strip() for e in events.split(',')]
        result = client._post("/webhooks", json={
            "url": url,
            "events": event_list
        })
        echo_output(result)
    except Exception as e:
        click.echo(f"Error creating webhook: {str(e)}", err=True)

@webhooks.command('delete')
@click.argument('id')
@click.pass_context
def delete_webhook(ctx, id):
    """Delete a webhook"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._delete(f"/webhooks/{id}")
        echo_output(result)
    except Exception as e:
        click.echo(f"Error deleting webhook: {str(e)}", err=True)

@webhooks.command('test')
@click.argument('id')
@click.pass_context
def test_webhook(ctx, id):
    """Test a webhook"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming POST /webhooks/<id>/test
        result = client._post(f"/webhooks/{id}/test", json={})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error testing webhook: {str(e)}", err=True)
