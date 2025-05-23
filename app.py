import streamlit as st
import pandas as pd

# Cargar datos desde archivos locales
clientes = pd.read_csv("clientes.csv")
mercados = pd.read_csv("mercados.csv")
exportaciones = pd.read_csv("exportaciones.csv")
barreras = pd.read_csv("barreras.csv")

# Título del Dashboard
st.title("Dashboard Interactivo de Exportaciones de Chocolates")

# Filtro de país
paises = exportaciones["País"].unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises)

# Mostrar datos de clientes
st.subheader("Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)

# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]
st.dataframe(exportaciones_filtradas)

# Gráfico de exportaciones
if not exportaciones_filtradas.empty:
    st.bar_chart(exportaciones_filtradas.set_index("País")["Exportaciones (USD millones)"])

# Mostrar datos de mercados
st.subheader("Segmentos de Mercado")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
st.dataframe(mercados_filtrados)

# Mostrar barreras de entrada
st.subheader("Barreras de Entrada")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
st.dataframe(barreras_filtradas)

# Análisis Comparativo
st.subheader("Análisis Comparativo")
mercados_group = mercados.groupby("País")["Tamaño del Mercado (USD millones)"].sum()
st.bar_chart(mercados_group)
