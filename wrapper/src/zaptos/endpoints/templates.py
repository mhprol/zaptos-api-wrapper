import click
import json
import os
from ..cli import echo_output

@click.group()
def templates():
    """Manage message templates"""
    pass

@templates.command('list')
@click.pass_context
def list_templates(ctx):
    """List templates"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._get("/templates")
        echo_output(result)
    except Exception as e:
        click.echo(f"Error listing templates: {str(e)}", err=True)

@templates.command('get')
@click.argument('name')
@click.pass_context
def get_template(ctx, name):
    """Get template details"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._get(f"/templates/{name}")
        echo_output(result)
    except Exception as e:
        click.echo(f"Error getting template: {str(e)}", err=True)

@templates.command('create')
@click.option('--name', required=True, help='Template name')
@click.option('--file', required=True, help='Template JSON file')
@click.pass_context
def create_template(ctx, name, file):
    """Create a template"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    if not os.path.exists(file):
        click.echo(f"Error: File {file} not found", err=True)
        return

    try:
        with open(file, 'r') as f:
            data = json.load(f)

        # Ensure name in data matches or is set
        data['name'] = name

        result = client._post("/templates", json=data)
        echo_output(result)
    except Exception as e:
        click.echo(f"Error creating template: {str(e)}", err=True)

@templates.command('update')
@click.argument('name')
@click.option('--file', required=True, help='Template JSON file')
@click.pass_context
def update_template(ctx, name, file):
    """Update a template"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    if not os.path.exists(file):
        click.echo(f"Error: File {file} not found", err=True)
        return

    try:
        with open(file, 'r') as f:
            data = json.load(f)

        # Ensure name in data matches or is set
        data['name'] = name # Though usually name is immutable in WA

        # Using PUT or POST update? Assuming PUT /templates/<name>
        result = client._put(f"/templates/{name}", json=data)
        echo_output(result)
    except Exception as e:
        click.echo(f"Error updating template: {str(e)}", err=True)

@templates.command('delete')
@click.argument('name')
@click.pass_context
def delete_template(ctx, name):
    """Delete a template"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        result = client._delete(f"/templates/{name}")
        echo_output(result)
    except Exception as e:
        click.echo(f"Error deleting template: {str(e)}", err=True)

@templates.command('preview')
@click.argument('name')
@click.option('--number', required=True, help='Phone number to send preview to')
@click.pass_context
def preview_template(ctx, name, number):
    """Preview a template"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Assuming endpoint for previewing/sending template
        # Usually it's just sending a message using the template.
        # But maybe there is a specific preview endpoint.
        # I'll assume POST /templates/<name>/preview

        result = client._post(f"/templates/{name}/preview", json={"number": number})
        echo_output(result)
    except Exception as e:
        click.echo(f"Error previewing template: {str(e)}", err=True)
