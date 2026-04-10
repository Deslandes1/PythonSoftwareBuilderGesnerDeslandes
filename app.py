import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Photo App")
st.title("My Photo")

try:
    img = Image.open("my_photo.jpg")
    st.image(img, caption="This is my photo", width=400)
except FileNotFoundError:
    st.error("Photo not found. Make sure the file name matches.")
