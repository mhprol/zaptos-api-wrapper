import pytest
from zaptos.config import Config

def test_validate_zaptos():
    # Test valid
    cfg = Config(zaptos_instance="inst", zaptos_token="tok")
    cfg.validate_zaptos() # Should not raise

    # Test invalid instance
    cfg = Config(zaptos_instance="", zaptos_token="tok")
    with pytest.raises(ValueError, match="ZAPTOS_INSTANCE and ZAPTOS_TOKEN must be set"):
        cfg.validate_zaptos()

    # Test invalid token
    cfg = Config(zaptos_instance="inst", zaptos_token="")
    with pytest.raises(ValueError, match="ZAPTOS_INSTANCE and ZAPTOS_TOKEN must be set"):
        cfg.validate_zaptos()

def test_validate_ghl():
    # Test valid
    cfg = Config(ghl_api_key="key")
    cfg.validate_ghl() # Should not raise

    # Test invalid
    cfg = Config(ghl_api_key="")
    with pytest.raises(ValueError, match="GHL_API_KEY must be set"):
        cfg.validate_ghl()

def test_env_defaults():
    with pytest.MonkeyPatch.context() as m:
        m.setenv("ZAPTOS_INSTANCE", "env_inst")
        m.setenv("ZAPTOS_TOKEN", "env_tok")
        cfg = Config()
        assert cfg.zaptos_instance == "env_inst"
        assert cfg.zaptos_token == "env_tok"
