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
background-size: 140%;
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
st.title("Conclusiones")
st.markdown ("## **¿Se validó o no los resultados?**")
st.markdown ("Se logró validar los resultados ya que en la correlación de pandas y en el código que utilizamos para la correlación, a la hora de evaluar el máximo valor tenemos como resultado a los mismos usuarios.*")
st.markdown ("## **Los resultados Validados son:**")
st.markdown ("lapazav@unsa.edu.pe y xpinto@unsa.edu.pe con un índice de similitud de 0.7249*")
st.markdown ("rtelloa@unsa.edu.pe y soysebastian14@gmail.com con un índice de similitud de 0.5402*")
st.markdown ("## **¿Es efectivo el método de correlación de pearson?**")
st.markdown ("Nuestro objetivo era la de validar los datos a través de dos procesos, es por ello que podemos concluir que si resulta efectivo usar la correlación de pearson. Una de sus principales ventajas es que el valor es independiente de cualquier unidad que se utiliza para medir las variables, por lo que, si la muestra es grande es más probable la exactitud de la estimación.*")
st.markdown ("## **Correlación de Pearson y Regresión Lineal, ¿cuál es su relación?**")
st.markdown ("Dentro de la teoría establecemos que una relación causal entre dos eventos existe si la ocurrencia del primero cause el otro. El primer evento es llamado causa y el segundo evento es llamado efecto. Una correlación entre dos variables no implica causalidad. Por otro lado, si hay una relación causal entre dos variables estas deben estar corrrelacionadas.*")
