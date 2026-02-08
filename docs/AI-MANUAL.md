# Zaptos API Manual for AI Agents

**Design Principle**: Progressive Disclosure. Load only the level you need.

---

## Level 1: Quick Reference

**Context**:
- **Base URL**: `https://api.zaptoswpp.com`
- **Auth Header**: `token: {secret}` (NOT Bearer)
- **Number Format**: `55XXXXXXXXXXX` (Country code + Area code + Number. NO `+`, NO `-`)
- **Critical Change (Dec 2024)**: Use `number` and `text` fields. (NOT `phone`, NOT `message`).

| Intent | Endpoint | Minimal JSON Payload Example |
| :--- | :--- | :--- |
| **Send Text** | `POST /send/text` | `{"number": "5511999999999", "text": "Hello world"}` |
| **Send Image** | `POST /send/media` | `{"number": "5511999999999", "type": "image", "file": "https://url.com/img.jpg", "text": "Caption"}` |
| **Send Audio** | `POST /send/media` | `{"number": "5511999999999", "type": "audio", "file": "https://url.com/aud.mp3"}` |
| **Send Video** | `POST /send/media` | `{"number": "5511999999999", "type": "video", "file": "https://url.com/vid.mp4", "text": "Caption"}` |
| **Send Document** | `POST /send/media` | `{"number": "5511999999999", "type": "document", "file": "https://url.com/doc.pdf", "docName": "file.pdf"}` |
| **Send Sticker** | `POST /send/media` | `{"number": "5511999999999", "type": "sticker", "file": "https://url.com/sticker.webp"}` |
| **Send Buttons** | `POST /send/button` | `{"number": "5511999999999", "title": "Title", "buttons": [{"type": "reply", "id": "yes", "text": "Yes"}]}` |
| **Send List** | `POST /send/list` | `{"number": "5511999999999", "title": "Menu", "buttonText": "Open", "sections": [{"title": "A", "rows": [{"title": "Opt1"}]}]}` |
| **Send Carousel** | `POST /send/carousel` | `{"number": "5511999999999", "cards": [{"header": "Item 1", "body": "Desc", "image": "url", "buttons": [...]}]}` |
| **Send Location** | `POST /send/location` | `{"number": "5511999999999", "latitude": -23.55, "longitude": -46.63, "name": "Office"}` |
| **Send Contact** | `POST /send/contact` | `{"number": "5511999999999", "contactName": "John", "contactNumber": "5511888888888"}` |
| **Send PIX** | `POST /send/pix-button` | `{"number": "5511999999999", "pixKey": "key", "name": "Receiver Name"}` |
| **Campaign Simple** | `POST /sender/simple` | `{"folder": "camp1", "numbers": ["551199..."], "text": "Hi", "delayMin": 5, "delayMax": 10}` |
| **Campaign Adv.** | `POST /sender/advanced` | `{"folder_id": "camp2", "messages": [{"number": "...", "text": "..."}], "scheduled_for": 1700000000000}` |
| **Control Camp.** | `POST /sender/edit` | `{"folder_id": "camp1", "action": "stop"}` (Actions: `stop`, `continue`, `delete`) |
| **Set Presence** | `POST /message/presence` | `{"number": "5511999999999", "presence": "composing", "delay": 1200}` |
| **Check Status** | `GET /status` | *No payload* |

---

## Level 2: Detailed Usage

### 1. Authentication & Basics
- **Headers**: `{"token": "YOUR_INSTANCE_SECRET"}`
- **Number Format**: `55` (Brazil) + `DD` (Area) + `9XXXXXXXX` (Phone). Example: `5511999999999`.
- **Legacy Note**: Do NOT use `phone` or `message` in JSON keys. Use `number` and `text`.

### 2. Messaging Endpoints

#### Text Message
`POST /send/text`
```json
{
  "number": "5511999999999",
  "text": "Hello, {{name}}!", // Client-side spintax only
  "linkPreview": true // Optional
}
```

#### Media (Image, Video, Audio, Document, Sticker)
`POST /send/media`
```json
{
  "number": "5511999999999",
  "type": "image", // Options: image, video, audio, document, sticker
  "file": "https://example.com/media.jpg", // Must be a URL
  "text": "Optional caption for image/video",
  "docName": "Contract.pdf" // Required if type is 'document'
}
```

#### Buttons (Interactive)
`POST /send/button`
- **Max Buttons**: 3
- **Types**: `reply` (triggers webhook/response), `url` (opens link), `call` (dials number), `copy` (copies text).
```json
{
  "number": "5511999999999",
  "title": "Header Text",
  "description": "Body text description",
  "footer": "Footer text",
  "buttons": [
    {"type": "reply", "id": "btn_yes", "text": "Yes, I want it"},
    {"type": "url", "url": "https://google.com", "text": "Visit Website"},
    {"type": "call", "phoneNumber": "5511999999999", "text": "Call Support"},
    {"type": "copy", "copyCode": "PROMO2024", "text": "Copy Code"}
  ]
}
```

#### List Messages
`POST /send/list`
- **Max Sections**: 10
- **Max Rows per Section**: 10
```json
{
  "number": "5511999999999",
  "title": "Menu Title",
  "description": "Select an option",
  "buttonText": "Open Menu",
  "sections": [
    {
      "title": "Section 1",
      "rows": [
        {"title": "Option 1", "description": "Desc 1", "rowId": "opt_1"},
        {"title": "Option 2", "description": "Desc 2", "rowId": "opt_2"}
      ]
    }
  ]
}
```

