# Zaptos API Wrapper

Python CLI wrapper for Zaptos WhatsApp API — Commercial automation platform with GHL integration.

## Features

- 📤 **Messages**: Send text, images, buttons, carousels, lists
- 📊 **Campaigns**: Bulk messaging with scheduling and tracking
- 💬 **Conversations**: Unified inbox management
- 👥 **Contacts**: Sync with GoHighLevel CRM
- 📝 **Templates**: Message template management
- 🔗 **Webhooks**: Event handling and notifications
- 📈 **Analytics**: Reports and metrics
- 🤖 **Flows**: Chatbot automation (YAML-based)

## Installation

```bash
cd wrapper
pip install -e .
```

## Usage

```bash
# Send message
zaptos messages send 5511999999999 --text "Hello!"

# Create campaign  
zaptos campaigns create --name "Promo" --ghl-tag "leads" --template promo1

# List conversations
zaptos conversations list --unread

# Sync contacts from GHL
zaptos contacts sync-ghl --tag "customers"
```

## Configuration

```bash
export ZAPTOS_INSTANCE="your_instance"
export ZAPTOS_TOKEN="your_token"
export GHL_API_KEY="your_ghl_key"
export GHL_LOCATION_ID="your_location"
```

## License

MIT
