import os
import yaml
from pathlib import Path
from pydantic import BaseModel, Field

PROFILES_FILE = Path.home() / '.config' / 'zaptos' / 'profiles.yaml'

def load_profiles():
    if not PROFILES_FILE.exists():
        return {'default': None, 'profiles': {}}
    try:
        with open(PROFILES_FILE) as f:
            return yaml.safe_load(f) or {'default': None, 'profiles': {}}
    except Exception:
        # If parsing fails, return empty
        return {'default': None, 'profiles': {}}

def get_profile(name: str = None):
    data = load_profiles()
    profile_name = name or data.get('default')
    if not profile_name:
        return {}
    return data.get('profiles', {}).get(profile_name, {})

class Config(BaseModel):
    zaptos_instance: str = Field(default_factory=lambda: os.getenv("ZAPTOS_INSTANCE", ""))
    zaptos_token: str = Field(default_factory=lambda: os.getenv("ZAPTOS_TOKEN", ""))
    ghl_api_key: str = Field(default_factory=lambda: os.getenv("GHL_API_KEY", ""))
    ghl_location_id: str = Field(default_factory=lambda: os.getenv("GHL_LOCATION_ID", ""))

    # Optional output format
    output: str = Field(default="json")

    @classmethod
    def load(cls, profile_name: str = None):
        profile_data = get_profile(profile_name)
        return cls(**profile_data)

    def validate_zaptos(self):
        if not self.zaptos_instance or not self.zaptos_token:
            raise ValueError("ZAPTOS_INSTANCE and ZAPTOS_TOKEN must be set or provided.")

    def validate_ghl(self):
        if not self.ghl_api_key:
            raise ValueError("GHL_API_KEY must be set or provided for GHL operations.")

config = Config()
