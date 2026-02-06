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
def test_error_handling(client):
    respx.post("https://api.zaptoswpp.com/test_instance/send-text").mock(
        return_value=httpx.Response(500, json={"error": "Internal Server Error"})
    )

    with pytest.raises(httpx.HTTPStatusError):
        client.send_text(number="1234567890", text="Fail")
