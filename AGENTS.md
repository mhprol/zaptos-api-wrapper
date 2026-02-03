# AGENTS.md — Zaptos WhatsApp API Wrapper

## Project Overview

Build a Python CLI wrapper for the Zaptos WhatsApp API, creating a commercial-grade WhatsApp automation platform with GHL (GoHighLevel) CRM integration.

**Benchmark**: WhatFlow.app — Features to match or exceed:
- Bulk messaging / broadcasts
- Live inbox (conversation management)
- Chatbot flows
- Template management
- Analytics & reporting
- CRM integration (we use GHL)

## Architecture

```
zaptos-api-wrapper/
├── wrapper/
│   ├── zaptos                   # Main CLI entrypoint
│   ├── pyproject.toml
│   └── src/
│       └── zaptos/
│           ├── __init__.py
│           ├── cli.py           # Click CLI
│           ├── client.py        # Zaptos API client
│           ├── config.py        # Instance/token management
│           ├── ghl.py           # GHL integration layer
│           └── endpoints/
│               ├── __init__.py
│               ├── messages.py      # Send, templates, media
│               ├── campaigns.py     # Bulk messaging, scheduling
│               ├── conversations.py # Inbox, threads, assignments
│               ├── contacts.py      # Sync with GHL
│               ├── templates.py     # Template CRUD
│               ├── webhooks.py      # Event handling
│               ├── analytics.py     # Reports, metrics
│               └── flows.py         # Chatbot automation
├── docs/
│   └── api-reference.md
└── AGENTS.md
```

## Zaptos API Reference

**Base URL**: `https://api.zaptoswpp.com/{instance}/`
**Auth**: Header `token: {secret}`

### Core Endpoints

```
POST /send-text           # Send text message
POST /send-image          # Send image with caption
POST /send-buttons        # Interactive buttons (REPLY/URL/COPY/CALL)
POST /send-list           # List message with sections
POST /send-carousel       # Product carousel (up to 10 cards)
POST /send-location       # Location message
POST /send-contact        # Contact card
POST /send-document       # PDF, docs, etc.
POST /send-audio          # Audio/voice message
POST /send-video          # Video message
POST /send-sticker        # Sticker message

GET  /messages            # Get message history
GET  /contacts            # List contacts
POST /contacts            # Create/update contact
GET  /groups              # List groups
GET  /status              # Instance status
GET  /qrcode              # Get QR for pairing

# Webhooks (received at your endpoint)
- message.received
- message.sent
- message.delivered
- message.read
- button.clicked
- presence.update
```

### Message Types

```python
# Text
{"number": "5511999999999", "text": "Hello!"}

# Buttons (up to 3)
{
  "number": "5511999999999",
  "title": "Choose an option",
  "description": "Select below",
  "buttons": [
    {"id": "btn1", "text": "Option 1"},
    {"id": "btn2", "text": "Option 2"}
  ]
}

# Carousel (up to 10 cards)
{
  "number": "5511999999999",
  "cards": [
    {
      "title": "Product 1",
      "description": "Description here",
      "image": "https://...",
      "buttons": [{"id": "buy1", "text": "Buy Now"}]
    }
  ]
}
```

## CLI Design

### Command Structure

```bash
zaptos <resource> <action> [options]
```

### Resources

1. **messages** — Send and manage messages
2. **campaigns** — Bulk messaging and scheduling
3. **conversations** — Inbox and thread management
4. **contacts** — Contact management + GHL sync
5. **templates** — Message template CRUD
6. **webhooks** — Webhook configuration
7. **analytics** — Reports and metrics
8. **flows** — Chatbot automation

### Commands

```bash
# Messages
zaptos messages send <number> --text "Hello"
zaptos messages send <number> --image ./photo.jpg --caption "Check this"
zaptos messages send <number> --buttons '{"title":"Choose","buttons":[...]}'
zaptos messages send <number> --carousel ./products.json
zaptos messages list [--contact NUMBER] [--since DATE]

# Campaigns (bulk)
zaptos campaigns create --name "Promo" --contacts ./list.csv --template promo1
zaptos campaigns create --name "Promo" --ghl-tag "leads" --template promo1
zaptos campaigns list [--status active|paused|completed]
zaptos campaigns start <id>
zaptos campaigns pause <id>
zaptos campaigns status <id>
zaptos campaigns delete <id>

# Conversations (inbox)
zaptos conversations list [--unread] [--assigned-to USER]
zaptos conversations get <contact_number>
zaptos conversations assign <contact_number> --to <user>
zaptos conversations close <contact_number>
zaptos conversations search --query "keyword"

# Contacts
zaptos contacts list [--limit N] [--query Q]
zaptos contacts get <number>
zaptos contacts create --number 5511999999999 --name "John"
zaptos contacts sync-ghl [--tag TAG] [--since DATE]  # Sync from GHL
zaptos contacts push-ghl <number>                     # Push to GHL

# Templates
zaptos templates list
zaptos templates get <name>
zaptos templates create --name promo1 --file template.json
zaptos templates update <name> --file template.json
zaptos templates delete <name>
zaptos templates preview <name> --number 5511999999999

# Webhooks
zaptos webhooks list
zaptos webhooks create --url https://... --events message.received,button.clicked
zaptos webhooks delete <id>
zaptos webhooks test <id>

# Analytics
zaptos analytics summary [--period day|week|month]
zaptos analytics campaign <id>
zaptos analytics messages --since DATE --until DATE
zaptos analytics conversations --since DATE
zaptos analytics export --format csv|json

# Flows (chatbot)
zaptos flows list
zaptos flows get <name>
zaptos flows create --name welcome --file flow.yaml
zaptos flows update <name> --file flow.yaml
zaptos flows enable <name>
zaptos flows disable <name>
zaptos flows test <name> --simulate
```

