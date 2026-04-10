import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="My Photo App")
st.title("My Photo")

# Find the first image file in the current directory
image_files = [f for f in os.listdir(".") if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

if image_files:
    img = Image.open(image_files[0])
    st.image(img, caption=image_files[0], width=400)
else:
    st.error("No image file found. Please upload a .jpg or .png file to the repository.")
