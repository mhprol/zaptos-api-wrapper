import pytest
from unittest.mock import MagicMock
from zaptos.endpoints.contacts import contacts as contacts_group

def test_contacts_list(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = [{"number": "123", "name": "John"}]

    result = runner.invoke(contacts_group, ['list'], obj=ctx_obj)

    assert result.exit_code == 0
    assert "John" in result.output
    mock_client._get.assert_called_with("/contacts", params={"limit": 20})

def test_contacts_get(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = [{"number": "123", "name": "John"}]

    result = runner.invoke(contacts_group, ['get', '123'], obj=ctx_obj)

    assert result.exit_code == 0
    assert "John" in result.output
    # The implementation calls _get("/contacts", params={"number": "123"})
    mock_client._get.assert_called_with("/contacts", params={"number": "123"})

def test_contacts_create(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {"id": "c1", "status": "created"}

    result = runner.invoke(contacts_group, ['create', '--number', '123', '--name', 'John'], obj=ctx_obj)

    assert result.exit_code == 0
    assert "created" in result.output
    mock_client._post.assert_called_with("/contacts", json={"number": "123", "name": "John"})

def test_contacts_sync_ghl(runner, mock_client, mock_ghl_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    ctx_obj.ghl_client = mock_ghl_client

    mock_ghl_client.get_contacts.return_value = [
        {"phone": "123", "name": "GHL John"}
    ]
    mock_client._post.return_value = {"status": "created"}

    result = runner.invoke(contacts_group, ['sync-ghl'], obj=ctx_obj)

    assert result.exit_code == 0
    assert "Synced 1 contacts" in result.output

    mock_ghl_client.get_contacts.assert_called()
    mock_client._post.assert_called_with("/contacts", json={"number": "123", "name": "GHL John"})

def test_contacts_push_ghl(runner, mock_client, mock_ghl_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    ctx_obj.ghl_client = mock_ghl_client

    # Mock getting contact from Zaptos
    mock_client._get.return_value = [{"number": "123", "name": "Zap John"}]

    # Mock creating in GHL
    mock_ghl_client.create_contact.return_value = {"status": "success"}

    result = runner.invoke(contacts_group, ['push-ghl', '123'], obj=ctx_obj)

    assert result.exit_code == 0

    mock_client._get.assert_called_with("/contacts", params={"number": "123"})
    mock_ghl_client.create_contact.assert_called_with({"name": "Zap John", "phone": "123"})
