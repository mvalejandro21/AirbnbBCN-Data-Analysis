import streamlit as st

st.set_page_config(page_title="Selector de Informes", layout="wide")

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

st.title("📊 Visualización de Informes Airbnb - Barcelona")




st.divider()

# Selector de informe
informe = st.selectbox("📁 Selecciona el informe que deseas visualizar:", 
                       ["Informe por barrios de barcelona", "Informe superhosts vs no superhosts", "Informe tipo de habitación", "Informe de comparación de hosts"])

# Contenido según el informe elegido
if informe == "Informe por barrios de barcelona":

    st.markdown("""
    <div style="display: flex; justify-content: center;">
    <iframe src="https://app.powerbi.com/view?r=eyJrIjoiZjBkNzY3MmUtYTdkNC00MDc4LTlkOWUtMDg3ZTBmOGRmNTM2IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=0b3fa4ce8555f0ec6995" width="800" height="600" style="border:none;"></iframe>
    </div>
    """, unsafe_allow_html=True)

    st.title("📊 Conclusiones clave del análisis de barrios de Barcelona")

    # Bloque 1: L’Eixample
    st.header("💎 1. L’Eixample: líder absoluto en rentabilidad")
    st.markdown("""
    - **Barrio más rentable de Barcelona**, con precios promedio elevados.
    - Alta demanda debido a su ubicación estratégica cerca de **la Sagrada Familia**, **Passeig de Gràcia** y una gran variedad de comercios y restaurantes.
    - Es una **zona central y turística**, lo que **garantiza ocupación alta y retorno elevado** para anfitriones.
    - **Dreta de l’Eixample** destaca como el punto más rentable dentro del distrito.
    """)
    st.divider()

    # Bloque 2: Cercanía a Plaça Catalunya
    st.header("📍 2. Cercanía a Plaça Catalunya: clave para la rentabilidad")
    st.markdown("""
    - El **mapa de ingresos revela una tendencia clara**: **a menor distancia de Plaça Catalunya, mayor rentabilidad**.
    - Barrios cercanos como el **Raval**, el **Gòtic** y la **Barceloneta** presentan alta demanda turística y buena ocupación.
    - La localización central **prima sobre el precio**.
    """)
    st.divider()

    # Bloque 3: Sarrià-Sant Gervasi
    st.header("💸 3. Sarrià-Sant Gervasi: lujo sin retorno proporcional")
    st.markdown("""
    - Es uno de los barrios con **precios promedio más altos** de la ciudad.
    - Sin embargo, **su rentabilidad y ocupación son bajas**, lo que indica que un precio elevado **no asegura mayor retorno**.
    - La **lejanía del centro turístico** parece ser un factor clave en su bajo rendimiento.
    """)
    st.divider()

    # Bloque 4: Sants-Montjuïc
    st.header("🚆 4. Sants-Montjuïc: alta ocupación y buena conexión")
    st.markdown("""
    - Destaca por una **alta ocupación**, a pesar de no ser un barrio central.
    - Su **conectividad mediante la Estación de Sants** y precios más accesibles lo convierten en una **opción ideal para viajeros prácticos**.
    - Es una **zona estratégica para anfitriones que buscan equilibrio entre demanda y precio**.
    """)
    st.divider()

    # Bloque 5: Barrios periféricos
    st.header("🧭 5. Barrios periféricos: bajo impacto turístico")
    st.markdown("""
    - Zonas como **Les Corts**, **Sant Andreu** o **Nou Barris** no aparecen entre los barrios con alta rentabilidad u ocupación.
    - **Ni tienen precios elevados, ni ubicación estratégica**, lo que se traduce en **menor atractivo turístico**.
    """)
    st.divider()

    # Bloque 6: Scatter plots
    st.header("📊 6. Scatter plots: datos valiosos sobre tendencias y excepciones")
    st.markdown("""
    - Muestran **medias de ocupación y rentabilidad por barrio**, separadas por distrito.
    - **Nou Barris** y **Sarrià-Sant Gervasi** presentan muy baja ocupación.
    - **No hay una correlación clara entre precio y ocupación**: lo que **más influye es la ubicación**, no el coste.
    - Barrios alejados como **La Sagrera**, **La Teixonera** o **Les Roquetes** alcanzan ocupaciones similares a zonas céntricas como la Dreta de l’Eixample, gracias a un buen **equilibrio entre precio y ubicación**.
    """)
    st.divider()

    # Bloque 7: Outliers
    st.header("❗ 7. Outliers: casos extremos a tener en cuenta")
    st.markdown("""
    - **Torre Baró** (Nou Barris) y **Baró de Viver** (Sant Andreu) presentan casos extremos: uno con **casi 0 ingresos y ocupación**, el otro con ingresos **muy altos (140 € media)**.
    - Ambos están **en la periferia**, pero muestran cómo puede haber grandes diferencias dentro del mismo distrito.
    """)
    st.divider()

    # Bloque 8: Sant Martí
    st.header("🏖️ 8. Sant Martí: precios premium por playa y turismo")
    st.markdown("""
    - Algunos barrios como **Diagonal Mar** y **la Vila Olímpica** tienen **precios superiores a Dreta de l’Eixample**.
    - Se debe a que **están en primera línea de playa**, con perfil muy turístico.
    - Atraen a visitantes por su ambiente vacacional, lo que **eleva la demanda y el precio**.
    """)
    st.divider()

    # Bloque 9: Casos fuera de Barcelona
    st.header("🧩 9. Casos fuera de Barcelona: anomalía interesante")
    st.markdown("""
    - Se detecta un punto con **rentabilidad y ocupación mucho mayores al resto**.
    - No pertenece a la ciudad de Barcelona, sino a **otro municipio cercano de otra comarca**, por lo tanto **no es representativo del mercado barcelonés**.
    """)
    st.divider()

    # Bloque 10: Precio vs Revenue
    st.header("📈 10. Revenue y precio: una relación parcial")
    st.markdown("""
    - En el scatter plot de revenue, **sí se ve cierta correlación entre precio y revenue total**.
    - Sin embargo, **la cercanía al centro sigue siendo un factor decisivo**.
    - Ejemplo: **Sarrià-Sant Gervasi**, con precios similares a Sants-Montjuïc, genera **mucho menos revenue** porque **no está cerca del centro ni es turístico**.
    """)


