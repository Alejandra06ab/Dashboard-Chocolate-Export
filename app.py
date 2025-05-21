import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URLs de los archivos CSV
# Asegúrate de reemplazar 'YOUR_GITHUB_USERNAME' con tu nombre de usuario de GitHub
# y que los archivos CSV estén en el directorio 'main' (o la rama que estés usando) de tu repositorio público.
clientes_url = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/Dashboard-ChocolateExport/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/Dashboard-ChocolateExport/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/Dashboard-ChocolateExport/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/Dashboard-ChocolateExport/main/barreras.csv"



# Cargar los datos
@st.cache_data # Decorador para cachear los datos y mejorar el rendimiento
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
st.subheader("Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
if not clientes_filtrados.empty:
    st.dataframe(clientes_filtrados)
else:
    st.write(f"No hay datos de clientes disponibles para {pais_seleccionado}.")


# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]

if not exportaciones_filtradas.empty:
    fig, ax = plt.subplots(figsize=(10, 6)) # Aumentar el tamaño de la figura para mejor visualización
    ax.bar(exportaciones_filtradas["Año"], exportaciones_filtradas["Exportaciones (USD millones)"], color='#2E86C1')
    ax.set_xlabel("Año")
    ax.set_ylabel("Exportaciones (USD millones)")
    ax.set_title(f"Exportaciones de Chocolates en {pais_seleccionado}")
    plt.xticks(rotation=45, ha='right') # Rotar etiquetas del eje x para evitar superposición
    plt.tight_layout() # Ajustar el diseño para que no se corten las etiquetas
    st.pyplot(fig)
else:
    st.write(f"No hay datos de exportaciones disponibles para {pais_seleccionado}.")

# Mostrar datos de mercados
st.subheader("Segmentos de Mercado")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
if not mercados_filtrados.empty:
    st.dataframe(mercados_filtrados)
else:
    st.write(f"No hay datos de segmentos de mercado disponibles para {pais_seleccionado}.")

# Mostrar barreras de entrada
st.subheader("Barreras de Entrada")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
if not barreras_filtradas.empty:
    st.dataframe(barreras_filtradas)
else:
    st.write(f"No hay datos de barreras de entrada disponibles para {pais_seleccionado}.")

# Análisis Comparativo
st.subheader("Análisis Comparativo de Tamaño de Mercado")
if not mercados.empty:
    fig2, ax2 = plt.subplots(figsize=(12, 7)) # Aumentar el tamaño de la figura
    ax2.bar(mercados["País"], mercados["Tamaño del Mercado (USD millones)"], color='#F39C12')
    ax2.set_xlabel("País")
    ax2.set_ylabel("Tamaño del Mercado (USD millones)")
    ax2.set_title("Comparación de Tamaños de Mercado por País")
    plt.xticks(rotation=60, ha='right') # Rotar más las etiquetas para muchos países
    plt.tight_layout()
    st.pyplot(fig2)
else:
    st.write("No hay datos disponibles para el análisis comparativo de tamaño de mercado.")

El mié, 21 may 2025 a las 0:54, José Manuel (<jmaa118@gmail.com>) escribió:
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URLs de los archivos CSV
# Asegúrate de reemplazar 'TU_NOMBRE_DE_USUARIO_GITHUB' con tu nombre de usuario de GitHub
# y que los archivos CSV estén en el directorio 'main' (o la rama que estés usando) de tu repositorio público.
clientes_url = "https://raw.githubusercontent.com/TU_NOMBRE_DE_USUARIO_GITHUB/Dashboard-ChocolateExport/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/TU_NOMBRE_DE_USUARIO_GITHUB/Dashboard-ChocolateExport/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/TU_NOMBRE_DE_USUARIO_GITHUB/Dashboard-ChocolateExport/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/TU_NOMBRE_DE_USUARIO_GITHUB/Dashboard-ChocolateExport/main/barreras.csv"

# Cargar los datos
@st.cache_data # Decorador para cachear los datos y mejorar el rendimiento
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
st.subheader("Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
if not clientes_filtrados.empty:
    st.dataframe(clientes_filtrados)
else:
    st.write(f"No hay datos de clientes disponibles para {pais_seleccionado}.")


# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]

if not exportaciones_filtradas.empty:
    fig, ax = plt.subplots(figsize=(10, 6)) # Aumentar el tamaño de la figura para mejor visualización
    ax.bar(exportaciones_filtradas["Año"], exportaciones_filtradas["Exportaciones (USD millones)"], color='#2E86C1')
    ax.set_xlabel("Año")
    ax.set_ylabel("Exportaciones (USD millones)")
    ax.set_title(f"Exportaciones de Chocolates en {pais_seleccionado}")
    plt.xticks(rotation=45, ha='right') # Rotar etiquetas del eje x para evitar superposición
    plt.tight_layout() # Ajustar el diseño para que no se corten las etiquetas
    st.pyplot(fig)
else:
    st.write(f"No hay datos de exportaciones disponibles para {pais_seleccionado}.")

# Mostrar datos de mercados
st.subheader("Segmentos de Mercado")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
if not mercados_filtrados.empty:
    st.dataframe(mercados_filtrados)
else:
    st.write(f"No hay datos de segmentos de mercado disponibles para {pais_seleccionado}.")

# Mostrar barreras de entrada
st.subheader("Barreras de Entrada")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
if not barreras_filtradas.empty:
    st.dataframe(barreras_filtradas)
else:
    st.write(f"No hay datos de barreras de entrada disponibles para {pais_seleccionado}.")

# Análisis Comparativo
st.subheader("Análisis Comparativo de Tamaño de Mercado")
if not mercados.empty:
    fig2, ax2 = plt.subplots(figsize=(12, 7)) # Aumentar el tamaño de la figura
    ax2.bar(mercados["País"], mercados["Tamaño del Mercado (USD millones)"], color='#F39C12')
    ax2.set_xlabel("País")
    ax2.set_ylabel("Tamaño del Mercado (USD millones)")
    ax2.set_title("Comparación de Tamaños de Mercado por País")
    plt.xticks(rotation=60, ha='right') # Rotar más las etiquetas para muchos países
    plt.tight_layout()
    st.pyplot(fig2)
