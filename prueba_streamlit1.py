import streamlit as st
import pandas as pd

st.write("Mi Primer Página Web jeje")
st.write("Página de prueba")

#Creación de un botón de carga
st.write("Para ver la información de la tabla presione aquí:")
Boton_Carga = st.button("Ver Tabla")
if Boton_Carga:
    st.write(pd.DataFrame({
    'Lugares':[1,2,3,4,5,6],
    'Cantidades':[10,20,20,10,15,5]
    }))
    Boton_Cierre = st.button("Ocultar Tabla")
    if Boton_Cierre:
        Boton_Carga = None
st.write("Very Good!")