elif informe == "Informe superhosts vs no superhosts":

    st.markdown("""
    <div style="display: flex; justify-content: center;">
    <iframe src="https://app.powerbi.com/view?r=eyJrIjoiZjBkNzY3MmUtYTdkNC00MDc4LTlkOWUtMDg3ZTBmOGRmNTM2IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=b2fe3ea58efbff51d0f7" width="800" height="600" style="border:none;"></iframe>
    </div>
    """, unsafe_allow_html=True)

    st.header("📌 Informe 2: Relación Precio vs Rentabilidad")
    st.markdown("""
    🌟 🔍 Conclusiones clave del análisis de Superhosts vs. no Superhosts
    💼 1. Ser Superhost marca una gran diferencia en rentabilidad
    Aunque el precio medio por noche no varía mucho entre Superhosts y el resto, el revenue anual estimado de los Superhosts es notablemente superior. Esto indica que reciben más reservas y, por tanto, son más rentables.

    ✅ 2. Más confianza, más reservas
    Los Superhosts generan mayor confianza en los huéspedes, lo que aumenta su tasa de ocupación. Además, Airbnb podría favorecerlos en los resultados de búsqueda, dándoles más visibilidad y oportunidades de reserva.

    📝 3. Las valoraciones confirman el éxito
    A pesar de que hay más anfitriones que no son Superhosts, la suma total de valoraciones no difiere tanto. De hecho, los anuncios gestionados por Superhosts tienen un promedio de 70 reviews más, lo cual refuerza su mayor nivel de actividad.

    🗺️ 4. Distribución geográfica: no dependen de la zona
    El mapa de distribución muestra que los Superhosts no se concentran en zonas más rentables, sino que están repartidos de forma equitativa por la ciudad. Su éxito no depende tanto de la ubicación como de su prestigio como anfitriones.

    📊 5. Ser Superhost sí merece la pena
    Los datos reflejan que el programa de Superhost de Airbnb funciona correctamente. Los anfitriones con esta distinción logran una rentabilidad significativamente mayor, lo que demuestra que premiar a los mejores genera un efecto positivo tanto para ellos como para la plataforma.
    """)