### Global Options

```bash
--instance NAME      # Override env ZAPTOS_INSTANCE
--token TOKEN        # Override env ZAPTOS_TOKEN
--ghl-key KEY        # Override env GHL_API_KEY (for sync)
--ghl-location ID    # Override env GHL_LOCATION_ID
--output json        # Always JSON (default)
-v, -vv              # Verbosity
--dry-run            # Show without executing
--debug              # HTTP details
```

## GHL Integration

The wrapper integrates with GoHighLevel for:

1. **Contact Sync**: Pull contacts by tag/filter, push updates back
2. **Workflow Triggers**: Webhook events can trigger GHL workflows
3. **Conversation Sync**: WhatsApp conversations visible in GHL
4. **Custom Fields**: Map WhatsApp data to GHL custom fields

```python
# Example: Sync contacts from GHL tag
def sync_from_ghl(client: ZaptosClient, ghl_client: GHLClient, tag: str):
    contacts = ghl_client.contacts.list(query=f"tags:{tag}")
    for contact in contacts:
        client.contacts.create_or_update(
            number=contact['phone'],
            name=contact['name'],
            metadata={'ghl_id': contact['id']}
        )
```

## Flow Definition (Chatbot)

Flows are defined in YAML:

```yaml
# flows/welcome.yaml
name: welcome
trigger:
  type: keyword
  keywords: ["oi", "olá", "hello", "hi"]

steps:
  - id: greeting
    message:
      type: buttons
      title: "Olá! Como posso ajudar?"
      buttons:
        - id: products
          text: "Ver produtos"
          next: show_products
        - id: support
          text: "Falar com atendente"
          next: transfer_human
        - id: hours
          text: "Horário de funcionamento"
          next: show_hours

  - id: show_products
    message:
      type: carousel
      source: ghl_products  # Pull from GHL
    next: ask_interest

  - id: transfer_human
    action: assign_conversation
    to: available_agent
    message:
      type: text
      text: "Um momento, vou transferir você para um atendente."

  - id: show_hours
    message:
      type: text
      text: "Funcionamos de segunda a sexta, das 9h às 18h."
    next: greeting  # Loop back
```

## Implementation Notes

### HTTP Client

```python
import httpx

class ZaptosClient:
    def __init__(self, instance: str, token: str):
        self.base_url = f"https://api.zaptoswpp.com/{instance}"
        self.client = httpx.Client(
            base_url=self.base_url,
            headers={"token": token}
        )
    
    def send_text(self, number: str, text: str) -> dict:
        return self.client.post("/send-text", json={
            "number": number,
            "text": text
        }).json()
```

### Campaign Engine

```python
class CampaignManager:
    def __init__(self, client: ZaptosClient, db: Database):
        self.client = client
        self.db = db
    
    async def run_campaign(self, campaign_id: str):
        campaign = self.db.get_campaign(campaign_id)
        contacts = self.db.get_campaign_contacts(campaign_id)
        
        for contact in contacts:
            # Apply template with contact data
            message = render_template(campaign.template, contact)
            
            # Send with rate limiting
            await self.client.send(contact.number, message)
            await asyncio.sleep(random.uniform(2, 5))  # Anti-detection
            
            # Track
            self.db.log_message(campaign_id, contact.id, message)
```

## Deliverables

1. Working CLI with all 8 resources
2. Full Zaptos API coverage
3. GHL integration (sync contacts, push events)
4. Campaign management with scheduling
5. Conversation inbox management
6. Flow/chatbot YAML parser and executor
7. Analytics and reporting
8. Webhook handling

## Priority Order

1. Core client + config + CLI skeleton
2. messages (foundation)
3. contacts + GHL sync
4. campaigns (bulk)
5. conversations (inbox)
6. templates
7. webhooks
8. analytics
9. flows (chatbot)

## Style

- Python 3.11+
- Type hints everywhere
- `ruff` for linting
- `click` for CLI
- `httpx` for HTTP (async-capable)
- `pydantic` for models
- Minimal dependencies
