# Zaptos API Wrapper

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust Python CLI wrapper and client library for the Zaptos WhatsApp API, featuring GoHighLevel (GHL) integration for seamless CRM automation.

---

**🤖 For AI Agents:** Please refer to the [AI Manual](docs/AI-MANUAL.md) for detailed API specifications and progressive disclosure patterns.

---

## 📖 Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quick Start](#quick-start)
- [CLI Reference](#cli-reference)
- [API Client Usage](#api-client-usage)
- [Authentication](#authentication)
- [Error Handling](#error-handling)
- [Rate Limits & Best Practices](#rate-limits--best-practices)
- [Common Workflows](#common-workflows)
- [Contributing](#contributing)
- [License](#license)

---

## Project Description

The **Zaptos API Wrapper** provides a unified interface to interact with the Zaptos WhatsApp API. It simplifies sending messages (text, media, interactive), managing campaigns, and syncing contacts with GoHighLevel (GHL).

**Key Features:**
- 📤 **Messaging**: Send text, images, videos, audio, documents, stickers, locations, contacts, buttons, lists, and carousels.
- 🚀 **Campaign Management**: Create, start, and track bulk messaging campaigns.
- 🔗 **GoHighLevel Integration**: Sync contacts and trigger automations directly from GHL tags.
- 💬 **Conversation Management**: Manage inbox conversations programmatically.
- 🛠️ **CLI Power**: extensive command-line interface for manual operations and scripting.

## Installation

Clone the repository and install the package:

```bash
# Clone the repository
git clone https://github.com/your-org/zaptos-api-wrapper.git
cd zaptos-api-wrapper

# Install in editable mode
pip install -e ./wrapper

# For development (includes testing tools)
pip install -e "./wrapper[dev]"
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

# 3. Send Buttons (Interactive)
client.send_buttons(
    number="5511999999999",
    title="Choose an option",
    buttons=[
        {"type": "reply", "id": "yes", "text": "Yes"},
        {"type": "reply", "id": "no", "text": "No"}
    ],
    description="Please select one"
)

# 4. Send a Carousel
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

## CLI Reference

The CLI provides a convenient way to interact with the API from the terminal.

### Global Options
- `--instance`: Override `ZAPTOS_INSTANCE`.
- `--token`: Override `ZAPTOS_TOKEN`.
- `--ghl-key`: Override `GHL_API_KEY`.
- `--output`: Output format (default: `json`).
- `--debug`: Enable debug logging.

### Messages (`zaptos messages`)

Send various types of messages.

```bash
# Send Text
zaptos messages send 5511999999999 --text "Hello World"

# Send Image
zaptos messages send 5511999999999 --image "https://example.com/pic.jpg" --caption "Nice view"

# Send Buttons (JSON string)
zaptos messages send 5511999999999 --buttons '{"title": "Vote", "buttons": [{"type": "reply", "id": "1", "text": "Up"}, {"type": "reply", "id": "2", "text": "Down"}]}'

# Send Carousel (from file)
zaptos messages send 5511999999999 --carousel carousel.json
```

### Campaigns (`zaptos campaigns`)

Manage bulk messaging campaigns.

```bash
# Create a campaign targeting contacts with a specific GHL tag
zaptos campaigns create \
  --name "New Year Promo" \
  --ghl-tag "active-leads" \
  --template "Happy New Year {{name}}! Check our offers."

# Start the campaign
zaptos campaigns start <campaign_id>

# Check status
zaptos campaigns status <campaign_id>
```

### Other Commands
- `zaptos contacts`: Manage contacts and sync with GoHighLevel.
- `zaptos conversations`: List and manage inbox conversations.
- `zaptos templates`: Manage message templates.
- `zaptos webhooks`: Configure and test webhooks.
- `zaptos analytics`: View delivery reports and usage stats.
- `zaptos flows`: Manage chatbot flows.

Run `zaptos <command> --help` for more details.

## API Client Usage

The `ZaptosClient` exposes the following methods:

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

## Authentication

The API uses header-based authentication. The client handles this automatically using the `token` parameter.

**Header Format:**
```http
token: {secret}
```
*Note: Do NOT use `Bearer` prefix.*

## Error Handling

The client uses `httpx` and will raise exceptions for HTTP errors.

- **401 Unauthorized**: Invalid token or instance ID.
- **404 Not Found**: Invalid endpoint or instance not connected.
- **5xx Server Error**: API server issues.

**Example Error Handling:**
```python
import httpx
from zaptos.client import ZaptosClient

try:
    client.send_text("5511999999999", "Hello")
except httpx.HTTPStatusError as e:
    print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
except httpx.RequestError as e:
    print(f"Request Error: {e}")
```

## Rate Limits & Best Practices

- **Delays**: When sending bulk messages, introduce a delay between requests (e.g., 5-15 seconds) to avoid being flagged for spam. The CLI campaign runner handles this automatically.
- **Number Format**: Always use the format `55XXXXXXXXXXX` (Country Code + Area Code + Number). Do not use `+` or `-`.
- **Media**: Ensure media URLs are publicly accessible.

## Common Workflows

### 1. Loop Through Contacts
It is common to iterate through a list of contacts and send personalized messages.

```python
contacts = [
    {"number": "5511999999999", "name": "Alice"},
    {"number": "5511888888888", "name": "Bob"}
]

for contact in contacts:
    message = f"Hello {contact['name']}, check our new offer!"
    client.send_text(contact['number'], message)
    time.sleep(5)  # Respect rate limits
```

### 2. GHL Sync and Blast
1. Fetch contacts from GHL using a tag.
2. Send a message to each contact via Zaptos.
3. (Optional) Update GHL with the status.

*This workflow is built-in via `zaptos campaigns` CLI.*

## Contributing

Contributions are welcome! Please follow these steps:

1.  **Fork the repository**.
2.  **Install dependencies**: `pip install -e ".[dev]"`
3.  **Run tests**: `pytest wrapper/tests`
4.  **Lint your code**: Ensure your code follows the project's style (using `ruff` and `mypy`).
5.  **Submit a Pull Request**.

## License

Distributed under the MIT License.
