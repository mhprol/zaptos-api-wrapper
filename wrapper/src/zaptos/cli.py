import click
import os
import json
from .config import config
from .client import ZaptosClient
from .ghl import GHLClient

class ContextObj:
    def __init__(self):
        self.config = config
        self.client = None
        self.ghl_client = None

@click.group()
@click.option('--instance', help='Override ZAPTOS_INSTANCE')
@click.option('--token', help='Override ZAPTOS_TOKEN')
@click.option('--ghl-key', help='Override GHL_API_KEY')
@click.option('--ghl-location', help='Override GHL_LOCATION_ID')
@click.option('--output', default='json', help='Output format (json)')
@click.option('--debug/--no-debug', default=False, help='Enable debug logging')
@click.pass_context
def cli(ctx, instance, token, ghl_key, ghl_location, output, debug):
    """Zaptos WhatsApp API CLI Wrapper"""
    ctx.obj = ContextObj()

    # Update config from options
    if instance:
        ctx.obj.config.zaptos_instance = instance
    if token:
        ctx.obj.config.zaptos_token = token
    if ghl_key:
        ctx.obj.config.ghl_api_key = ghl_key
    if ghl_location:
        ctx.obj.config.ghl_location_id = ghl_location
    ctx.obj.config.output = output

    # Initialize clients if credentials are present
    if ctx.obj.config.zaptos_instance and ctx.obj.config.zaptos_token:
        ctx.obj.client = ZaptosClient(
            instance=ctx.obj.config.zaptos_instance,
            token=ctx.obj.config.zaptos_token
        )

    if ctx.obj.config.ghl_api_key:
        ctx.obj.ghl_client = GHLClient(
            api_key=ctx.obj.config.ghl_api_key,
            location_id=ctx.obj.config.ghl_location_id
        )

# Helper to format output
def echo_output(data):
    click.echo(json.dumps(data, indent=2))

from .endpoints import messages, contacts, campaigns, conversations, templates, webhooks, analytics, flows
cli.add_command(messages.messages)
cli.add_command(contacts.contacts)
cli.add_command(campaigns.campaigns)
cli.add_command(conversations.conversations)
cli.add_command(templates.templates)
cli.add_command(webhooks.webhooks)
cli.add_command(analytics.analytics)
cli.add_command(flows.flows)
