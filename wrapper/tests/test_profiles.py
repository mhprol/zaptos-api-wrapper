import pytest
from unittest.mock import patch, mock_open, MagicMock
import os
import yaml
from pathlib import Path
from zaptos.config import Config, load_profiles, get_profile, PROFILES_FILE

# Mock data for profiles.yaml
MOCK_PROFILES_YAML = """
default: prod
profiles:
  prod:
    zaptos_instance: prod-instance
    zaptos_token: prod-token
  dev:
    zaptos_instance: dev-instance
    zaptos_token: dev-token
    ghl_api_key: dev-ghl
"""

@pytest.fixture
def mock_profiles_file():
    with patch("builtins.open", mock_open(read_data=MOCK_PROFILES_YAML)) as m:
        yield m

@pytest.fixture
def mock_no_profiles_file():
    with patch("pathlib.Path.exists", return_value=False):
        yield

@pytest.fixture
def mock_profiles_path_exists():
    with patch("pathlib.Path.exists", return_value=True):
        yield

def test_load_profiles_exists(mock_profiles_path_exists, mock_profiles_file):
    profiles = load_profiles()
    assert profiles['default'] == 'prod'
    assert 'prod' in profiles['profiles']
    assert 'dev' in profiles['profiles']

def test_load_profiles_not_exists(mock_no_profiles_file):
    profiles = load_profiles()
    assert profiles == {'default': None, 'profiles': {}}

def test_get_profile_named(mock_profiles_path_exists, mock_profiles_file):
    profile = get_profile('dev')
    assert profile['zaptos_instance'] == 'dev-instance'
    assert profile['ghl_api_key'] == 'dev-ghl'

def test_get_profile_default(mock_profiles_path_exists, mock_profiles_file):
    profile = get_profile()
    assert profile['zaptos_instance'] == 'prod-instance'

def test_get_profile_none_no_default(mock_profiles_path_exists):
    # Mock yaml with no default
    yaml_data = "profiles:\n  test:\n    foo: bar"
    with patch("builtins.open", mock_open(read_data=yaml_data)):
        profile = get_profile()
        assert profile == {}

def test_config_load_from_profile(mock_profiles_path_exists, mock_profiles_file):
    # Ensure env vars don't interfere with this specific test if we want to test purity,
    # but here we test that profile is loaded.
    config = Config.load('dev')
    assert config.zaptos_instance == 'dev-instance'
    assert config.zaptos_token == 'dev-token'
    assert config.ghl_api_key == 'dev-ghl'

def test_config_load_default(mock_profiles_path_exists, mock_profiles_file):
    config = Config.load()
    assert config.zaptos_instance == 'prod-instance'

def test_config_precedence_profile_over_env(mock_profiles_path_exists, mock_profiles_file):
    # Set env var
    with patch.dict(os.environ, {"ZAPTOS_INSTANCE": "env-instance", "ZAPTOS_TOKEN": "env-token"}):
        # Profile has instance 'dev-instance'
        config = Config.load('dev')
        assert config.zaptos_instance == 'dev-instance'
        # Profile has token 'dev-token'
        assert config.zaptos_token == 'dev-token'

def test_config_fallback_to_env(mock_profiles_path_exists, mock_profiles_file):
    # 'dev' profile has ghl_api_key, but NOT ghl_location_id
    with patch.dict(os.environ, {"GHL_LOCATION_ID": "env-location"}):
        config = Config.load('dev')
        # Should take from profile
        assert config.ghl_api_key == 'dev-ghl'
        # Should take from env
        assert config.ghl_location_id == 'env-location'

def test_config_no_profile_uses_env():
    with patch("zaptos.config.load_profiles", return_value={'default': None, 'profiles': {}}):
        with patch.dict(os.environ, {"ZAPTOS_INSTANCE": "env-only", "ZAPTOS_TOKEN": "env-token"}):
             config = Config.load()
             assert config.zaptos_instance == "env-only"
