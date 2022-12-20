import streamlit as st
from PIL import Image
import base64
import plotly.express as px


ds = px.data.iris()

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        dat = f.read()
    return base64.b64encode(dat).decode()


img = get_img_as_base64("imagenes/imagen.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs8ujv8r0jGFqrG2cYpKYhVyGtgrjhSuzW0MMePxfYqEdNb0k-U2gAXv7F-F9epEi6bZE&usqp=CAU");
background-size: 150%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-size: 130%;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

logo = Image.open('imagenes/logo.png')
with st.sidebar:
    st.image(logo)
st.title("REFERENCIAS")
st.markdown ("##### [1] https://profile.es/blog/pandas-python/")
st.markdown ("##### [2] https://aprendeconalf.es/docencia/python/manual/numpy/")
st.markdown ("##### [3] https://www.questionpro.com/blog/es/que-es-la-escala-de-likert-y-como-utilizarla/")
st.markdown ("##### [4] https://www.geeknetic.es/Archivo-CSV/que-es-y-para-que-sirve")
st.markdown ("##### [5] https://www.w3schools.com/python/")
st.markdown ("##### [6] https://www.edx.org/course/python-for-data-science-2")
st.markdown ("##### [7] https://ellibrodepython.com/diccionarios-en-python")
st.markdown ("##### [8] https://youtu.be/2lAfenU75bM")
st.markdown ("##### [9] https://youtu.be/ZZ4B0QUHuNc")
