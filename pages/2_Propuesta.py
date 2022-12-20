import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import webbrowser
import base64
import plotly.express as px

st.set_page_config(
    page_title="Propuesta",
)

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
background-size: 190%;
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
st.markdown("# 1. Encuesta Google Forms")
st.markdown("Primero se realizo una encuesta mediante el formulario de Google de lo cual obtuvimos los datos necesarios a partir de un archivo .CSV, con lo cual se realizó el debido preprocesamiento de los datos para generar la matriz de correlacion con pandas")

c1,c2 = st.columns([6,4])

c1.markdown("### Encuesta:")
c1.markdown("#####  ")
c1.markdown("  ")
url1 = 'https://forms.gle/nvfZxwp9e4QWEZvc9'
c1.markdown(f'''
<a href={url1}><button style="background-color:#1D1919;"><p style="color:white;">Ver Encuesta</p></button></a>
''',
unsafe_allow_html=True)

img1 = Image.open('imagenes/1.png')
c1.image(img1, width=380)


st.markdown("# 2. Lectura del archivo CSV e imputación de los NaN")
st.markdown("A continuación se pasara a leer el archivo de las respuestas de los encuestados mediante pandas. Y luego se imputara los NAN con la media usando el metodo fillna.median()")
## LEER ARCHIVO CSV
d1,d2 = st.columns(2)
data = pd.read_csv('Películas.csv')

if d1.button('Generar lectura del Csv'):
    data
## Imputando los NAN
data = data.fillna(data.median(numeric_only=True))
if d2.button('Generar Csv con imputacion de los "NAN"'):
    data
