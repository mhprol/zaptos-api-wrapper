import click
from ..cli import echo_output

@click.group()
def analytics():
    """View analytics and reports"""
    pass

@analytics.command('summary')
@click.option('--period', type=click.Choice(['day', 'week', 'month']), default='day', help='Time period')
@click.pass_context
def summary(ctx, period):
    """Get analytics summary"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming GET /analytics/summary
        result = client._get("/analytics/summary", params={"period": period})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error getting analytics summary: {str(e)}", err=True)

@analytics.command('campaign')
@click.argument('id')
@click.pass_context
def campaign_analytics(ctx, id):
    """Get campaign analytics"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming GET /analytics/campaign/<id> or /campaigns/<id>/stats
        # I'll stick to /analytics/campaign/<id> pattern based on command structure
        result = client._get(f"/analytics/campaign/{id}")
        echo_output(result)
    except Exception as e:
        click.echo(f"Error getting campaign analytics: {str(e)}", err=True)

@analytics.command('messages')
@click.option('--since', help='Start date')
@click.option('--until', help='End date')
@click.pass_context
def messages_analytics(ctx, since, until):
    """Get messages analytics"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        params = {}
        if since: params['since'] = since
        if until: params['until'] = until

        result = client._get("/analytics/messages", params=params)
        echo_output(result)
    except Exception as e:
        click.echo(f"Error getting messages analytics: {str(e)}", err=True)

@analytics.command('conversations')
@click.option('--since', help='Start date')
@click.pass_context
def conversations_analytics(ctx, since):
    """Get conversations analytics"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        params = {}
        if since: params['since'] = since

        result = client._get("/analytics/conversations", params=params)
        echo_output(result)
    except Exception as e:
        click.echo(f"Error getting conversations analytics: {str(e)}", err=True)

@analytics.command('export')
@click.option('--format', type=click.Choice(['csv', 'json']), default='json', help='Export format')
@click.pass_context
def export_analytics(ctx, format):
    """Export analytics data"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming GET /analytics/export
        result = client._get("/analytics/export", params={"format": format})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error exporting analytics: {str(e)}", err=True)
