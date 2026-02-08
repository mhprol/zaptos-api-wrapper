import pytest
from unittest.mock import patch, MagicMock, mock_open
from zaptos.endpoints.campaigns import campaigns as campaigns_group
import json

@pytest.fixture
def mock_campaigns_data():
    return {
        "camp1": {
            "id": "camp1",
            "name": "Test Camp",
            "status": "created",
            "template": "Hello {{name}}",
            "source": "csv",
            "source_config": "contacts.csv",
            "stats": {"total": 0, "sent": 0, "failed": 0}
        }
    }

def test_campaign_create(runner, mock_config):
    with patch('zaptos.endpoints.campaigns.load_campaigns', return_value={}), \
         patch('zaptos.endpoints.campaigns.save_campaigns') as mock_save:

        result = runner.invoke(campaigns_group, [
            'create',
            '--name', 'New Camp',
            '--ghl-tag', 'mytag',
            '--template', 'Hi'
        ])

        assert result.exit_code == 0
        assert "created" in result.output

        # Verify save called
        mock_save.assert_called_once()
        saved_data = mock_save.call_args[0][0]
        assert len(saved_data) == 1
        cid = list(saved_data.keys())[0]
        assert saved_data[cid]['name'] == 'New Camp'
        assert saved_data[cid]['source'] == 'ghl'

def test_campaign_list(runner, mock_campaigns_data):
    with patch('zaptos.endpoints.campaigns.load_campaigns', return_value=mock_campaigns_data):
        result = runner.invoke(campaigns_group, ['list'])
        assert result.exit_code == 0
        assert "Test Camp" in result.output

def test_campaign_start_csv(runner, mock_campaigns_data, mock_client):
    # Mock CSV reading
    csv_content = "number,name\n123,Alice\n456,Bob"

    with patch('zaptos.endpoints.campaigns.load_campaigns', return_value=mock_campaigns_data), \
         patch('zaptos.endpoints.campaigns.save_campaigns') as mock_save, \
         patch('builtins.open', mock_open(read_data=csv_content)), \
         patch('zaptos.endpoints.campaigns.time.sleep'): # skip sleep

        ctx_obj = MagicMock()
        ctx_obj.client = mock_client
        # No ghl_client needed for CSV

        result = runner.invoke(campaigns_group, ['start', 'camp1'], obj=ctx_obj)

        assert result.exit_code == 0
        assert "completed" in result.output

        # Verify messages sent
        assert mock_client.send_text.call_count == 2
        mock_client.send_text.assert_any_call("123", "Hello Alice")
        mock_client.send_text.assert_any_call("456", "Hello Bob")

        # Verify status update
        final_save_args = mock_save.call_args[0][0]
        assert final_save_args['camp1']['status'] == 'completed'
        assert final_save_args['camp1']['stats']['sent'] == 2

def test_campaign_start_ghl(runner, mock_client, mock_ghl_client):
    data = {
        "camp2": {
            "id": "camp2",
            "name": "GHL Camp",
            "status": "created",
            "template": "Hey {{name}}",
            "source": "ghl",
            "source_config": "sometag",
            "stats": {}
        }
    }

    # Mock GHL contacts
    mock_ghl_client.get_contacts_by_tag.return_value = [
        {"phone": "789", "firstName": "Charlie"}
    ]

    with patch('zaptos.endpoints.campaigns.load_campaigns', return_value=data), \
         patch('zaptos.endpoints.campaigns.save_campaigns') as mock_save, \
         patch('zaptos.endpoints.campaigns.time.sleep'):

        ctx_obj = MagicMock()
        ctx_obj.client = mock_client
        ctx_obj.ghl_client = mock_ghl_client

        result = runner.invoke(campaigns_group, ['start', 'camp2'], obj=ctx_obj)

        assert result.exit_code == 0

        # Verify GHL fetch
        mock_ghl_client.get_contacts_by_tag.assert_called_with("sometag")

        # Verify send
        mock_client.send_text.assert_called_with("789", "Hey Charlie")

def test_campaign_pause(runner, mock_campaigns_data):
    with patch('zaptos.endpoints.campaigns.load_campaigns', return_value=mock_campaigns_data), \
         patch('zaptos.endpoints.campaigns.save_campaigns') as mock_save:

        result = runner.invoke(campaigns_group, ['pause', 'camp1'])
        assert result.exit_code == 0

        saved_data = mock_save.call_args[0][0]
        assert saved_data['camp1']['status'] == 'paused'

def test_campaign_delete(runner, mock_campaigns_data):
    with patch('zaptos.endpoints.campaigns.load_campaigns', return_value=mock_campaigns_data), \
         patch('zaptos.endpoints.campaigns.save_campaigns') as mock_save:

        result = runner.invoke(campaigns_group, ['delete', 'camp1'])
        assert result.exit_code == 0

        saved_data = mock_save.call_args[0][0]
        assert 'camp1' not in saved_data
