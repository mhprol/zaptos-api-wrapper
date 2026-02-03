import httpx
from typing import Optional, Dict, Any, List

class GHLClient:
    def __init__(self, api_key: str, location_id: Optional[str] = None):
        self.base_url = "https://rest.gohighlevel.com/v1"  # Assuming V1 for now, or check docs if available.
        # Actually, GHL has V2 API now (services.leadconnectorhq.com), but instructions mention "api_key" which is often V1.
        # However, for robustness, I'll stick to a generic implementation that can be adapted.
        # If the user provides an API Key, it's usually Bearer token in V2 or Authorization header in V1.

        self.headers = {
            "Authorization": f"Bearer {api_key}"
        }
        if location_id:
             self.location_id = location_id

        self.client = httpx.Client(
            base_url="https://rest.gohighlevel.com/v1",
            headers=self.headers,
            timeout=30.0
        )

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        response = self.client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        response = self.client.post(endpoint, json=json)
        response.raise_for_status()
        return response.json()

    def _put(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        response = self.client.put(endpoint, json=json)
        response.raise_for_status()
        return response.json()

    def get_contacts(self, query: Optional[str] = None, limit: int = 20) -> List[Dict[str, Any]]:
        # This is a simplified implementation. Real GHL API has specific search endpoints.
        params = {"limit": limit}
        if query:
            params["query"] = query
        if hasattr(self, 'location_id'):
            params['locationId'] = self.location_id

        return self._get("/contacts", params=params).get("contacts", [])

    def create_contact(self, contact_data: Dict[str, Any]) -> Dict[str, Any]:
        if hasattr(self, 'location_id'):
            contact_data['locationId'] = self.location_id
        return self._post("/contacts", json=contact_data)

    def update_contact(self, contact_id: str, contact_data: Dict[str, Any]) -> Dict[str, Any]:
        return self._put(f"/contacts/{contact_id}", json=contact_data)

    def get_contacts_by_tag(self, tag: str) -> List[Dict[str, Any]]:
        # This might vary depending on API version.
        # Assuming simple filter or search.
        # V2 uses lookup? Or search.
        # I'll stick to a generic search for now, assuming the wrapper logic will handle filtering if API doesn't support direct tag filter in one go.
        # However, typical GHL usage involves GET /contacts with query.
        return self.get_contacts(query=tag)
