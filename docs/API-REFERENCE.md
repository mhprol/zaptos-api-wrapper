# ZaptosWPP API Reference

> **Purpose**: Consolidated API intel for ZaptosWPP integration  
> **Last Updated**: 2025-12-16  
> **Source**: Validation tests + production usage

---

## Quick Facts

| Item | Value |
|------|-------|
| Base URL | `https://api.zaptoswpp.com` |
| Auth Header | `token: {secret}` |
| Instance | `whatsapp3` (Caiçara), `whatsapp4` (Food & Health) |
| Field Format | `number` + `text` (NOT phone + message) |

---

## Environment Variables

**Canonical names** (from `.env`):

| Variable | Purpose | Example |
|----------|---------|---------|
| `ZAPTOS_API_BASE_URL` | API base URL | `https://api.zaptoswpp.com` |
| `ZAPTOS_INSTANCE_PATH` | Instance identifier | `whatsapp3` |
| `ZAPTOS_API_TOKEN` | Authentication token | `abc123-...` |
| `ZAPTOS_TEST_PHONE` | Default test recipient | `55XXXXXXXXXXX` |
| `ZAPTOS_TEST_PHONE_ALT` | Alternate test (for presence) | `55XXXXXXXXXXX` |
| `ZAPTOS_PIX_KEY` | PIX key for payments | CNPJ or phone |
| `ZAPTOS_PIX_NAME` | PIX recipient name | Business name |

**Common mistakes**:
```python
# WRONG - these names don't exist
os.getenv("ZAPTOS_BASE_URL")      # → None
os.getenv("ZAPTOS_INSTANCE")      # → None  
os.getenv("ZAPTOS_TOKEN")         # → None

# CORRECT
os.getenv("ZAPTOS_API_BASE_URL")  # → https://api.zaptoswpp.com
os.getenv("ZAPTOS_INSTANCE_PATH") # → whatsapp3
os.getenv("ZAPTOS_API_TOKEN")     # → (token value)
```

---

## Endpoints We Use

### Campaign Management

| Endpoint | Method | Purpose | Notes |
|----------|--------|---------|-------|
| `/sender/simple` | POST | Create simple campaign | Basic text/media |
| `/sender/advanced` | POST | Create advanced campaign | Per-recipient customization, carousels |
| `/sender/edit` | POST | Control campaign | `action`: start, stop, continue, delete |
| `/sender/listfolders` | GET | List campaigns | Returns folder stats |
| `/sender/listmessages` | POST | List messages in campaign | Individual message status |
| `/sender/cleardone` | POST | Clear completed messages | Cleanup |
| `/sender/clearall` | DELETE | Clear all messages | Full reset |

### Messaging

| Endpoint | Method | Purpose | Notes |
|----------|--------|---------|-------|
| `/send/text` | POST | Send text message | Fields: `number`, `text` |
| `/send/media` | POST | Send image/video/doc | URL-based |
| `/send/carousel` | POST | Send carousel | Up to 10 cards |
| `/send/menu` | POST | Send interactive menu | Types: button, list, poll |
| `/send/location` | POST | Send location | Lat/long with name |
| `/send/pix-button` | POST | PIX quick copy button | No amount |
| `/send/request-payment` | POST | Full PIX payment | With amount |
| `/message/presence` | POST | Typing indicator | `composing`, `recording`, `paused` |

### Instance

| Endpoint | Method | Purpose | Notes |
|----------|--------|---------|-------|
| `/status` | GET | Health check | Works |
| `/instance/info` | GET | Instance details | 404 after API update |
| `/instance/connectionState` | GET | Connection state | 404 after API update |

### Media

| Endpoint | Method | Purpose | Notes |
|----------|--------|---------|-------|
| `/medias/upload-file` | POST | Upload media file | Returns GCS URL |

---

## Field Mappings

### CRITICAL: Field Name Changes (Dec 2024 API Update)

