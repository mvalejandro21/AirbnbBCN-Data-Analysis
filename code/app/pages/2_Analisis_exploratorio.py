from pathlib import Path
import streamlit as st

# Configurar la página
st.set_page_config(
    page_title="Analisis Exploratorio de Airbnb Barcelona",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado con bloques más suaves (cian armonioso)
st.markdown("""
<style>
    /* Fondo general claro */
    .stApp {
        background-color: #EAF4FB;
        color: #2C3E50;
    }

    /* Sidebar clara */
    section[data-testid="stSidebar"] {
        background-color: #01a3af !important;
        color: #2C3E50;
    }
    

    /* Bloques personalizados con cian grisáceo y texto blanco */
    .custom-block {
        background-color: #01a3af;
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 25px;
    }

    .custom-block h1, .custom-block h2, .custom-block h3 {
        color: white;
    }

    /* Botones */
    .stButton>button {
        background-color: #00b99d;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #3a78c2;
        transition: 0.3s;
    }

    .custom-block p, .custom-block li {
        font-size: 1.1em;
        line-height: 1.5em;
    }
</style>
""", unsafe_allow_html=True)


st.title("🔍 Análisis Exploratorio de Airbnb Barcelona"
         " (Exploratory Data Analysis - EDA)")
st.markdown("""
Este análisis exploratorio tiene como objetivo comprender mejor los datos de Airbnb en Barcelona, 
identificando patrones, tendencias y áreas de interés a través de visualizaciones y estadísticas descriptivas.
""")


st.markdown("""
<div class="custom-block">
    <h2>📃 Archivos Analizados</h2>
    <p>
       Listings.csv: 19.422 registros, 79 columnas.
    </p>
</div> 
            """, unsafe_allow_html=True)


st.markdown("""
<div class="custom-block">
    <h2>⚠️ Observacion de cantidad nulos</h2>
    <p>
       A continuacion se muestran los nulos encontrados en el dataset Listings.csv usando un grafico de barras que nos 
ayuda a identificar las columnas con mayor cantidad de valores nulos.
    </p>
    </div> 
                """, unsafe_allow_html=True)
    
from PIL import Image
from pathlib import Path
import streamlit as st

ruta = Path(__file__).parent.parent / "assets" / "nullamount.png"

try:
    img = Image.open(ruta)
    st.image(img, caption="Gráfico de Nulos en Listings.csv")
except Exception as e:
    st.error(f"No se pudo cargar la imagen: {e}")

  
st.markdown("""
<div class="custom-block">
    <h2>⚠️ Observacion de patron de nulos</h2>
    <p>
       A continuacion se muestran los nulos encontrados en el dataset Listings.csv usando una matriz de calor que nos muestra la posicion de estos nulos en el dataset.
    </p>
    </div> 
                """, unsafe_allow_html=True)

from PIL import Image
from pathlib import Path
import streamlit as st

ruta = Path(__file__).parent.parent / "assets" / "nullgap.png"

try:
    img = Image.open(ruta)
    st.image(img, caption="Gráfico de Nulos en Listings.csv")
except Exception as e:
    st.error(f"No se pudo cargar la imagen: {e}")

st.markdown("""
<div class="custom-block">
    <h2>♦️ Identificando nulos</h2>
    <p>
       Una vez tenemos identificados los nulos, es importante observar el patron de estos nulos.
            Debido a que teniendo tanto la cantidad de nulos como el patron de estos, podemos tomar decisiones informadas sobre el tratamiento de 
            los datos faltantes.
    </p>
    <br>
    <p>
       A continuacion se muestra un archivo de Excel donde me he guiado para identificar los nulos y su patron. Las resoluciones y decisiones que se dicen tomar en el excel son
            intuitivas y algunas variaran por motivos de contexto que me encontrare mas adelante en el dataset.
    </p>
    </div> 
            """, unsafe_allow_html=True)

from PIL import Image
from pathlib import Path
import streamlit as st

ruta = Path(__file__).parent.parent / "assets" / "excel.jpg"

try:
    img = Image.open(ruta)
    st.image(img, caption="Gráfico de Nulos en Listings.csv")
except Exception as e:
    st.error(f"No se pudo cargar la imagen: {e}")