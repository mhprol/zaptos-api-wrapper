import pytest
from unittest.mock import MagicMock
from click.testing import CliRunner
from zaptos.client import ZaptosClient
from zaptos.ghl import GHLClient
from zaptos.config import config as zaptos_config
import os

@pytest.fixture
def mock_client():
    """Returns a MagicMock of ZaptosClient for CLI tests."""
    client = MagicMock(spec=ZaptosClient)
    # Default behavior for common methods
    client.send_text.return_value = {"status": "success", "messageId": "mock_id"}
    client._get.return_value = {}
    client._post.return_value = {"status": "success"}
    client._put.return_value = {"status": "success"}
    client._delete.return_value = {"status": "success"}
    return client

@pytest.fixture
def mock_ghl_client():
    """Returns a MagicMock of GHLClient for CLI tests."""
    client = MagicMock(spec=GHLClient)
    client.get_contacts.return_value = []
    client.get_contacts_by_tag.return_value = []
    client.create_contact.return_value = {"status": "success"}
    return client

@pytest.fixture
def runner():
    """Returns a CliRunner instance."""
    return CliRunner()

@pytest.fixture(autouse=True)
def mock_config():
    """
    Fixture to mock the zaptos.config object.
    It saves the original values and restores them after the test.
    It sets default test values.
    """
    # Save original values
    original_instance = zaptos_config.zaptos_instance
    original_token = zaptos_config.zaptos_token
    original_ghl_key = zaptos_config.ghl_api_key
    original_ghl_location = zaptos_config.ghl_location_id
    original_output = zaptos_config.output

    # Set defaults for testing
    zaptos_config.zaptos_instance = "test_instance"
    zaptos_config.zaptos_token = "test_token"
    zaptos_config.ghl_api_key = "test_ghl_key"
    zaptos_config.ghl_location_id = "test_ghl_loc"
    zaptos_config.output = "json"

    yield

    # Restore
    zaptos_config.zaptos_instance = original_instance
    zaptos_config.zaptos_token = original_token
    zaptos_config.ghl_api_key = original_ghl_key
    zaptos_config.ghl_location_id = original_ghl_location
    zaptos_config.output = original_output

@pytest.fixture
def real_client():
    """Returns a real ZaptosClient instance for testing with respx."""
    return ZaptosClient(instance="test_instance", token="test_token")
