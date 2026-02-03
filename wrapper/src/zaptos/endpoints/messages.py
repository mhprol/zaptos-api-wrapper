import click
import json
import os
from ..cli import echo_output

@click.group()
def messages():
    """Manage and send messages"""
    pass

@messages.command()
@click.argument('number')
@click.option('--text', help='Text message content')
@click.option('--image', help='Image URL')
@click.option('--caption', help='Caption for media')
@click.option('--buttons', help='Buttons JSON or string')
@click.option('--list', 'list_msg', help='List message JSON')
@click.option('--carousel', help='Carousel cards JSON or file path')
@click.option('--location', help='Location "lat,long"')
@click.option('--address', help='Location address')
@click.option('--contact-name', help='Contact card name')
@click.option('--contact-number', help='Contact card number')
@click.option('--document', help='Document URL')
@click.option('--filename', help='Document filename')
@click.option('--audio', help='Audio URL')
@click.option('--video', help='Video URL')
@click.option('--sticker', help='Sticker URL')
@click.pass_context
def send(ctx, number, text, image, caption, buttons, list_msg, carousel, location, address, contact_name, contact_number, document, filename, audio, video, sticker):
    """Send a message to a number."""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized. Check credentials.", err=True)
        return

    try:
        if text:
            result = client.send_text(number, text)

        elif image:
            result = client.send_image(number, image, caption)

        elif buttons:
            # Parse buttons if string
            try:
                data = json.loads(buttons)
            except json.JSONDecodeError:
                click.echo("Error: Invalid JSON for buttons", err=True)
                return

            # If full structure provided
            if "buttons" in data and "title" in data:
                 result = client.send_buttons(number, data["title"], data["buttons"], data.get("description"))
            else:
                 click.echo("Error: Buttons JSON must contain 'title' and 'buttons' array", err=True)
                 return

        elif list_msg:
             try:
                data = json.loads(list_msg)
             except json.JSONDecodeError:
                click.echo("Error: Invalid JSON for list", err=True)
                return

             if "sections" in data and "title" in data and "buttonText" in data:
                 result = client.send_list(number, data["title"], data["sections"], data["buttonText"], data.get("description"))
             else:
                 click.echo("Error: List JSON must contain 'title', 'sections', and 'buttonText'", err=True)
                 return

        elif carousel:
            if os.path.exists(carousel):
                with open(carousel, 'r') as f:
                    data = json.load(f)
            else:
                try:
                    data = json.loads(carousel)
                except json.JSONDecodeError:
                    click.echo("Error: Invalid JSON or file path for carousel", err=True)
                    return

            cards = data.get("cards", data) if isinstance(data, dict) else data
            result = client.send_carousel(number, cards)

        elif location:
            parts = location.split(',')
            if len(parts) != 2:
                click.echo("Error: Location must be 'lat,long'", err=True)
                return
            result = client.send_location(number, parts[0].strip(), parts[1].strip(), address, name=caption)

        elif contact_name and contact_number:
            result = client.send_contact(number, contact_name, contact_number)

        elif document:
            result = client.send_document(number, document, filename, caption)

        elif audio:
            result = client.send_audio(number, audio)

        elif video:
            result = client.send_video(number, video, caption)

        elif sticker:
            result = client.send_sticker(number, sticker)

        else:
            click.echo("Error: No message content provided. Use --text, --image, etc.", err=True)
            return

        echo_output(result)

    except Exception as e:
        click.echo(f"Error sending message: {str(e)}", err=True)
        if ctx.obj.config.output == 'json':
             echo_output({"error": str(e)})

@messages.command('list')
@click.option('--contact', help='Filter by contact number')
@click.option('--since', help='Filter messages since date')
@click.pass_context
def list_messages(ctx, contact, since):
    """List message history"""
    client = ctx.obj.client
    if not client:
        click.echo("Error: Zaptos client not initialized.", err=True)
        return

    try:
        # Implementation depends on client support
        # Assuming client._get("/messages") works
        params = {}
        if contact:
            params['contact'] = contact
        if since:
            params['since'] = since

        result = client._get("/messages", params=params)
        echo_output(result)
    except Exception as e:
        click.echo(f"Error listing messages: {str(e)}", err=True)
