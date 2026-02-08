import click
import json

def echo_output(data):
    """Helper to format output as JSON."""
    click.echo(json.dumps(data, indent=2))
