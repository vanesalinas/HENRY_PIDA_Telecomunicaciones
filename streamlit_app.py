import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
from pathlib import Path


# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Telecomunicaciones en Argentina',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_data():
 
    DATA_FILENAME1 = Path(__file__).parent/'data/df.csv'
    data1 = pd.read_csv(DATA_FILENAME1)

    DATA_FILENAME2 = Path(__file__).parent/'data/df_totales.csv'
    data2 = pd.read_csv(DATA_FILENAME2)

    DATA_FILENAME3 = Path(__file__).parent/'data/df_localidades.csv'
    data3 = pd.read_csv(DATA_FILENAME3)

    MIN_YEAR = 2014
    MAX_YEAR = 2024

    return data1, data2, data3

df, df_totales, df_localidades = get_data()

# Título del dashboard
st.title('Consumo de Internet en Argentina')

# Mostrar DataFrame 1
st.subheader('Datos del Archivo CSV 1')
st.write(df)

# Mostrar DataFrame 2
st.subheader('Datos del Archivo CSV 2')
st.write(df_totales)

# Mostrar DataFrame 3
st.subheader('Datos del Archivo CSV 3')
st.write(df_localidades)
