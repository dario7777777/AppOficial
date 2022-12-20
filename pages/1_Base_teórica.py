import streamlit as st
from PIL import Image
import base64
import plotly.express as px

st.set_page_config(
    page_title="Marco Teórico",
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
background-image: url("https://wallpapercave.com/wp/wp6310497.jpg");
background-size: 300%;
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
st.title("Sistema Recomendador")

st.markdown("Los sistemas de recomendación son herramientas importantes que ayudan a los usuarios a conocer opciones o elementos de interés para personalizar la experiencia del usuario. Tenemos contacto con estos poderosos sistemas de recomendación a diario.")
st.markdown("Cuando disfrutamos de un video en Youtube o dejamos que Spotify haga una mezcla de artistas para una playlist estamos aportando elementos de personalización para que estos sistemas construyan sus recomendaciones. El funcionamiento de los sistemas de recomendación ha evolucionado gracias al Machine Learning. Anteriormente los motores de búsqueda, plataformas de contenido y ventas de producto funcionaban con rankings o listas de popularidad. Estos sistemas eran funcionales hasta cierto punto, pero no podían personalizar la experiencia del usuario y mostraban elementos que no se correspondían a nuestros intereses.")
st.header("¿Cómo funciona la inteligencia artificial en los sistemas de recomendación?")
st.markdown("En la actualidad los sistemas de recomendación están por todas partes, son los encargados de mostrar contenido relacionado en portales de cine, productos similares en tiendas online y hasta anuncios adaptados a nuestros gustos en las redes sociales. Estos sistemas aprenden, literalmente, sobre los temas que nos gustan, y muestran todo el contenido que pueda ser interesante para nosotros basándose en nuestros gustos pasados, o lo que es lo mismo, en el patrón de elecciones que hemos tenido hasta la fecha en un portal determinado.")
st.header("Analisis de correlación: ")
st.markdown("El análisis de correlación consiste en un procedimiento estadístico para determinar si dos variables están relacionadas o no. El resultado del análisis es un coeficiente de correlación  que puede tomar valores entre -1 y +1.  El signo indica el  tipo de correlación entre las dos variables . Un signo positivo indica que existe una relación positiva entre las dos variables.  Un signo negativo  indica que existe una relación negativa entre las dos variables.  Si dos variables son independientes, el coeficiente de correlación es de magnitud cero.")
st.header("¿Qué es la correlación?")
st.markdown("La correlación es un tipo de asociación entre dos variables numéricas, específicamente evalúa la *tendencia (creciente o decreciente) en los datos*. Usualmente las correlaciones se escriben con dos números clave: r = y p = . Cuanto más se aproxima r a cero, más débil es la relación lineal. Los valores de r positivos indican una correlación positiva, en la que los valores de ambas variables tienden a incrementarse juntos.")
st.header("Tipos de correlación:")
st.markdown("Mientras que la correlación estudia cómo se relacionan dos entidades entre sí, el coeficiente de correlación mide la fuerza de la relación entre las dos variables. En estadística, hay tres tipos de coeficientes de correlación. Son los siguientes:")
st.markdown("- Correlación de Pearson: La correlación de Pearson es la medida más utilizada para determinar una relación lineal entre dos variables. Cuanto más fuerte sea la correlación entre estos dos conjuntos de datos, más cerca estará de +1 o -1.")
st.markdown("- Correlación de Spearman: Este tipo de correlación se utiliza para determinar la relación o asociación monótona entre dos conjuntos de datos. A diferencia del coeficiente de correlación de Pearson, se basa en los valores clasificados de cada conjunto de datos y utiliza variables asimétricas u ordinales en lugar de las distribuidas normalmente.")
st.markdown("- Correlación con Kendall: Este tipo de correlación mide la fuerza de la dependencia entre dos conjuntos de datos.")
st.header("Correlación de Pearson")
st.markdown("El coeficiente de correlación de Pearson, también llamado coeficiente de correlación lineal o simplemente coeficiente de correlación, es una medida estadística que indica la relación entre dos variables. Para calcular este coeficiente se debe dividir la covarianza de dichas variables por la raíz cuadrada del producto de sus varianzas. De manera que el coeficiente de correlación de Pearson trata de cuantificar la dependencia lineal entre dos variables aleatorias cuantitativas. ")
st.markdown("El valor del índice de correlación de Pearson está entre -1 y +1, ambos incluidos.")
st.header("¿Cómo se interpreta la correlación de Pearson?: ")
st.markdown("El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.")
st.markdown(" - un valor positivo indica una relación directa o positiva.")
st.markdown(" - un valor negativo indica relación indirecta, inversa o negativa.")
st.markdown(" - un valor nulo indica que no existe una tendencia entre ambas variables.")
st.markdown("La magnitud nos indica la fuerza de la relación, y toma valores entre -1 a 1. Cuanto más cercano sea el valor a los extremos del intervalo (1 o -1) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.")
st.markdown(" - si la correlación vale 1 o -1 diremos que la correlación es “perfecta”.")
st.markdown(" - si la correlación vale 0 diremos que las variables no están correlacionadas.")
img3 = Image.open('imagenes/correlacion.png')
st.image(img3, width=700)
st.header("Regresión lineal")
st.markdown("La regresión lineal se usa para encontrar una relación lineal entre el objetivo y uno o más predictores.")
st.markdown("La regresión lineal es una técnica de modelado estadístico que se emplea para describir una variable de respuesta continua como una función de una o varias variables predictoras. Puede ayudar a comprender y predecir el comportamiento de sistemas complejos o a analizar datos experimentales, financieros y biológicos. Es común que hagamos uso de una hoja de cálculo sobre la cual aplicamos las fórmulas de regresión lineal.")
st.markdown("Para llevar a cabo, necesitaremos una serie de librerías, vamos a describir cada una de ellas: Numpy: Es el paquete fundamental para la computación en matrices con Python. Matplotlib: Es un paquete para crear gráficos en Python. Sklearn: Un conjunto de módulos de Python para el aprendizaje automático y la minería de datos.")
img6 = Image.open('imagenes/regre.png')
st.image(img6, width=700)
st.header("Escala de Likert")
st.markdown("La escala de Likert es un modelo de encuesta que suele incluir de 5 a 7 opciones de respuesta que van desde muy de acuerdo a muy en desacuerdo, con una opción neutral en el medio. La escala puede utilizarse para medir una serie de temas diferentes, como la probabilidad, el acuerdo, la calidad, la frecuencia y la importancia.")
img7 = Image.open('imagenes/likert.png')
st.image(img7, width=700)
st.markdown("Ventajas de usar una escala de Likert:")
st.markdown(" - La medición de los comentarios a través de preguntas de escala Likert también proporciona una visión más matizada.")
st.markdown(" - Es una forma sencilla de generar información para el análisis de datos.")
st.markdown(" - Las preguntas tipo Likert ofrecen más datos para trabajar sobre la intención, perspectiva y la importancia que le dan a ciertos temas. Además, es más fácil analizar las respuestas de los encuestados con las preguntas cuantitativas de Likert ")
st.header("NumPy")
st.markdown("NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos. Incorpora una nueva clase de objetos llamados arrays que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación. La ventaja de Numpy frente a las listas predefinidas en Python es que el procesamiento de los arrays se realiza mucho más rápido (hasta 50 veces más) que las listas, lo cual la hace ideal para el procesamiento de vectores y matrices de grandes dimensiones.")
img8 = Image.open('imagenes/numpy.png')
st.image(img8, width=700)
st.header("Pandas")
st.markdown("Pandas es una librería de código abierto dentro de los desarrolladores de Python. Ofrece unas estructuras muy poderosas y flexibles que facilitan la manipulación y tratamiento de datos.")
img9 = Image.open('imagenes/Pandas.png')
st.image(img9, width=700)
st.header("Caso Netflix")
st.markdown("Todo lo explicado anteriormente se da en un caso ideal, es decir, que todos los datos fueron respondidos. Pero ¿qué pasa cuando el usuario encuestado no responde a la pregunta? Esto se conoce como la variable humana y es algo que no podemos controlar. Es por ello que existen los métodos de inputación para poder rellenar esos valores con otro valor que guarde relación con mas demás.")
