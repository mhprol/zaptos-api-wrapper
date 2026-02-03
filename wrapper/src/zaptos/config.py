import os
from pydantic import BaseModel, Field

class Config(BaseModel):
    zaptos_instance: str = Field(default_factory=lambda: os.getenv("ZAPTOS_INSTANCE", ""))
    zaptos_token: str = Field(default_factory=lambda: os.getenv("ZAPTOS_TOKEN", ""))
    ghl_api_key: str = Field(default_factory=lambda: os.getenv("GHL_API_KEY", ""))
    ghl_location_id: str = Field(default_factory=lambda: os.getenv("GHL_LOCATION_ID", ""))

    # Optional output format
    output: str = Field(default="json")

    def validate_zaptos(self):
        if not self.zaptos_instance or not self.zaptos_token:
            raise ValueError("ZAPTOS_INSTANCE and ZAPTOS_TOKEN must be set or provided.")

    def validate_ghl(self):
        if not self.ghl_api_key:
            raise ValueError("GHL_API_KEY must be set or provided for GHL operations.")

config = Config()
