import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página de Streamlit
st.set_page_config(layout="wide", page_title="Dashboard de Exportación de Chocolate")

# Título principal del dashboard
st.title("🍫 Dashboard de Exportación de Chocolate 📊")

# Descripción
st.markdown("""
Este dashboard interactivo te permite explorar datos sobre la exportación de chocolate.
Puedes filtrar los datos por país, año y tipo de producto para obtener insights detallados.
""")

# --- Carga de datos de ejemplo ---
# En una aplicación real, cargarías tus datos desde un archivo CSV, Excel o una base de datos.
# Aquí creamos un DataFrame de ejemplo para demostrar la funcionalidad.
@st.cache_data
def load_data():
    data = {
        'Año': [2020, 2020, 2021, 2021, 2022, 2022, 2023, 2023],
        'País': ['Francia', 'Alemania', 'Francia', 'Alemania', 'Francia', 'Alemania', 'Francia', 'Alemania'],
        'Producto': ['Chocolate Negro', 'Chocolate con Leche', 'Chocolate Negro', 'Chocolate con Leche', 'Chocolate Negro', 'Chocolate con Leche', 'Chocolate Negro', 'Chocolate con Leche'],
        'Valor_Exportacion_USD': [150000, 120000, 160000, 130000, 170000, 140000, 180000, 150000],
        'Cantidad_KG': [5000, 4000, 5200, 4100, 5500, 4300, 5800, 4500]
    }
    df = pd.DataFrame(data)
    return df

df = load_data()

# --- Filtros en la barra lateral ---
st.sidebar.header("Filtros de Datos")

# Filtro por País
paises_disponibles = sorted(df['País'].unique())
pais_seleccionado = st.sidebar.multiselect(
    "Selecciona País(es):",
    options=paises_disponibles,
    default=paises_disponibles
)

# Filtro por Año
años_disponibles = sorted(df['Año'].unique())
año_seleccionado = st.sidebar.multiselect(
    "Selecciona Año(s):",
    options=años_disponibles,
    default=años_disponibles
)

# Filtro por Producto
productos_disponibles = sorted(df['Producto'].unique())
producto_seleccionado = st.sidebar.multiselect(
    "Selecciona Tipo de Producto:",
    options=productos_disponibles,
    default=productos_disponibles
)

# Aplicar filtros
df_filtrado = df[
    df['País'].isin(pais_seleccionado) &
    df['Año'].isin(año_seleccionado) &
    df['Producto'].isin(producto_seleccionado)
]

# --- Visualización de datos ---

if df_filtrado.empty:
    st.warning("No hay datos disponibles para la combinación de filtros seleccionada.")
else:
    st.subheader("Resumen de Datos Filtrados")
    st.dataframe(df_filtrado)

    # Gráfico 1: Valor de Exportación por Año y País
    st.subheader("Valor de Exportación por Año y País")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Año', y='Valor_Exportacion_USD', hue='País', data=df_filtrado, ax=ax1, palette='viridis')
    ax1.set_title('Valor de Exportación (USD) por Año y País')
    ax1.set_xlabel('Año')
    ax1.set_ylabel('Valor de Exportación (USD)')
    plt.xticks(rotation=45)
    st.pyplot(fig1)
    plt.close(fig1) # Cierra la figura para liberar memoria

    # Gráfico 2: Cantidad Exportada por Producto
    st.subheader("Cantidad Exportada por Producto")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Producto', y='Cantidad_KG', data=df_filtrado.groupby('Producto')['Cantidad_KG'].sum().reset_index(), ax=ax2, palette='magma')
    ax2.set_title('Cantidad Total Exportada (KG) por Producto')
    ax2.set_xlabel('Producto')
    ax2.set_ylabel('Cantidad Exportada (KG)')
    plt.xticks(rotation=45)
    st.pyplot(fig2)
    plt.close(fig2) # Cierra la figura para liberar memoria

    # Gráfico 3: Distribución del Valor de Exportación
    st.subheader("Distribución del Valor de Exportación")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.histplot(df_filtrado['Valor_Exportacion_USD'], kde=True, ax=ax3, color='skyblue')
    ax3.set_title('Distribución del Valor de Exportación (USD)')
    ax3.set_xlabel('Valor de Exportación (USD)')
    ax3.set_ylabel('Frecuencia')
    st.pyplot(fig3)
    plt.close(fig3) # Cierra la figura para liberar memoria

    # Métricas clave
    st.subheader("Métricas Clave")
    col1, col2, col3 = st.columns(3)
    with col1:
        total_exportacion_usd = df_filtrado['Valor_Exportacion_USD'].sum()
        st.metric(label="Valor Total de Exportación", value=f"${total_exportacion_usd:,.2f}")
    with col2:
        total_cantidad_kg = df_filtrado['Cantidad_KG'].sum()
        st.metric(label="Cantidad Total Exportada", value=f"{total_cantidad_kg:,.2f} KG")
    with col3:
        num_registros = len(df_filtrado)
        st.metric(label="Número de Registros", value=num_registros)

# Información adicional
st.sidebar.markdown("---")
st.sidebar.info("Este dashboard es un ejemplo. Puedes personalizarlo con tus propios datos y visualizaciones.")
