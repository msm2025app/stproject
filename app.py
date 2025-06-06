import streamlit as st
import pandas as pd
import gdown
import os

st.set_page_config(page_title="buscaproductomsm", layout="wide")

st.title("🧠 Buscador de Datos MSM")

# ID del archivo en Google Drive
FILE_ID = "1RDXUkcZkto1Xp93aZkTtFiIq7F1aEAWE"

# URL de descarga directa
url = f"https://drive.google.com/uc?id={FILE_ID}"

# Nombre temporal del archivo descargado
downloaded_file = "datos_csv.app"

@st.cache_data
def cargar_datos(url):
    gdown.download(url, downloaded_file, quiet=False)
    try:
        df = pd.read_csv(downloaded_file, sep=",", encoding="utf-8")
        return df
    except Exception as e:
        st.error(f"Error al cargar archivo: {e}")
        return None
    
df = cargar_datos(url)

if df is not None:
    st.success("Datos cargados correctamente.")
    st.dataframe(df.head())
else:
    st.warning("No se pudieron cargar los datos.")

