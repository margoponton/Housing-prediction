import streamlit as st
import pandas as pd
import joblib


st.set_page_config(page_title="Predicción de Precio de Vivienda")

st.title("🏠 Predicción de Precio Mediano de Vivienda")

st.write("Ingrese los valores de las características de la vivienda:")

# Entradas del usuario
longitud = st.number_input("Longitud", value=-122.23)
latitud = st.number_input("Latitud", value=37.88)

edad_mediana_vivienda = st.slider(
    "Edad Mediana de la Vivienda",
    min_value=1,
    max_value=100,
    value=25
)

total_habitaciones = st.number_input(
    "Total Habitaciones",
    min_value=1,
    value=2000
)

total_dormitorios = st.number_input(
    "Total Dormitorios",
    min_value=1,
    value=400
)

poblacion = st.number_input(
    "Población",
    min_value=1,
    value=1000
)

hogares = st.number_input(
    "Hogares",
    min_value=1,
    value=350
)

ingreso_mediano = st.number_input(
    "Ingreso Mediano",
    min_value=0.0,
    value=4.5,
    step=0.1
)

proximidad_oceano = st.selectbox(
    "Proximidad al Océano",
    [
        "<1H OCEAN",
        "INLAND",
        "NEAR OCEAN",
        "NEAR BAY",
        "ISLAND"
    ]
)

# Crear DataFrame
datos = pd.DataFrame({
    "longitud": [longitud],
    "latitud": [latitud],
    "edad_mediana_vivienda": [edad_mediana_vivienda],
    "total_habitaciones": [total_habitaciones],
    "total_dormitorios": [total_dormitorios],
    "poblacion": [poblacion],
    "hogares": [hogares],
    "ingreso_mediano": [ingreso_mediano],
    "proximidad_oceano": [proximidad_oceano]
})

# Botón de predicción
if st.button("Predecir"):
    prediccion = modelo.predict(datos)[0]

    st.success(
        f"💰 Precio Mediano Estimado de la Vivienda: ${prediccion:,.2f}"
    )

    st.subheader("Datos ingresados")
    st.dataframe(datos)
