import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import webbrowser
import base64
import plotly.express as px

st.set_page_config(
    page_title="Matriz Correlacion",
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
st.title("3. Matriz de correlación(PANDAS)")
st.markdown("Para generar la matriz de correlación en Pandas, se convirtio a un dataframe nuestros datos y se utilizo el metodo .corr(), para generar nuestra matriz en Pandas:")
data = pd.read_csv('Películas.csv')
data = data.fillna(data.median(numeric_only=True))

valores = data[data.columns[1:]].to_numpy()
usuarios = data[data.columns[0]].to_numpy()
valt = valores.T
df = pd.DataFrame(valt, columns = usuarios)
m_corr_pandas = df.corr()
m_corr_d_pandas = np.round(m_corr_pandas, decimals = 4)
m_corr_d_pandas

st.title("4. Gráfica de calor")
import seaborn as sns
sns.heatmap(m_corr_pandas, cmap="GnBu")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot ()

st.title("5. Resultados")
st.markdown("A partir de la matriz en Pandas hallamos los 2 ususarios mas similes como se muestra a continuacion:")
maxim = m_corr_d_pandas.unstack()
st.write(maxim.sort_values(ascending=False)[range(len(valores),((len(valores)+4)))])

st.markdown("Los resultados de similitud obtenidos en **Películas** según la tabla de **Correlación** son los siguientes encuestados:")

st.markdown(" 1. _lapazav@unsa.edu.pe y xpinto@unsa.edu.pe obtienen el PRIMER indice mas alto de similitud con 0.7249")

st.markdown(" 2. _rtelloa@unsa.edu.pe y soysebastian14@gmail.com obtienen el SEGUNDO indice mas alto de similitud con 0.5402")
