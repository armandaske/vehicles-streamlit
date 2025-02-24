"""
Este código implementa una aplicación web usando Streamlit para crear una interfaz gráfica
donde el usuario puede interactuar con distintos gráficos para analizar las tendencias 
y las diferentes características de autos vendidos en los Estados Unidos
"""

import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.title('¡Bienvenido!\nElige una opción para analizar las tendencias de venta de autos')
st.write('\n')  # Dejar una separación entre título y casillas de verificación

# crear casillas de verificación
build_histogram = st.checkbox('Construir un histograma para años de los autos')
build_scatter = st.checkbox(
    'Construir un gráfico de dispersión entre odómetro y precio de venta')
build_bar_plot = st.checkbox(
    'Construir un gráfico de barras para el tipo de auto')

st.write('\n')  # Dejar una separación entre casillas y gráficos

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Distribución de años de autos')

    # crear un histograma
    fig = px.histogram(car_data, x="model_year")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Relación entre el odómetro y el precio de venta')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

if build_bar_plot:
    st.write('Distribución de tipo de vehículo')

    # crear un countplot
    fig = px.histogram(car_data, x="type")
    st.plotly_chart(fig, use_container_width=True)
