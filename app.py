import streamlit as st
import pandas as pd
import numpy as np

st.title("¡Mi primera app con Streamlit! 🚀")
st.write("Hola, soy Jose de Jesus C, y esta es mi app del Proyecto Final Sprint 7")

# Ejemplo rápido
data = pd.DataFrame({
    'x': np.arange(0, 10),
    'sin': np.sin(np.arange(0, 10)),
    'cos': np.cos(np.arange(0, 10))
})
st.line_chart(data)