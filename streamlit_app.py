import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import math
from pathlib import Path


# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Telecomunicaciones en Argentina',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------

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
data_mapa = pd.read_excel('./data/mapa_conectividad.xlsx')

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        color: #DCDCDC;  
        font-size: 64px; 
        font-weight: bold; 
    }
    </style>
    <div class="title">Reporte de Conexiones a Internet en Argentina</div></br>
    """,
    unsafe_allow_html=True
)

# Función para calcular el total de habitantes con acceso a internet
def calcular_habitantes_con_conexion(df):
    # Sumamos la cantidad de accesos por cada 100 habitantes
    total_accesos_habitantes = df['Accesos por cada 100 hab'].sum()
    # Aquí asumimos que el total de habitantes es proporcionado por otro dataframe o es calculado
    # Por simplicidad, aquí solo mostramos el total de accesos (modifica esto según tus datos)
    return total_accesos_habitantes

# Función para calcular el total de hogares con acceso a internet
def calcular_hogares_con_conexion(df):
    # Sumamos la cantidad de accesos por cada 100 hogares
    total_accesos_hogares = df['Accesos por cada 100 hogares'].sum()
    # Aquí asumimos que el total de hogares es proporcionado por otro dataframe o es calculado
    # Por simplicidad, aquí solo mostramos el total de accesos (modifica esto según tus datos)
    return total_accesos_hogares

# Cálculo de totales
total_habitantes_con_conexion = calcular_habitantes_con_conexion(df)
total_hogares_con_conexion = calcular_hogares_con_conexion(df)

# Crear gráficos con Plotly
fig_habitantes = go.Figure()
fig_habitantes.add_trace(go.Indicator(
    mode="number",
    value=total_habitantes_con_conexion,
    title={"text": "Habitantes con Acceso a Internet"},
    number={'font': {'size': 60, 'color': '#2e8b57'}},
    domain={'x': [0.2, 0.8], 'y': [0.5, 0.8]},
    title_font_color="#4682b4"
))

fig_hogares = go.Figure()
fig_hogares.add_trace(go.Indicator(
    mode="number",
    value=total_hogares_con_conexion,
    title={"text": "Hogares con Acceso a Internet"},
    number={'font': {'size': 60, 'color': '#ff6347'}},
    domain={'x': [0.2, 0.8], 'y': [0.5, 0.8]},
    title_font_color="#4682b4"
))

# Mostrar gráficos en Streamlit
col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(fig_habitantes)
with col2:
    st.markdown(
        """
        <style>
        .center-image {
            display: flex;
            justify-content: center; /* Centra horizontalmente */
            align-items: center; /* Centra verticalmente */
            height: 400px; /* Ajusta según el tamaño deseado */
        }
        .center-image img {
            max-width: 100%; /* Ajusta la imagen para que no exceda el contenedor */
            max-height: 100%; /* Ajusta la imagen para que no exceda el contenedor */
        }
        </style>
        <div class="center-image">
            <img src="https://cdn.wallpapersafari.com/36/86/wfz7dH.jpg" alt="Imagen de Conexiones">
        </div>
        """,
        unsafe_allow_html=True
    )
with col3:
    st.plotly_chart(fig_hogares)

# Agrupar y promediar solo las columnas numéricas en mapa
mapa_grouped = data_mapa.groupby('Provincia').agg({
    'Latitud': 'mean',
    'Longitud': 'mean'
}).reset_index()
# Combinar los DataFrames
combined_df = pd.merge(df, mapa_grouped, on='Provincia')
# Crear el mapa
fig_map = px.scatter_geo(combined_df,
                        lat='Latitud',
                        lon='Longitud',
                        size='Accesos_por_100_habitantes',
                        color='Accesos_por_100_hogares',
                        hover_name='Provincia',
                        size_max=50,
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title="Accesos de Internet por Provincia en Argentina")

# Crear los gráficos de barras
fig_bar_habitantes = px.bar(combined_df,
                           x='Provincia',
                           y='Accesos_por_100_habitantes',
                           title="Accesos a Internet por Cada 100 Habitantes",
                           labels={'Accesos_por_100_habitantes': 'Accesos por 100 Habitantes'})

fig_bar_hogares = px.bar(combined_df,
                        x='Provincia',
                        y='Accesos_por_100_hogares',
                        title="Accesos a Internet por Cada 100 Hogares",
                        labels={'Accesos_por_100_hogares': 'Accesos por 100 Hogares'})

# Aplicación Streamlit
def main():
    st.title("Penetración de Internet en Provincias de Argentina")

    # Muestra el mapa
    st.header("Mapa de Penetración de Internet")
    st.plotly_chart(fig_map)

    # Muestra los gráficos de barras
    st.header("Accesos a Internet por Cada 100 Habitantes")
    st.plotly_chart(fig_bar_habitantes)

    st.header("Accesos a Internet por Cada 100 Hogares")
    st.plotly_chart(fig_bar_hogares)

if __name__ == "__main__":
    main()

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

#----------------------------------------------------------------------------------------------

# Selector de Provincias
provincias = df['Provincia'].unique()
selected_provincia = st.sidebar.selectbox('Selecciona una Provincia', provincias)

# Selector de Año y Trimestre
años = df['Año'].unique()
selected_año = st.sidebar.selectbox('Selecciona un Año', años)
trimestres = df['Trimestre'].unique()
selected_trimestre = st.sidebar.selectbox('Selecciona un Trimestre', trimestres)

# Filtros de datos
filtered_df = df[(df['Provincia'] == selected_provincia) & 
                 (df['Año'] == selected_año) & 
                 (df['Trimestre'] == selected_trimestre)]

# Mostrar los datos seleccionados
st.subheader('Datos Filtrados')
st.write(filtered_df)

# Gráficos
st.subheader('Distribución de Conexiones por Velocidad')
st.bar_chart(filtered_df[['0-10 Mbps', '+10-25 Mbps', '+25-50 Mbps', '+50-100 Mbps', '+100-250 Mbps', '+250-500 Mbps', '+500-1000 Mbps', '+1000-5000 Mbps', '+5000 Mbps']].sum())

st.subheader('Penetración de Internet por Habitante y Hogares')
st.line_chart(filtered_df[['Accesos por cada 100 hab', 'Accesos por cada 100 hogares']])

# Datos Totales
st.subheader('Datos Totales Nacionales')
st.write(df_totales)

# Datos de Localidades
localidades_filtered = df_localidades[df_localidades['Provincia'] == selected_provincia]
st.subheader('Datos por Localidades')
st.write(localidades_filtered)

