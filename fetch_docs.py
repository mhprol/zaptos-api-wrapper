import requests
import os

BASE_URL = "https://www.radix-ui.com/primitives/docs"
BASE_DIR = "radix-ui-primitives/references"

components = [
    "accordion", "alert-dialog", "aspect-ratio", "avatar", "checkbox",
    "collapsible", "context-menu", "dialog", "dropdown-menu", "form",
    "hover-card", "label", "menubar", "navigation-menu", "popover",
    "progress", "radio-group", "scroll-area", "select", "separator",
    "slider", "switch", "tabs", "toast", "toggle", "toggle-group",
    "toolbar", "tooltip"
]

overviews = [
    "introduction", "getting-started", "accessibility", "releases"
]

guides = [
    "styling", "animation", "composition", "server-side-rendering"
]

def fetch_and_save(category, items):
    for item in items:
        url = f"{BASE_URL}/{category}/{item}.md"
        response = requests.get(url)

        if response.status_code == 200:
            filepath = os.path.join(BASE_DIR, category, f"{item}.md")
            with open(filepath, 'w') as f:
                f.write(response.text)
            print(f"Successfully fetched {category}/{item}")
        else:
            print(f"Failed to fetch {category}/{item}: HTTP {response.status_code}")

print("Fetching Overviews...")
fetch_and_save("overview", overviews)

print("\nFetching Guides...")
fetch_and_save("guides", guides)

print("\nFetching Components...")
fetch_and_save("components", components)

print("\nDone!")
