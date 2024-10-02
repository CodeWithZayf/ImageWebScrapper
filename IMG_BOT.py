import requests
import streamlit as st
from PIL import Image
from io import BytesIO

def img_bot():
    import requests
import streamlit as st

def img_bot():
    st.markdown("<h1 style='text-align: center;'>🖼️ SEARCH IT</h1>", unsafe_allow_html=True)
    with st.form("Search"):
        keyword = st.text_input("Enter a Keyword")
        search = st.form_submit_button("Search")
    if search:
        access_key = "Replace with your API Token from Unsplash"  # Replace with your Unsplash API access key
        url = f"https://api.unsplash.com/search/photos?query={keyword}&client_id={access_key}&per_page=6"
        response = requests.get(url)
        if response.status_code == 200:
            images = response.json()["results"]
            for i, img in enumerate(images):
                img_url = img["urls"]["small"]
                st.image(img_url, caption=f"Image {i+1}: {img['alt_description'] or 'No Description'}", use_column_width=True)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

img_bot()