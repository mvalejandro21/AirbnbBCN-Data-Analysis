import streamlit as st

# Configurar la página
st.set_page_config(
    page_title="Airbnb Barcelona Analysis",
    page_icon="🏠",
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

# --- CONTENIDO DE LA PÁGINA DE INTRODUCCIÓN ---

st.title("🏡 Análisis de Airbnb en Barcelona")

st.markdown("""
<div class="custom-block">
    <h2>📍 ¿Por qué Barcelona?</h2>
    <p>
        He elegido Barcelona como foco de este análisis porque es mi ciudad. Esto me permite interpretar los datos 
        no solo desde lo técnico, sino también desde el conocimiento local de barrios, turismo y dinámica urbana.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-block">
    <h2>🛠️ Enfoque metodológico</h2>
    <ul>
        <li>🔍 Exploración inicial en <strong>Jupyter Notebook</strong> para conocer la estructura del dataset y detectar problemas.</li>
        <li>🧹 Limpieza de datos organizada en módulos separados (tratamiento de nulos, outliers, codificación...)</li>
        <li>📊 Análisis y visualización en <strong>Power BI</strong>, que permite construir dashboards dinámicos e interactivos.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-block">
    <h2>📂 ¿Qué encontrarás en esta app?</h2>
    <ul>
        <li>📁 <strong>Limpieza de Datos</strong> – Cómo se procesaron los datos para dejar un conjunto fiable y modelable.</li>
        <li>📈 <strong>Dashboards</strong> – Visualizaciones en Power BI integradas directamente en la app.</li>
        <li>🔍 <strong>Insights</strong> – Comparativas entre superhosts, empresas como anfitriones, barrios y más.</li>
        <li>🌍 <strong>Distribución geográfica</strong> – Mapas de rentabilidad y concentración por zona.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.success("Desliza el menú lateral izquierdo para explorar cada sección del análisis 📊")
