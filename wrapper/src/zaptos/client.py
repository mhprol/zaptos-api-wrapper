import httpx
from typing import Optional, Dict, Any, Union

class ZaptosClient:
    def __init__(self, instance: str, token: str):
        self.base_url = f"https://api.zaptoswpp.com/{instance}"
        self.headers = {"token": token}
        self.client = httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            timeout=30.0
        )

    def _post(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        response = self.client.post(endpoint, json=json)
        response.raise_for_status()
        return response.json()

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        response = self.client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def _delete(self, endpoint: str) -> Dict[str, Any]:
        response = self.client.delete(endpoint)
        response.raise_for_status()
        return response.json()

    def send_text(self, number: str, text: str) -> Dict[str, Any]:
        return self._post("/send-text", json={
            "number": number,
            "text": text
        })

    def send_image(self, number: str, url: str, caption: Optional[str] = None) -> Dict[str, Any]:
        data = {
            "number": number,
            "url": url
        }
        if caption:
            data["caption"] = caption
        return self._post("/send-image", json=data)

    def send_buttons(self, number: str, title: str, buttons: list, description: Optional[str] = None) -> Dict[str, Any]:
        data = {
            "number": number,
            "title": title,
            "buttons": buttons
        }
        if description:
            data["description"] = description
        return self._post("/send-buttons", json=data)

    def send_list(self, number: str, title: str, sections: list, button_text: str, description: Optional[str] = None) -> Dict[str, Any]:
        data = {
            "number": number,
            "title": title,
            "sections": sections,
            "buttonText": button_text
        }
        if description:
            data["description"] = description
        return self._post("/send-list", json=data)

    def send_carousel(self, number: str, cards: list) -> Dict[str, Any]:
        return self._post("/send-carousel", json={
            "number": number,
            "cards": cards
        })

    def send_location(self, number: str, latitude: str, longitude: str, address: Optional[str] = None, name: Optional[str] = None) -> Dict[str, Any]:
        data = {
            "number": number,
            "latitude": latitude,
            "longitude": longitude
        }
        if address:
            data["address"] = address
        if name:
            data["name"] = name
        return self._post("/send-location", json=data)

    def send_contact(self, number: str, contact_name: str, contact_number: str) -> Dict[str, Any]:
        return self._post("/send-contact", json={
            "number": number,
            "name": contact_name,
            "contactNumber": contact_number
        })

    def send_document(self, number: str, url: str, filename: Optional[str] = None, caption: Optional[str] = None) -> Dict[str, Any]:
        data = {
            "number": number,
            "url": url
        }
        if filename:
            data["filename"] = filename
        if caption:
            data["caption"] = caption
        return self._post("/send-document", json=data)

    def send_audio(self, number: str, url: str) -> Dict[str, Any]:
        return self._post("/send-audio", json={
            "number": number,
            "url": url
        })

    def send_video(self, number: str, url: str, caption: Optional[str] = None) -> Dict[str, Any]:
        data = {
            "number": number,
            "url": url
        }
        if caption:
            data["caption"] = caption
        return self._post("/send-video", json=data)

    def send_sticker(self, number: str, url: str) -> Dict[str, Any]:
        return self._post("/send-sticker", json={
            "number": number,
            "url": url
        })

    # Other endpoints will be added later or accessed via _get/_post