elif informe == "Informe tipo de habitación":

    st.markdown("""
    <div style="display: flex; justify-content: center;">
    <iframe src="https://app.powerbi.com/view?r=eyJrIjoiZjBkNzY3MmUtYTdkNC00MDc4LTlkOWUtMDg3ZTBmOGRmNTM2IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=fd45ada333d06d7ab805" width="800" height="600" style="border:none;"></iframe>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 🏆 **1. Entire home/apartment: el más rentable y popular**

- **Ingresos estimados más altos**: con un promedio de **16.000 € anuales**, duplica o cuadruplica a otros tipos.
- **Mayor ocupación promedio**: **100%**, lo que indica una demanda muy fuerte.
- **Mayor presencia en el mercado**: representa el **tipo más ofertado**, con casi **12.000 anuncios**.
- **Conclusión:** Este tipo es el más atractivo para anfitriones por su **alta rentabilidad y ocupación**, y también para los turistas por la privacidad y comodidad que ofrece.

---

### 🛏️ **2. Private room: bajo ingreso, pero muy común**

- **Ingresos bajos**: en promedio solo **4.000 € al año**, el más bajo del grupo.
- **Ocupación media-baja**: 55%.
- **Segundo tipo más ofertado**: con **7.390 anuncios**, es **muy común**, especialmente en zonas céntricas.
- **Conclusión:** Aunque es poco rentable por unidad, su **popularidad se debe a barreras de entrada más bajas** (es más fácil alquilar una habitación que un piso entero) y su accesibilidad para viajeros con presupuestos bajos.

---

### 🏨 **3. Hotel room: ingresos y ocupación moderados, pero poca presencia**

- **Ingresos promedio:** 7.000 €, más que private y shared, pero menos que entire home.
- **Ocupación baja:** solo 50%.
- **Presencia casi marginal**: solo **110 anuncios**.
- **Localización céntrica**: aparecen en zonas turísticas de alta densidad.
- **Conclusión:** Aunque podrían generar ingresos razonables, **no están bien representadas en Airbnb**, probablemente por regulaciones o porque los hoteles usan otras plataformas. Es un tipo **residual** en esta muestra.

---

### 🧍‍♂️ **4. Shared room: poco común y poco rentable**

- **Ingresos promedio:** 5.000 €
- **Ocupación media-alta:** 78%, mejor que private y hotel.
- **Muy pocos anuncios:** 110 aproximadamente.
- **Conclusión:** Aunque no es el peor en ocupación, su **falta de privacidad limita su popularidad**. Es un formato más común en mochileros o estancias muy económicas, y su **baja presencia indica baja demanda u oferta**.

---

## 🗺️ 🔍 Conclusión del mapa (distribución geográfica)

- **Hotel room y private room** están **más presentes en zonas céntricas** (Ej: Eixample, Gòtic, Raval).
- Esto tiene sentido porque **los viajeros con presupuestos ajustados suelen buscar zonas bien ubicadas**, aunque los ingresos no sean los más altos.
- **Entire home/apartment** está más disperso y es el más flexible geográficamente, posiblemente porque tiene **demanda en casi todas las zonas**.
    """)

