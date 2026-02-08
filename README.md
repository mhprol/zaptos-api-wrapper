# Zaptos API Wrapper

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust Python CLI wrapper and client library for the Zaptos WhatsApp API, featuring GoHighLevel (GHL) integration for seamless CRM automation.

---

**🤖 For AI Agents:** Please refer to the [AI Manual](docs/AI-MANUAL.md) for detailed API specifications and progressive disclosure patterns.

---

## Features

- 📤 **Comprehensive Messaging**: Send text, images, videos, audio, documents, stickers, locations, contacts, buttons, lists, and carousels.
- 🚀 **Campaign Management**: Create and manage bulk messaging campaigns with scheduling and tracking.
- 🔗 **GoHighLevel Integration**: Sync contacts and trigger automations directly from GHL tags.
- 💬 **Conversation Management**: Access and manage inbox conversations programmatically.
- 🤖 **Chatbot Flows**: Design and deploy chatbot flows (YAML-based).
- 📊 **Analytics**: View reports and metrics on message delivery and campaign performance.
- 🛠️ **CLI Power**: Full command-line interface for manual operations and scripting.

## Installation

You can install the package directly from the source:

```bash
# Clone the repository
git clone https://github.com/your-org/zaptos-api-wrapper.git
cd zaptos-api-wrapper/wrapper

# Install in editable mode
pip install -e .

# For development (includes testing tools)
pip install -e ".[dev]"
```

## Configuration

The wrapper can be configured using environment variables or a configuration file.

### Environment Variables

Set the following environment variables in your shell or `.env` file:

```bash
export ZAPTOS_INSTANCE="your_instance_id"
export ZAPTOS_TOKEN="your_api_token"
export GHL_API_KEY="your_ghl_api_key"       # Optional: For GHL integration
export GHL_LOCATION_ID="your_ghl_location"  # Optional: For GHL integration
```

### Configuration Profiles

You can also use configuration profiles stored in `~/.config/zaptos/profiles.yaml`. Use the `--profile` flag with CLI commands to switch between environments.

## Quick Start

### Python Client

Use the `ZaptosClient` class to interact with the API programmatically.

```python
from zaptos.client import ZaptosClient

# Initialize client
client = ZaptosClient(
    instance="your_instance_id",
    token="your_api_token"
)

# 1. Send a Text Message
client.send_text("5511999999999", "Hello from Zaptos Wrapper!")

# 2. Send Media (Image)
client.send_image(
    number="5511999999999",
    url="https://example.com/image.jpg",
    caption="Check this out!"
)

# 3. Send a Carousel
cards = [
    {
        "header": "Product A",
        "body": "Description of Product A",
        "image": "https://example.com/product-a.jpg",
        "buttons": [{"type": "reply", "id": "btn_a", "text": "Buy Now"}]
    },
    {
        "header": "Product B",
        "body": "Description of Product B",
        "image": "https://example.com/product-b.jpg",
        "buttons": [{"type": "reply", "id": "btn_b", "text": "Learn More"}]
    }
]
client.send_carousel("5511999999999", cards)
```

### CLI Usage

The CLI provides a convenient way to interact with the API from the terminal.

#### Send a Message

```bash
# Send Text
zaptos messages send 5511999999999 --text "Hello World"

# Send Image
zaptos messages send 5511999999999 --image "https://example.com/pic.jpg" --caption "Nice view"

# Send Carousel (from JSON string)
zaptos messages send 5511999999999 --carousel '[{"header":"Title","body":"Desc","image":"url","buttons":[{"type":"reply","id":"1","text":"Btn"}]}]'
```

#### Create a Campaign

```bash
# Create a campaign targeting contacts with a specific GHL tag
zaptos campaigns create \
  --name "New Year Promo" \
  --ghl-tag "active-leads" \
  --template "Happy New Year {{name}}! Check our offers."

# Start the campaign
zaptos campaigns start <campaign_id>
```

## CLI Reference

Run `zaptos --help` for a full list of commands.

- `zaptos messages` - Manage and send messages (text, media, interactive).
- `zaptos campaigns` - Manage bulk messaging campaigns (create, list, start, pause, stop).
- `zaptos contacts` - Manage contacts and sync with GoHighLevel.
- `zaptos conversations` - List and manage inbox conversations.
- `zaptos templates` - Manage message templates.
- `zaptos webhooks` - Configure and test webhooks.
- `zaptos analytics` - View delivery reports and usage stats.
- `zaptos flows` - Manage chatbot flows.

## API Client Reference

The `ZaptosClient` exposes the following methods for direct API interaction:

| Method | Description |
| :--- | :--- |
| `send_text(number, text)` | Send a text message. |
| `send_image(number, url, caption)` | Send an image with optional caption. |
| `send_video(number, url, caption)` | Send a video with optional caption. |
| `send_audio(number, url)` | Send an audio file. |
| `send_document(number, url, filename, caption)` | Send a document (PDF, DOCX, etc). |
| `send_sticker(number, url)` | Send a sticker (WebP format). |
| `send_location(number, lat, long, address, name)` | Send a location pin. |
| `send_contact(number, name, contact_number)` | Send a vCard contact. |
| `send_buttons(number, title, buttons, description)` | Send interactive buttons (max 3). |
| `send_list(number, title, sections, button_text)` | Send a list menu. |
| `send_carousel(number, cards)` | Send a carousel with multiple cards. |

## Contributing

Contributions are welcome! Please follow these steps:

1.  **Fork the repository**.
2.  **Install dependencies**: `pip install -e ".[dev]"`
3.  **Run tests**: `pytest wrapper/tests`
4.  **Lint your code**: Ensure your code follows the project's style (using `ruff` and `mypy`).
5.  **Submit a Pull Request**.

## License

Distributed under the MIT License.
