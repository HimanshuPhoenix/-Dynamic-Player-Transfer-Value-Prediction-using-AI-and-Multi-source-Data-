import streamlit as st
from streamlit_autorefresh import st_autorefresh
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

# Thread pool for background image fetch
executor = ThreadPoolExecutor(max_workers=2)

# Default placeholder image
DEFAULT_PLAYER_IMG = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png"

# Session state setup
if "image_futures" not in st.session_state:
    st.session_state.image_futures = {}

st.title("⚽ Transfermarkt Player Image Loader (Async)")

# --- Input box ---
player_id = st.text_input("Enter Transfermarkt Player ID:", "108390")

# --- Helper functions ---
def _fetch_image_for_id(player_id):
    """Scrape Transfermarkt for the player's profile image bytes."""
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        profile_url = f"https://www.transfermarkt.com/-/profil/spieler/{player_id}"
        r = requests.get(profile_url, headers=headers, timeout=6)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        img_tag = soup.find("img", class_="data-header__profile-image")
        if img_tag and img_tag.get("src"):
            img_url = img_tag["src"]
            r2 = requests.get(img_url, stream=True, timeout=6)
            r2.raise_for_status()
            return r2.content
    except requests.RequestException:
        return None
    return None

def request_image_load(player_id):
    """Start async image fetch if not already running."""
    key = str(player_id)
    if key not in st.session_state.image_futures:
        future = executor.submit(_fetch_image_for_id, player_id)
        st.session_state.image_futures[key] = future
    return st.session_state.image_futures[key]

# --- UI display ---
if player_id:
    placeholder = st.empty()
    key = str(player_id)

    # Start background load
    future = request_image_load(player_id)

    # Check if ready
    if not future.done():
        placeholder.info("Fetching player image from Transfermarkt...")
        placeholder.image(DEFAULT_PLAYER_IMG, width=160, caption="Loading...")
        # Auto-refresh every second
        st_autorefresh(interval=1000, limit=30, key=f"img_refresh_{key}")
    else:
        img_bytes = future.result()
        if img_bytes:
            placeholder.image(img_bytes, width=160, caption=f"Player {player_id}")
        else:
            placeholder.image(DEFAULT_PLAYER_IMG, width=160, caption="No image available")
else:
    st.warning("Please enter a player ID.")
