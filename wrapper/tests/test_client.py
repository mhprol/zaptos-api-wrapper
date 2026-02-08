import pytest
import respx
import httpx
import json
from zaptos.client import ZaptosClient

@pytest.fixture
def client():
    return ZaptosClient(instance="test_instance", token="test_token")

@respx.mock
def test_send_text(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-text").mock(
        return_value=httpx.Response(200, json={"status": "success", "messageId": "123"})
    )

    response = client.send_text(number="1234567890", text="Hello")

    assert response["status"] == "success"
    assert response["messageId"] == "123"

    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "text": "Hello"
    }
    assert respx.calls.last.request.headers["token"] == "test_token"

@respx.mock
def test_send_image(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-image").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    # Test without caption
    client.send_image(number="1234567890", url="http://example.com/image.png")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "url": "http://example.com/image.png"
    }

    # Test with caption
    client.send_image(number="1234567890", url="http://example.com/image.png", caption="Nice pic")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "url": "http://example.com/image.png",
        "caption": "Nice pic"
    }

@respx.mock
def test_send_buttons(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-buttons").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    buttons = [{"id": "btn1", "text": "Yes"}, {"id": "btn2", "text": "No"}]

    # Test without description
    client.send_buttons(number="1234567890", title="Are you sure?", buttons=buttons)
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "title": "Are you sure?",
        "buttons": buttons
    }

    # Test with description
    client.send_buttons(number="1234567890", title="Confirmation", buttons=buttons, description="Please confirm")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "title": "Confirmation",
        "buttons": buttons,
        "description": "Please confirm"
    }

@respx.mock
def test_send_list(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-list").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    sections = [
        {"title": "Section 1", "rows": [{"id": "row1", "title": "Option 1"}]}
    ]

    # Test without description
    client.send_list(number="1234567890", title="Menu", sections=sections, button_text="Show options")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "title": "Menu",
        "sections": sections,
        "buttonText": "Show options"
    }

    # Test with description
    client.send_list(number="1234567890", title="Menu", sections=sections, button_text="Show", description="Select one")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "title": "Menu",
        "sections": sections,
        "buttonText": "Show",
        "description": "Select one"
    }

@respx.mock
def test_send_carousel(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-carousel").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    cards = [{"title": "Card 1", "body": "Body 1"}]

    client.send_carousel(number="1234567890", cards=cards)
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "cards": cards
    }

@respx.mock
def test_send_location(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-location").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    # Test minimal
    client.send_location(number="1234567890", latitude="40.7128", longitude="-74.0060")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "latitude": "40.7128",
        "longitude": "-74.0060"
    }

    # Test with address and name
    client.send_location(number="1234567890", latitude="40.7128", longitude="-74.0060", address="New York", name="NY")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "latitude": "40.7128",
        "longitude": "-74.0060",
        "address": "New York",
        "name": "NY"
    }

@respx.mock
def test_send_contact(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-contact").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    client.send_contact(number="1234567890", contact_name="John Doe", contact_number="9876543210")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "name": "John Doe",
        "contactNumber": "9876543210"
    }

@respx.mock
def test_send_document(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-document").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    # Test minimal
    client.send_document(number="1234567890", url="http://example.com/doc.pdf")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "url": "http://example.com/doc.pdf"
    }

    # Test with filename and caption
    client.send_document(number="1234567890", url="http://example.com/doc.pdf", filename="doc.pdf", caption="Here is the doc")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "url": "http://example.com/doc.pdf",
        "filename": "doc.pdf",
        "caption": "Here is the doc"
    }

@respx.mock
def test_send_audio(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-audio").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    client.send_audio(number="1234567890", url="http://example.com/audio.mp3")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "url": "http://example.com/audio.mp3"
    }

@respx.mock
def test_send_video(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-video").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    # Test minimal
    client.send_video(number="1234567890", url="http://example.com/video.mp4")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "url": "http://example.com/video.mp4"
    }

    # Test with caption
    client.send_video(number="1234567890", url="http://example.com/video.mp4", caption="Watch this")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "url": "http://example.com/video.mp4",
        "caption": "Watch this"
    }

@respx.mock
def test_send_sticker(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-sticker").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )

    client.send_sticker(number="1234567890", url="http://example.com/sticker.webp")
    assert json.loads(respx.calls.last.request.content) == {
        "number": "1234567890",
        "url": "http://example.com/sticker.webp"
    }

@respx.mock
def test_error_401(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-text").mock(
        return_value=httpx.Response(401, json={"error": "Unauthorized"})
    )
    with pytest.raises(httpx.HTTPStatusError) as excinfo:
        client.send_text(number="123", text="Fail")
    assert excinfo.value.response.status_code == 401

@respx.mock
def test_error_403(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-text").mock(
        return_value=httpx.Response(403, json={"error": "Forbidden"})
    )
    with pytest.raises(httpx.HTTPStatusError) as excinfo:
        client.send_text(number="123", text="Fail")
    assert excinfo.value.response.status_code == 403

@respx.mock
def test_error_429(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-text").mock(
        return_value=httpx.Response(429, json={"error": "Too Many Requests"})
    )
    with pytest.raises(httpx.HTTPStatusError) as excinfo:
        client.send_text(number="123", text="Fail")
    assert excinfo.value.response.status_code == 429

@respx.mock
def test_error_500(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-text").mock(
        return_value=httpx.Response(500, json={"error": "Internal Server Error"})
    )
    with pytest.raises(httpx.HTTPStatusError) as excinfo:
        client.send_text(number="123", text="Fail")
    assert excinfo.value.response.status_code == 500

@respx.mock
def test_malformed_response(client):
    # Response is not valid JSON
    respx.post("https://api.zaptoswpp.com/test_instance/send-text").mock(
        return_value=httpx.Response(200, text="Not JSON")
    )
    with pytest.raises(json.JSONDecodeError):
        client.send_text(number="123", text="Fail")

@respx.mock
def test_timeout(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-text").mock(
        side_effect=httpx.ConnectTimeout("Timeout", request=None)
    )
    with pytest.raises(httpx.ConnectTimeout):
        client.send_text(number="123", text="Fail")

@respx.mock
def test_generic_methods(client):
    # Test _get
    respx.get("https://api.zaptoswpp.com/test_instance/some-endpoint").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    assert client._get("/some-endpoint") == {"ok": True}

    # Test _delete
    respx.delete("https://api.zaptoswpp.com/test_instance/some-endpoint").mock(
        return_value=httpx.Response(200, json={"deleted": True})
    )
    assert client._delete("/some-endpoint") == {"deleted": True}
