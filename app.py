import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URLs de los archivos CSV
# Asegúrate de que estos URLs sean correctos y apunten a tus archivos raw en GitHub.
# Para el usuario 'Alejandra06ab', los URLs deberían ser algo como esto:
clientes_url = "https://raw.githubusercontent.com/Alejandra06ab/Dashboard-ChocolateExport/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/Alejandra06ab/Dashboard-ChocolateExport/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/Alejandra06ab/Dashboard-ChocolateExport/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/Alejandra06ab/Dashboard-ChocolateExport/main/barreras.csv"

# Cargar los datos
@st.cache_data # Decorador para cachear los datos y evitar recargarlos en cada interacción
def load_data():
    clientes = pd.read_csv(clientes_url)
    mercados = pd.read_csv(mercados_url)
    exportaciones = pd.read_csv(exportaciones_url)
    barreras = pd.read_csv(barreras_url)
    return clientes, mercados, exportaciones, barreras

clientes, mercados, exportaciones, barreras = load_data()

# Título del Dashboard
st.title("Dashboard Interactivo de Exportaciones de Chocolates")

# Filtro de país
paises = exportaciones["País"].unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises)

# Mostrar datos de clientes
st.subheader(f"Clientes en {pais_seleccionado}")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
if not clientes_filtrados.empty:
    st.dataframe(clientes_filtrados)
else:
    st.info(f"No hay datos de clientes disponibles para {pais_seleccionado}.")

# Mostrar datos de exportaciones
st.subheader(f"Exportaciones de Chocolates en {pais_seleccionado}")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]

if not exportaciones_filtradas.empty:
    fig, ax = plt.subplots()
    ax.bar(exportaciones_filtradas["Año"], exportaciones_filtradas["Exportaciones (USD millones)"], color='#2E86C1')
    ax.set_xlabel("Año")
    ax.set_ylabel("Exportaciones (USD millones)")
    ax.set_title(f"Exportaciones de Chocolates en {pais_seleccionado}")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.info(f"No hay datos de exportaciones disponibles para {pais_seleccionado}.")


# Mostrar datos de mercados
st.subheader(f"Segmentos de Mercado en {pais_seleccionado}")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
if not mercados_filtrados.empty:
    st.dataframe(mercados_filtrados)
else:
    st.info(f"No hay datos de segmentos de mercado disponibles para {pais_seleccionado}.")

# Mostrar barreras de entrada
st.subheader(f"Barreras de Entrada en {pais_seleccionado}")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
if not barreras_filtradas.empty:
    st.dataframe(barreras_filtradas)
else:
    st.info(f"No hay datos de barreras de entrada disponibles para {pais_seleccionado}.")


# Análisis Comparativo
st.subheader("Análisis Comparativo de Tamaño de Mercado por País")
if not mercados.empty:
    fig2, ax2 = plt.subplots(figsize=(10, 6)) # Aumentar tamaño para mejor visualización
    ax2.bar(mercados["País"], mercados["Tamaño del Mercado (USD millones)"], color='#F39C12')
    ax2.set_xlabel("País")
    ax2.set_ylabel("Tamaño del Mercado (USD millones)")
    ax2.set_title("Comparación de Tamaños de Mercado por País")
    plt.xticks(rotation=60, ha='right') # Rotar y alinear para etiquetas largas
    plt.tight_layout() # Ajustar el diseño para evitar el solapamiento
    st.pyplot(fig2)
