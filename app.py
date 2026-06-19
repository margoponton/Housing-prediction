import streamlit as st
import pandas as pd
import joblib
import os

st.title("Housing Prediction")

# Cargar modelo
@st.cache_resource
def load_model():
    model_path = "modelo.pkl"
    if not os.path.exists(model_path):
        st.error(f"No se encontro el archivo {model_path} en el repositorio.")
        st.info("Asegurese de subir el archivo modelo.pkl a GitHub")
        st.stop()
    try:
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        st.stop()

model = load_model()
st.success("Modelo cargado correctamente")

# Inputs del usuario
st.header("Ingrese los datos de la vivienda")

col1, col2 = st.columns(2)

with col1:
    crim = st.number_input("CRIM (Tasa de criminalidad)", value=0.0, format="%.4f")
    zn = st.number_input("ZN (Zonas residenciales)", value=0.0, format="%.2f")
    indus = st.number_input("INDUS (Proporcion industrial)", value=0.0, format="%.2f")
    chas = st.number_input("CHAS (Cerca del rio)", min_value=0, max_value=1, value=0)
    nox = st.number_input("NOX (Concentracion de oxido nitrico)", value=0.0, format="%.4f")

with col2:
    rm = st.number_input("RM (Habitaciones promedio)", value=6.0, format="%.2f")
    age = st.number_input("AGE (Edad de las viviendas)", value=0.0, format="%.2f")
    dis = st.number_input("DIS (Distancia a centros de empleo)", value=0.0, format="%.4f")
    rad = st.number_input("RAD (Accesibilidad a autopistas)", value=0)
    tax = st.number_input("TAX (Impuesto por propiedad)", value=0.0, format="%.2f")

lstat = st.number_input("LSTAT (% poblacion de bajo nivel)", value=0.0, format="%.2f")

if st.button("Predecir Precio"):
    input_data = pd.DataFrame({
        'CRIM': [crim],
        'ZN': [zn],
        'INDUS': [indus],
        'CHAS': [chas],
        'NOX': [nox],
        'RM': [rm],
        'AGE': [age],
        'DIS': [dis],
        'RAD': [rad],
        'TAX': [tax],
        'LSTAT': [lstat]
        # Agrega aqui las demas columnas que necesita tu modelo si faltan
    })
    
    prediction = model.predict(input_data)
    st.success(f"Precio estimado: {prediction[0]:,.2f}")

