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
