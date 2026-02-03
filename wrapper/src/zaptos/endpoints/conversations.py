import click
from ..cli import echo_output

@click.group()
def conversations():
    """Manage conversations (inbox)"""
    pass

@conversations.command('list')
@click.option('--unread/--all', default=False, help='Show only unread')
@click.option('--assigned-to', help='Filter by assigned user')
@click.pass_context
def list_conversations(ctx, unread, assigned_to):
    """List conversations"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming GET /conversations endpoint
        params = {}
        if unread:
            params['unread'] = 'true'
        if assigned_to:
            params['assignedTo'] = assigned_to

        result = client._get("/conversations", params=params)
        echo_output(result)
    except Exception as e:
        click.echo(f"Error listing conversations: {str(e)}", err=True)

@conversations.command('get')
@click.argument('contact_number')
@click.pass_context
def get_conversation(ctx, contact_number):
    """Get conversation details"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming GET /conversations/<number>
        result = client._get(f"/conversations/{contact_number}")
        echo_output(result)
    except Exception as e:
        click.echo(f"Error getting conversation: {str(e)}", err=True)

@conversations.command('assign')
@click.argument('contact_number')
@click.option('--to', required=True, help='User to assign to')
@click.pass_context
def assign_conversation(ctx, contact_number, to):
    """Assign conversation to a user"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming POST /conversations/<number>/assign
        result = client._post(f"/conversations/{contact_number}/assign", json={"user": to})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error assigning conversation: {str(e)}", err=True)

@conversations.command('close')
@click.argument('contact_number')
@click.pass_context
def close_conversation(ctx, contact_number):
    """Close conversation"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming POST /conversations/<number>/close
        result = client._post(f"/conversations/{contact_number}/close", json={})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error closing conversation: {str(e)}", err=True)

@conversations.command('search')
@click.option('--query', required=True, help='Search keyword')
@click.pass_context
def search_conversations(ctx, query):
    """Search conversations"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming GET /conversations/search or ?query=
        result = client._get("/conversations/search", params={"query": query})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error searching conversations: {str(e)}", err=True)