| Documentation Says | API Actually Uses | Context |
|-------------------|-------------------|---------|
| `phone` | `number` | All send endpoints |
| `message` | `text` | Text message content |

```python
# WRONG (old docs)
payload = {"phone": "5511999999999", "message": "Hello"}

# CORRECT (current API)
payload = {"number": "5511999999999", "text": "Hello"}
```

### Carousel Format (`choices[]`)

The `/sender/advanced` endpoint uses a `choices[]` array for carousels:

```python
choices = [
    # Card 1
    "[Card Title\nCard description text]",    # Header (title + description)
    "{https://image.url/image.png}",          # Image URL in curly braces
    "Button Text|https://url.com",            # URL button
    "Button Text|reply:callback_id",          # REPLY button (trackable)
    "Button Text|copy:text_to_copy",          # COPY button
    "Button Text|call:5511999999999",         # CALL button
    # Card 2...
]
```

**Button Types**:
| Type | Format | Use Case |
|------|--------|----------|
| URL | `Text\|https://...` | Open link |
| REPLY | `Text\|reply:callback` | Trackable CTA (webhooks) |
| COPY | `Text\|copy:text` | Copy to clipboard |
| CALL | `Text\|call:number` | Initiate phone call |

**Conversion function**:
```python
def yaml_cards_to_choices(cards: list[dict]) -> list[str]:
    """Convert YAML card definitions to choices[] format."""
    choices = []
    for card in cards:
        # Header
        choices.append(f"[{card['title']}\n{card.get('description', '')}]")
        # Image
        if card.get('image'):
            choices.append(f"{{{card['image']}}}")
        # Buttons
        for btn in card.get('buttons', []):
            if btn['type'] == 'URL':
                choices.append(f"{btn['text']}|{btn['url']}")
            elif btn['type'] == 'REPLY':
                choices.append(f"{btn['text']}|reply:{btn['id']}")
            elif btn['type'] == 'COPY':
                choices.append(f"{btn['text']}|copy:{btn['payload']}")
            elif btn['type'] == 'CALL':
                choices.append(f"{btn['text']}|call:{btn['number']}")
    return choices
```

---

## Status Values

### Campaign Status (folder-level)

| Status | Description |
|--------|-------------|
| `scheduled` | Queued for sending |
| `sending` | Currently sending messages |
| `paused` | Paused by user |
| `done` | All messages processed |
| `deleting` | Being deleted |

**Transitions**:
```
scheduled → sending → done
         ↘ paused (if paused)
              ↘ scheduled (if resumed)
```

### Message Status (message-level)

| Status | Description |
|--------|-------------|
| `scheduled` | Queued, waiting to be sent |
| `Sent` | Sent but not yet delivered (in transit) |
| `Delivered` | Successfully delivered to recipient |
| `Read` | Recipient opened/read the message |
| `Played` | Recipient played audio/video |
| `Failed` | Failed to send (check `error` field) |

**Lifecycle**:
```
scheduled → Sent → Delivered → Read/Played
                            ↘ Failed
```

**Code constants**:
```python
SENT_STATUSES = {"Sent", "Delivered", "Read", "Played"}
FAILED_STATUSES = {"Failed"}
```

### Folder Stats Fields

```json
{
  "log_total": 5,
  "log_sucess": 4,      // Note: API typo "sucess" not "success"
  "log_delivered": 3,
  "log_read": 1,
  "log_played": 0,
  "log_failed": 1
}
```

---

## Scheduling & Control

### Timestamp Scheduling

Campaigns accept Unix timestamp in **milliseconds**:

```python
import time

# Schedule for specific time
scheduled_for = int(time.time() * 1000) + (60 * 1000)  # 1 minute from now

# In API payload
payload = {
    "folder_name": "my-campaign",
    "scheduled_for": scheduled_for,  # Unix ms
    "delayMin": 12,
    "delayMax": 25,
    # ...
}
```

