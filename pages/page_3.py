import streamlit as st
from PIL import Image

image = Image.open('datas/A.png')
st.image(image, width=200)
