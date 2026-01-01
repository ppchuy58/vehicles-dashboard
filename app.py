import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración página
st.set_page_config(page_title="Vehicles Dashboard", layout="wide")

# Título
st.header("🚗 Dashboard Análisis Vehículos US")
st.markdown("---")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

car_data = load_data()
st.write(f"📊 Datos cargados: **{len(car_data):,}** registros")

# Sidebar filtros (opcional extra)
st.sidebar.header("Filtros")
max_price = st.sidebar.slider("Precio máximo", 0, int(car_data['price'].max()), 50000)

# Filtrar datos
filtered_data = car_data[car_data['price'] <= max_price]

# Checkbox interactivos
col1, col2 = st.columns(2)

with col1:
    show_histogram = st.checkbox("📈 Histograma Odometer", value=True)
    
with col2:
    show_scatter = st.checkbox("📉 Precio vs Odometer", value=True)

# Histograma
if show_histogram:
    st.subheader("Histograma Odometer")
    fig_hist = px.histogram(filtered_data, x="odometer", nbins=50, 
                           title="Distribución Kilometraje")
    st.plotly_chart(fig_hist, use_container_width=True)

# Scatter
if show_scatter:
    st.subheader("Precio vs Kilometraje")
    fig_scatter = px.scatter(filtered_data, x="odometer", y="price",
                           hover_data=["make", "model"],
                           title="Relación Precio-Kilometraje")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Estadísticas
col1, col2, col3 = st.columns(3)
col1.metric("Precio Promedio", f"${filtered_data['price'].mean():,.0f}")
col2.metric("Odometer Promedio", f"{filtered_data['odometer'].mean():,.0f} millas")
col3.metric("Autos Disponibles", f"{len(filtered_data):,}")

