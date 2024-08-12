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

# Agregar un selector de provincias
provincia = st.selectbox('Selecciona una provincia', df_localidades['Provincia'].unique())
# Filtrar los datos por provincia
df_filtrado = df_localidades[df_localidades['Provincia'] == provincia]
# Agrupar los datos por tecnología y sumar los valores
totales_por_tecnologia = df_filtrado[['ADSL', 'CABLEMODEM', 'DIAL UP', 'FIBRA OPTICA',
                                    'SATELITAL', 'WIMAX', 'WIRELESS', 'Otras_Tecnologias']].sum()
# Definir umbral (ajusta según tus necesidades)
umbral = 1
# Obtener las categorías con un porcentaje mayor al umbral
categorias_significativas = totales_por_tecnologia[totales_por_tecnologia > totales_por_tecnologia.sum() * umbral / 100].index
# Crear la categoría "Otros"
otros = totales_por_tecnologia[~totales_por_tecnologia.index.isin(categorias_significativas)].sum()
totales_por_tecnologia['Otros'] = otros
# Eliminar las categorías menores del DataFrame
totales_por_tecnologia = totales_por_tecnologia[categorias_significativas.tolist() + ['Otros']]
# Creando el gráfico circular
fig, ax = plt.subplots()
# Crear el gráfico circular con colores aleatorios y etiquetas
ax.pie(totales_por_tecnologia, labels=totales_por_tecnologia.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(totales_por_tecnologia))), startangle=140)
ax.axis('equal')
# Agregar título al gráfico
plt.title('Distribución de tecnologías de conexión')
# Mostrar el gráfico en Streamlit
st.pyplot(fig)