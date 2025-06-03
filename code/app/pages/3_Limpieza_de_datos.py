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


import streamlit as st

st.title("🔧 Limpieza de Datos")

# Introducción general
st.markdown("""
En esta sección explicamos cómo llevamos a cabo el proceso de limpieza de datos antes del análisis.  
Organizamos la limpieza en pasos separados mediante una **estructura de carpetas**, donde cada subcarpeta representaba una fase del preprocesamiento: eliminación de duplicados, renombrado de columnas, imputación de valores nulos, codificación, etc.

---

""")

# Eliminación de duplicados y estandarización
st.header("📁 Estructura de carpetas y pasos previos")
st.markdown("""
- **Eliminación de duplicados**: Se eliminaron registros completamente repetidos utilizando `drop_duplicates()`.
- **Estandarización de nombres de columnas**:
  - Convertimos todos los nombres a **minúsculas**.
  - Reemplazamos **espacios y caracteres especiales** por `_`.
  - Eliminamos **caracteres no alfabéticos** innecesarios.
  - Ejemplo:
    ```python
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_').str.replace(r'\W+', '', regex=True)
    ```

- **Eliminación de columnas innecesarias**:
  - Se eliminaron columnas irrelevantes para el análisis, como identificadores únicos que no aportaban valor, timestamps duplicados, entre otros.

---

""")

# Imputación de valores nulos
st.header("🧩 Tratamiento de valores nulos")

st.markdown("""
Una vez eliminadas columnas innecesarias y tratadas las constantes y vacías, nos centramos en **imputar valores faltantes**. Esta fase es clave para garantizar que el análisis sea fiable y no sesgado por ausencias aleatorias o estructurales en los datos.

Clasificamos los valores nulos en tres categorías según el patrón de "missingness":

- **MCAR** (Missing Completely At Random): Imputación simple (media, mediana o moda).
- **MAR** (Missing At Random): Imputación con modelos (regresión, MICE, etc.).
- **MNAR** (Missing Not At Random): En general, no imputamos. Creamos flags o eliminamos.

""")

# Variable por variable
with st.expander("🛁 bathrooms"):
    st.markdown("""
    - Algunas observaciones carecen de valor en bathrooms pero sí contienen texto en bathrooms_text.
    - **Estrategia**: si hay bathrooms_text, extraemos de ahí. Si no hay ninguna referencia, imputamos por la **media de baños** del conjunto similar.
    - Se añadió una columna *flag* que indica si el valor fue imputado.
    """)

with st.expander("🛏️ bedrooms, beds"):
    st.markdown("""
    - Variables numéricas continuas con pocos nulos.
    - Usamos **regresión bayesiana (BayesianRidge)** para predecir valores usando variables correlacionadas como `accommodates`, `property_type`, etc.
    """)

with st.expander("💰 price"):
    st.markdown("""
    - Preprocesamos para convertir el precio a formato numérico (`float`).
    - Si no hay `price` ni `estimated_revenue`, o si la disponibilidad es baja, marcamos como **precio cero**.
    - Resto: imputado con **regresión bayesiana**.
    - Se añade `flag_price_imputed` para trazabilidad.
    """)

with st.expander("📅 availability_30, availability_365"):
    st.markdown("""
    - Nulos suelen corresponder a alojamientos inactivos.
    - Imputamos con 0 si se detecta baja disponibilidad e ingresos.
    - Resto: se conserva nulo o se imputa con la mediana si se detecta patrón MAR.
    """)

with st.expander("📈 estimated_revenue_l365d"):
    st.markdown("""
    - Si `price = 0` y `availability_365 = 0` → revenue = 0.
    - Si hay `price` y `availability`, pero falta `revenue`, usamos **MICE** (Multivariate Imputation by Chained Equations).
    """)

with st.expander("📝 reviews_per_month, number_of_reviews"):
    st.markdown("""
    - Si el alojamiento nunca ha recibido una review, imputamos con 0.
    - Se añadió columna binaria `has_reviews`.
    """)

with st.expander("🌟 review_scores_*"):
    st.markdown("""
    - No se imputan valores nulos en puntuaciones, ya que sin reviews no es posible estimarlas.
    - Se mantienen los nulos.
    """)

# Codificación
st.header("🏷️ Codificación y Flags")

st.markdown("""
- Variables categóricas binarias: codificadas con **Label Encoding**.
- Variables nominales: se evita One-Hot Encoding para no aumentar excesivamente la dimensionalidad.
- Para cada imputación importante se añade una columna *flag_* que permite identificar los valores imputados artificialmente.
""")

# Outliers
st.header("📊 Detección y tratamiento de Outliers")

st.markdown("""
El tratamiento se hizo de forma diferenciada por variable:

- En variables como `beds`, `bedrooms`, `bathrooms`, `price`, `estimated_revenue`:
  - Se aplicó **capping dinámico** (ej. percentiles P1–P99) para suavizar los extremos sin eliminar información.
  - Ejemplo de código:
    ```python
    if use_percentile:
                lower, upper = df[col].quantile([0.01, 0.99])
            else:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - multiplier * IQR
                upper = Q3 + multiplier * IQR
    ```

- En otras como `number_of_reviews`, `accommodates`:
  - Se mantuvieron los outliers ya que representan comportamientos reales extremos (por ejemplo, hostales con muchas camas).

---

""")



