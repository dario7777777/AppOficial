import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import webbrowser
import math
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
background-size: 180%;
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
st.write("## Validacion de la matriz de correlacion")
st.write("Para validar la matriz de correlacion de pandas hemos hecho un codigo que permita generar el coeficiente de correlacion empleando la formula de correlación de Pearson")
st.write("A partir de ese coeficiente generamos el dataframe y la matriz de correlación.")



data = pd.read_csv('Películas.csv')
data = data.fillna(data.median(numeric_only=True))

valores2 = data[data.columns[1:]].to_numpy()
usuarios2 = data[data.columns[0]].to_numpy()

# Similitus y matriz de correlacion

simil = []

def correlacion(x,y):
    mx = x.mean()
    my = y.mean()
    cova = np.sum((x -mx)*(y-my))
    dist = np.sqrt(np.sum((x-mx)**2)*np.sum((y-my)**2))
    coef = cova/dist
    return coef

for i in range(len(usuarios2)):
    for j in range(len(usuarios2)):
        data2 = data.loc[[i,j],:]
        newv = data2[data2.columns[1:]].to_numpy()
        simil.append(correlacion(newv[0],newv[1]))

simil2 = np.array(simil).reshape(len(usuarios2),len(usuarios2))
matr = pd.DataFrame(simil2,usuarios2,usuarios2)
matr

# Resultados

st.write("## Resultados")
st.write("Para poder validar los resultados que obtuvimos con la matriz de correlación de Pandas, empleamos el mismo metodo pero con la matriz creada con nuestro codigo. Generando los 2 usuarios con mayor similitud como se muestra a continuación. ")
maxim = matr.unstack()
st.write(maxim.sort_values(ascending=False)[range(len(valores2),((len(valores2)+4)))])

st.write("#### Los resultados Validados son:")
st.markdown(" 1. _lapazav@unsa.edu.pe y xpinto@unsa.edu.pe obtienen el PRIMER indice mas alto de similitud con 0.7249")
st.markdown(" 2. _rtelloa@unsa.edu.pe y soysebastian14@gmail.com obtienen el SEGUNDO indice mas alto de similitud con 0.5402")

st.write("## Gráfica de calor")
import seaborn as sns
sns.heatmap(matr, cmap="spring")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot ()
