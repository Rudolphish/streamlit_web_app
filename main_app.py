import streamlit as st
from PIL import Image

st.title('test')
st.caption('This is Test Application')

image = Image.open('streamlit_web_app/datas/A.png')
st.image(image, width=200)