elif informe == "Informe de comparación de hosts":

    st.markdown("""
    <div style="display: flex; justify-content: center;">
    <iframe src="https://app.powerbi.com/view?r=eyJrIjoiZjBkNzY3MmUtYTdkNC00MDc4LTlkOWUtMDg3ZTBmOGRmNTM2IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=7b2d0c59b0b638c961e" width="800" height="600" style="border:none;"></iframe>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    ## 🧩 Análisis comparativo de hosts: Sweet Inn vs Ukio

Al analizar los datos de los hosts presentes en el mercado de Airbnb en Barcelona, resulta llamativa la presencia de **empresas como Ukio, Enter o Acommodis**, que gestionan múltiples propiedades. Este hallazgo me llevó a profundizar en su **modelo de negocio y rentabilidad**, centrándome en dos casos destacados: **Ukio** y **Sweet Inn**.

### 📊 Volumen vs Rentabilidad

Ukio es el **host con mayor número de listings en la ciudad**, lo cual podría hacernos pensar que lidera en rentabilidad. Sin embargo, en el ranking de **revenue anual estimado**, se encuentra en **quinta posición**, mientras que **Sweet Inn**, con menos de la mitad de propiedades, lidera claramente con la **mayor suma de ingresos**.

Esto plantea una pregunta clave:

> ¿Cómo puede Sweet Inn superar tan ampliamente a Ukio en rentabilidad, teniendo menos propiedades?
> 

### 🔍 Variables analizadas

**1. Room Type**

Ambas empresas ofrecen mayoritariamente el tipo "Entire Home", por lo tanto, este factor no explica las diferencias.

**2. Capacidad del alojamiento (accommodates)**

Sweet Inn: 5.09 personas de media

Ukio: 4.02 personas de media

➡️ Esto indica que Sweet Inn ofrece propiedades algo más grandes, lo cual podría justificar precios más altos.

**3. Número de habitaciones, baños y camas**

Sweet Inn tiene promedios más altos en estas tres variables, aunque la diferencia **no supera la unidad** en ninguno de los casos. Esto sugiere alojamientos ligeramente más amplios o mejor equipados, pero **no lo suficiente para justificar por sí solo la brecha en ingresos**.

### 💰 Ingresos y precios

**Precio promedio por listing:**

- Sweet Inn: ~199 €
- Ukio: ~149 €
    
    ➡️ Una diferencia de aproximadamente **50 € por noche**.
    

Sin embargo, al observar la **suma total del precio por noche de todos sus listings**, Ukio supera a Sweet Inn debido a su volumen:

- Ukio: ~50,000 €
- Sweet Inn: ~34,000 €

Este dato **parecería contradecir** la mayor rentabilidad de Sweet Inn, pero es aquí donde entra un factor clave:

### 📈 Ocupación, Reseñas y Engagement

**1. Ocupación total:**

- Sweet Inn: 27,144 días ocupados (suma)
- Ukio: 5,768 días ocupados

**2. Rating total:**

- Sweet Inn: 1,042 estrellas
- Ukio: 674 estrellas

**3. Reviews por mes (suma):**

- Sweet Inn: 465
- Ukio: 30

➡️ **Sweet Inn no solo cobra más por noche**, sino que **tiene una ocupación muy superior**, lo que dispara sus ingresos totales. Además, los altos ratings y volumen de reviews por mes sugieren **mayor satisfacción y engagement de los usuarios**, que puede deberse a una mejor experiencia o servicio.

---

## 🗺️ Distribución geográfica: ¿Dónde están ubicados?

Un análisis mediante mapa refuerza aún más estas conclusiones:

- **Ukio** tiene sus propiedades repartidas **principalmente en el centro de Barcelona**, pero también en zonas algo más periféricas y menos turísticas como **Les Corts, El Clot, Sant Gervasi o Sant Martí**. Aunque algunas de sus propiedades en el centro muestran buen rendimiento, **la mayoría no alcanzan revenues muy altos**, lo que podría deberse a una gestión masiva con enfoque menos personalizado.
- En cambio, **Sweet Inn presenta una estrategia mucho más focalizada**: sus listings están **agrupados en zonas muy rentables** y altamente turísticas como **Ciutat Vella, Gràcia o el Eixample (Diagonal/Passeig de Gràcia)**. Casi todas estas propiedades reflejan **niveles altos de revenue**, lo que confirma que una buena **ubicación estratégica** combinada con una **oferta premium** puede maximizar los ingresos incluso con menor volumen de listings.

---

## 🧠 Conclusiones finales

- **Ukio apuesta por volumen**, pero con precios más bajos, menor ocupación y dispersión en zonas menos óptimas, su rentabilidad por propiedad es baja.
- **Sweet Inn optimiza calidad y localización**, posicionando sus viviendas en zonas premium, con precios altos, mejor ocupación y mayor valoración.
- Este caso demuestra que en el mercado de Airbnb **una estrategia focalizada y selectiva puede ser mucho más rentable** que una expansiva y generalista.
    """)

# Puedes agregar aquí cualquier otro bloque de contenido adicional si quieres
