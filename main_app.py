import streamlit as st
from PIL import Image

st.title('test')
st.caption('This is Test Application')

image = Image.open('.\datas\A.png')
st.image(image, width=200)