#### Carousel
`POST /send/carousel`
- **Cards**: Array of card objects.
```json
{
  "number": "5511999999999",
  "cards": [
    {
      "header": "Card 1 Title",
      "body": "Card 1 Body",
      "image": "https://example.com/img1.jpg",
      "buttons": [
         {"type": "reply", "id": "click_1", "text": "Select 1"}
      ]
    },
    {
      "header": "Card 2 Title",
      "body": "Card 2 Body",
      "image": "https://example.com/img2.jpg",
      "buttons": [
         {"type": "reply", "id": "click_2", "text": "Select 2"}
      ]
    }
  ]
}
```
*Note: Some implementations use a string array format for `cards` where each string encodes the card. If using the simplified JSON endpoint, use the object structure above.*

### 3. Campaign Management

#### Simple Campaign (`/sender/simple`)
Best for sending the **same message** to a list of numbers.
```json
{
  "folder": "campaign_name_unique_id",
  "numbers": ["5511999999999", "5511888888888"],
  "type": "text", // or image, video, etc.
  "text": "Hello everyone!",
  "delayMin": 10, // Seconds
  "delayMax": 20, // Seconds
  "scheduled_for": 1700000000000 // Optional Unix Timestamp (ms)
}
```

#### Advanced Campaign (`/sender/advanced`)
Best for **per-recipient customization**.
```json
{
  "folder_id": "campaign_advanced_01",
  "scheduled_for": 1700000000000, // Unix Timestamp (ms)
  "delayMin": 15,
  "delayMax": 45,
  "messages": [
    {
      "number": "5511999999999",
      "type": "text",
      "text": "Hello John, special offer for you!"
    },
    {
      "number": "5511888888888",
      "type": "image",
      "file": "https://url.com/img.jpg",
      "text": "Hello Mary, check this image!"
    }
  ]
}
```

#### Campaign Control (`/sender/edit`)
Manage running campaigns.
```json
{
  "folder_id": "campaign_name_unique_id",
  "action": "stop" // Options: 'stop', 'continue', 'delete'
}
```

### 4. Instance & System
- **Check Status**: `GET /status` (Returns connection status).
- **Note**: `/instance/info` and `/connectionState` return **404**. Use `/status`.
- **Set Presence**: `POST /message/presence`
  - Simulates typing/recording.
  - `delay`: Duration in milliseconds.
```json
{
  "number": "5511999999999",
  "presence": "composing", // or 'recording', 'paused'
  "delay": 2000
}
```

---

## Level 3: Patterns and Combinations

### 1. Carousel + Reply Button Automation Loop
**Goal**: Send a carousel, user clicks a button, webhook triggers automation (e.g., GHL).

1.  **Send Carousel**:
    Use `/send/carousel` with `reply` buttons having unique IDs (e.g., `btn_product_A`).
2.  **Webhook Event**:
    Zaptos sends a webhook `messages` event when the user clicks. The `message.text` will be the button text, and `selectedId` (or similar field in response) will be `btn_product_A`.
3.  **GHL Trigger**:
    If using GoHighLevel, map the specific incoming message text or ID to a Workflow Trigger to send the next message.

### 2. Client-Side Spintax Processing
**Problem**: Server does NOT process Spintax (e.g., `{Hi|Hello}`).
**Solution**: Process it **before** sending the API request.

*Python Example:*
```python
import random
import re

def process_spintax(text):
    pattern = r"\{([^{}]+)\}"
    while True:
        match = re.search(pattern, text)
        if not match:
            break
        options = match.group(1).split("|")
        choice = random.choice(options)
        text = text[:match.start()] + choice + text[match.end():]
    return text

# Usage
raw_text = "{Hi|Hello} {{name}}, check this {offer|deal}!"
processed_text = process_spintax(raw_text)
# Payload: {"text": processed_text, ...}
```

### 3. Media Upload Flow (GCS / GHL)
**Problem**: API requires a public URL for media. Local files must be uploaded first.
**Pattern**:
1.  Upload file to a bucket (Google Cloud Storage, AWS S3, or GHL Media).
2.  Get the `public_url`.
3.  Call `/send/media` with `file: public_url`.

### 4. Presence Before Message
**Goal**: Make the bot feel human.
1.  Call `POST /message/presence` -> `{"presence": "composing", "delay": 3000}`.
2.  Wait 3 seconds (client-side sleep).
3.  Call `POST /send/text`.

### 5. Error Handling & Retries
- **401 Unauthorized**: Refresh token or check credentials.
- **404 Not Found**: Check endpoint URL or instance ID.
- **5xx Server Error**: Retry with exponential backoff.
- **Campaigns**:
  - `scheduled_for` is in **milliseconds**.
  - `messageTimestamp` in webhook events represents **queue time**, not delivery time.

### 6. Critical Notes
- **GHL Integration**: Uses V1 API.
- **Plus Sign**: Never use `+` in numbers. `5511...` is correct. `+5511...` is wrong.
- **Field Changes**: Legacy docs might say `phone`/`message`. ALWAYS use `number`/`text`.
