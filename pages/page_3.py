import streamlit as st
from PIL import Image

image = Image.open('streamlit_web_app/datas/A.png')
st.image(image, width=200)
