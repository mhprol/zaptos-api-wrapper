import pytest
import respx
import httpx
import json
from zaptos.ghl import GHLClient

@pytest.fixture
def ghl_client():
    return GHLClient(api_key="test_key", location_id="test_loc")

@respx.mock
def test_get_contacts(ghl_client):
    respx.get("https://rest.gohighlevel.com/v1/contacts").mock(
        return_value=httpx.Response(200, json={"contacts": [{"id": "c1", "name": "John"}]})
    )

    contacts = ghl_client.get_contacts()
    assert len(contacts) == 1
    assert contacts[0]["name"] == "John"

    # Check params
    req = respx.calls.last.request
    assert req.headers["Authorization"] == "Bearer test_key"
    # httpx handles params encoding, check if present
    params = dict(req.url.params)
    assert params["locationId"] == "test_loc"
    assert params["limit"] == "20"

@respx.mock
def test_get_contacts_with_query(ghl_client):
    respx.get("https://rest.gohighlevel.com/v1/contacts").mock(
        return_value=httpx.Response(200, json={"contacts": []})
    )

    ghl_client.get_contacts(query="John")
    req = respx.calls.last.request
    params = dict(req.url.params)
    assert params["query"] == "John"

@respx.mock
def test_create_contact(ghl_client):
    respx.post("https://rest.gohighlevel.com/v1/contacts").mock(
        return_value=httpx.Response(200, json={"contact": {"id": "new_id"}})
    )

    data = {"phone": "123", "name": "New"}
    resp = ghl_client.create_contact(data)
    assert resp["contact"]["id"] == "new_id"

    req = respx.calls.last.request
    assert req.headers["Authorization"] == "Bearer test_key"
    body = json.loads(req.content)
    assert body["locationId"] == "test_loc"
    assert body["phone"] == "123"

@respx.mock
def test_update_contact(ghl_client):
    respx.put("https://rest.gohighlevel.com/v1/contacts/c1").mock(
        return_value=httpx.Response(200, json={"contact": {"id": "c1", "updated": True}})
    )

    resp = ghl_client.update_contact("c1", {"name": "Updated"})
    assert resp["contact"]["updated"] is True

@respx.mock
def test_get_contacts_by_tag(ghl_client):
    respx.get("https://rest.gohighlevel.com/v1/contacts").mock(
        return_value=httpx.Response(200, json={"contacts": []})
    )

    ghl_client.get_contacts_by_tag("my_tag")
    req = respx.calls.last.request
    params = dict(req.url.params)
    assert params["query"] == "my_tag"

@respx.mock
def test_error_handling(ghl_client):
    respx.get("https://rest.gohighlevel.com/v1/contacts").mock(
        return_value=httpx.Response(401, json={"error": "Unauthorized"})
    )

    with pytest.raises(httpx.HTTPStatusError):
        ghl_client.get_contacts()