**Accuracy**: ~3 seconds variance from scheduled time (validated).

### Pause/Resume

```python
# Pause
POST /sender/edit
{"folder_id": "xxx", "action": "stop"}
# Response: {"status": "paused"}

# Resume  
POST /sender/edit
{"folder_id": "xxx", "action": "continue"}
# Response: {"status": "scheduled"}
```

**Behavior**:
- Pause takes effect within ~10 seconds
- No messages sent during pause (validated with 71s pause window)
- Resume continues from where it stopped
- No message drift or duplication

### Delays

```python
payload = {
    "delayMin": 12,   # Minimum seconds between messages
    "delayMax": 25,   # Maximum seconds between messages
}
```

**Note**: Per-message `delay` parameter is IGNORED by API. Use `delayMin`/`delayMax` only.

---

## Known Quirks & Gotchas

### 1. Spintax NOT Processed Server-Side

ZaptosWPP does NOT process spintax. Text arrives as-is:
```
# Sent
{Oi|Ola}, {{firstName}}!

# Received (raw, not processed)
{Oi|Ola}, {{firstName}}!
```

**Solution**: Process with `SpintaxProcessor` BEFORE building payload.

### 2. Presence Indicators Need Different Target

Presence indicators (`composing`, `recording`) don't display when sent to the instance's own number. Use a different target phone for testing.

### 3. Instance Endpoints Return 404

After Dec 2024 API update:
- `/instance/info` → 404
- `/instance/connectionState` → 404
- `/status` → Works (use this for health check)

### 4. Folder Status Returns None After Control

After pause/resume, `list_campaigns()` may return `status: None` briefly. Poll again after 1-2 seconds.

### 5. messageTimestamp Is Queue Time

`messageTimestamp` = when message was added to queue, NOT when it was actually sent. For accurate timing analysis, use webhook events (Phase 3).

### 6. Status Response Nesting

```python
# WRONG
connected = response.get("connected")  # → None

# CORRECT
connected = response.get("status", {}).get("connected")  # → True/False
```

---

## GHL Integration

### Media Upload

```
POST https://services.leadconnectorhq.com/medias/upload-file
Headers:
  Authorization: Bearer {location_token}
  Version: 2021-07-28
Body (multipart/form-data):
  file: binary
  name: string
Response:
  url: "https://storage.googleapis.com/msgsndr/{location_id}/media/{uuid}.png"
```

### Contact Phone Format

GHL returns E.164 format (`+5511999999999`), which is ZaptosWPP-compatible.

Filter for Brazilian phones:
```python
contacts = [c for c in all_contacts if c.phone and c.phone.startswith('+55')]
```

---

## Validation Summary

| Test | Status | Key Finding |
|------|--------|-------------|
| T1: Server-side delays | PASS | ~36s avg, within 30-60s range |
| T2: Presence indicators | PASS | 3/3 types working |
| T3: Pause/Resume | PASS | 0 messages during 71s pause |
| T4: Campaign status | PASS | Transitions accurate |
| T5: Message status | PASS | Individual tracking works |
| T6: Webhooks | DEFERRED | Phase 3 prerequisite |
| T7: Error handling | NOT TESTED | Low priority |
| T8a: Timestamp scheduling | PASS | +2.9s variance |
| T8b: Multiple campaigns | PASS | 3/3 concurrent |
| T8c: Cancellation | PASS | Immediate deletion |
| T8d: Advanced campaign | PASS | `/sender/advanced` works |
| T9: PIX payments | PASS | 2/2 endpoints |

**Conclusion**: Core campaign functionality fully validated. Ready for production.

---

## Cross-References

- **Full validation specs**: `docs/ZAPTOSWPP-VALIDATION-STRATEGY.md`
- **Test scripts**: `tests/validation/`
- **Session history**: `docs/SESSION-ARCHIVE.md`
