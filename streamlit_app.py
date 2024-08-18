import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
import plotly.graph_objects as go
import math
from pathlib import Path


# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Telecomunicaciones en Argentina',
    page_icon='⚡',
    layout="wide"
)

st.markdown("""
    <style>
    /* Fondo negro para el contenedor principal */
    .reportview-container {
        background-color: #000000; /* Color de fondo negro */
        color: #FFFFFF; /* Color del texto blanco para el contenido principal */
    }
    
    /* Fondo negro para la barra lateral */
    .css-1d391kg {
        background-color: #000000; /* Fondo negro para la barra lateral */
        color: #FFFFFF; /* Color del texto blanco en la barra lateral */
    }
    
    /* Fondo negro para los encabezados */
    .css-1v0mbdj {
        color: #FFFFFF; /* Color del texto blanco en los encabezados */
    }
    
    /* Ajustar el color del texto en los widgets */
    .css-1aumxhk {
        color: #FFFFFF; /* Color del texto blanco en los widgets */
    }
    
    /* Ajustar el color de los botones */
    .css-1n5o6dz {
        background-color: #333333; /* Fondo oscuro para los botones */
        color: #FFFFFF; /* Texto blanco en los botones */
    }
    </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------

@st.cache_data
def get_data():
 
    DATA_FILENAME1 = Path(__file__).parent/'data/df.csv'
    data1 = pd.read_csv(DATA_FILENAME1)

    DATA_FILENAME2 = Path(__file__).parent/'data/df_totales.csv'
    data2 = pd.read_csv(DATA_FILENAME2)

    DATA_FILENAME3 = Path(__file__).parent/'data/df_localidades.csv'
    data3 = pd.read_csv(DATA_FILENAME3)

    MIN = 2014
    MAX = 2024
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
    .subtitle {
        text-align: center;
        color: #DCDCDC;  
        font-size: 30px; 
        font-weight: bold; 
    }
    </style>
    <div class="title">UN VIAJE A TRAVES DE LA CONECTIVIDAD EN ARGENTINA</div></br>
    <div class="subtitle">El panorama de Internet en el pais</div></br>
    """,
    unsafe_allow_html=True
)

# Datos proporcionados por Indec segun censo 2022
poblacion_total = 46234830
total_viviendas = 17794949

# Filtrar datos para el primer trimestre de 2024
df_trimestre_2024_q1 = df_totales[(df_totales['Año'] == 2024) & (df_totales['Trimestre'] == 1)]

# Verificar que hay datos para el trimestre seleccionado
if df_trimestre_2024_q1.empty:
    print("No hay datos para el primer trimestre de 2024.")
else:
    # Calcular el número total de personas con acceso a Internet para el primer trimestre de 2024
    total_habitantes_con_conexion = (df_trimestre_2024_q1['Accesos por cada 100 hab'] / 100 * poblacion_total).sum()
    
    # Calcular el número total de hogares con acceso a Internet para el primer trimestre de 2024
    total_hogares_con_conexion = (df_trimestre_2024_q1['Accesos por cada 100 hogares'] / 100 * total_viviendas).sum()

# Calcular provincias y localidades únicas
num_provincias = df_localidades['Provincia'].nunique()
num_localidades = df_localidades['Localidad'].nunique()

# Crear gráficos con Plotly
fig_habitantes = go.Figure()
fig_habitantes.add_trace(go.Indicator(
    mode="number",
    value=total_habitantes_con_conexion,
    title={"text": "Habitantes con Acceso a Internet"},
    number={'font': {'size': 60, 'color': '#FFD700'}},
    domain={'x': [0.2, 0.8], 'y': [0.1, 0]},
    title_font_color="#87CEFA"
))
# Ajustar el diseño del gráfico
fig_habitantes.update_layout(
    margin=dict(l=20, r=20, t=0, b=0),  # Reducir márgenes
    height=300  # Ajustar altura total del gráfico
)

fig_hogares = go.Figure()
fig_hogares.add_trace(go.Indicator(
    mode="number",
    value=total_hogares_con_conexion,
    title={"text": "Hogares con Acceso a Internet"},
    number={'font': {'size': 60, 'color': '#7FFF00'}},
    domain={'x': [0.2, 0.8], 'y': [0.1, 0]},
    title_font_color="#87CEFA"
))
# Ajustar el diseño del gráfico
fig_hogares.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),  # Reducir márgenes
    height=300  # Ajustar altura total del gráfico
)

fig_provincias = go.Figure()
fig_provincias.add_trace(go.Indicator(
    mode="number",
    value=num_provincias,
    title={"text": "Provincias con Acceso a Internet"},
    number={'font': {'size': 60, 'color': '#00CED1'}},
    domain={'x': [0.2, 0.8], 'y': [0.1, 0]},
    title_font_color="#87CEFA"
))
# Añadir texto adicional (subtítulo)
fig_provincias.add_annotation(
    text="de 24 Jurisdicciones",
    x=0.5,  # Centrar horizontalmente
    y=0.25,  # Posicionar verticalmente debajo del número
    showarrow=False,  # No mostrar flecha
    font=dict(size=20, color="#00CED1"),  # Ajusta el tamaño y color del texto
    xref="paper",
    yref="paper"
)
# Ajustar el diseño del gráfico
fig_provincias.update_layout(
    margin=dict(l=30, r=30, t=0, b=30),  # Reducir márgenes
    height=300  # Ajustar altura total del gráfico
)

fig_localidades = go.Figure()
fig_localidades.add_trace(go.Indicator(
    mode="number",
    value=num_localidades,
    title={"text": "Localidades con Acceso a Internet"},
    number={'font': {'size': 60, 'color': '#FF6347'}},
    domain={'x': [0.2, 0.8], 'y': [0.1, 0]},
    title_font_color="#87CEFA"
))
# Ajustar el diseño del gráfico
fig_localidades.update_layout(
    margin=dict(l=20, r=20, t=0, b=20),  # Reducir márgenes
    height=300  # Ajustar altura total del gráfico
)

# Mostrar gráficos en Streamlit
col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(fig_habitantes, use_container_width=True)
    st.plotly_chart(fig_provincias, use_container_width=True)
with col2:
    st.markdown(
        """
        <style>
        .center-image {
            display: flex;
            justify-content: center; /* Centra horizontalmente */
            align-items: center; /* Centra verticalmente */
            height: 100%; /* Ajusta la altura del contenedor para centrado vertical */
            width: 100%; /* Asegúrate de que el contenedor ocupe el ancho completo */
        }
        </style>
        <div class="center-image">
            <img src="https://canalprovincial.com.ar/wp-content/uploads/2019/01/Rep%C3%BAblica_Argentina_mapa_aleg%C3%B3rico.png" alt="Imagen de Conexiones">
        </div>
        """,
        unsafe_allow_html=True
    )
with col3:
    st.plotly_chart(fig_hogares)
    st.plotly_chart(fig_localidades)

#----------------------------------------------------------------------------------------------

# Aplicar la transformación solo a la columna 'Provincia'
df['Provincia'] = df['Provincia'].str.upper()
# Agrupar y promediar solo las columnas numéricas en mapa
mapa_grouped = data_mapa.groupby('Provincia').agg({
    'Latitud': 'mean',
    'Longitud': 'mean'
}).reset_index()
# Combinar los DataFrames
combined_df = pd.merge(df, mapa_grouped, on='Provincia')

#----------------------------------------------------------------------------------------------

# Selector de Provincias, año y trimestre
provincias = combined_df['Provincia'].unique()
provincias = ['Todos'] + list(provincias)
selected_provincia = st.sidebar.selectbox('Selecciona una Provincia', provincias)

años = combined_df['Año'].unique()
selected_año = st.sidebar.selectbox('Selecciona un Año', años)

trimestres = combined_df['Trimestre'].unique()
selected_trimestre = st.sidebar.selectbox('Selecciona un Trimestre', trimestres)

# Filtros de datos
if selected_provincia == 'Todos':
    filtered_df = combined_df
else:
    filtered_df = combined_df[(combined_df['Provincia'] == selected_provincia) & 
                              (combined_df['Año'] == selected_año) & 
                              (combined_df['Trimestre'] == selected_trimestre)]

#----------------------------------------------------------------------------------------------

def create_map(df, provincia, año, trimestre):
    """
    Crea un mapa interactivo usando Plotly Express.

    Args:
        df (pd.DataFrame): DataFrame con los datos para graficar.
        provincia (str): Provincia seleccionada.
        año (int): Año seleccionado.
        trimestre (str): Trimestre seleccionado.

    Returns:
        fig_map (plotly.graph_objects.Figure): Mapa generado.
    """
    fig_map = px.scatter_geo(df,
                            lat='Latitud',
                            lon='Longitud',
                            size='Accesos por cada 100 hab',
                            color='Accesos por cada 100 hogares',
                            hover_name='Provincia',
                            size_max=30,
                            color_continuous_scale=px.colors.sequential.Plasma,
                            title=f"Accesos de Internet en {provincia} ({año} - {trimestre})",
                            projection="natural earth")
    return fig_map

def create_bar_charts(df, provincia, año, trimestre):
    """
    Crea gráficos de barras para accesos por cada 100 habitantes y hogares.

    Args:
        df (pd.DataFrame): DataFrame con los datos para graficar.
        provincia (str): Provincia seleccionada.
        año (int): Año seleccionado.
        trimestre (str): Trimestre seleccionado.

    Returns:
        tuple: Gráficos de barras para cada 100 habitantes y hogares.
    """
     # Ordenar los datos de mayor a menor
    df_sorted_habitantes = df.sort_values(by='Accesos por cada 100 hab', ascending=True)
    df_sorted_hogares = df.sort_values(by='Accesos por cada 100 hogares', ascending=True)
    
    # Gráfico de barras horizontales para "Accesos por cada 100 habitantes"
    fig_bar_habitantes = px.bar(df_sorted_habitantes,
                               x='Accesos por cada 100 hab',
                               y='Provincia',
                               title=f"Accesos a Internet por Cada 100 Habitantes en {provincia} ({año} - {trimestre})",
                               labels={'Accesos por cada 100 hab': 'Accesos por cada 100 Hab'},
                               orientation='h')
    
    # Gráfico de barras horizontales para "Accesos por cada 100 hogares"
    fig_bar_hogares = px.bar(df_sorted_hogares,
                            x='Accesos por cada 100 hogares',
                            y='Provincia',
                            title=f"Accesos a Internet por Cada 100 Hogares en {provincia} ({año} - {trimestre})",
                            labels={'Accesos por cada 100 hogares': 'Accesos por cada 100 Hogares'},
                            orientation='h')
    
    return fig_bar_habitantes, fig_bar_hogares

#----------------------------------------------------------------------------------------------

# Agregar lógica para mostrar datos agregados si 'Todos' está seleccionado
if selected_provincia == 'Todos':
    # Agrupar los datos por provincia y calcular el promedio
    filtered_df_todos = combined_df.groupby(['Provincia', 'Latitud', 'Longitud']).agg({
        'Accesos por cada 100 hab': 'mean',
        'Accesos por cada 100 hogares': 'mean'
        }).reset_index()
    fig_map = create_map(filtered_df_todos, selected_provincia, selected_año, selected_trimestre)
    fig_bar_habitantes, fig_bar_hogares = create_bar_charts(filtered_df_todos, selected_provincia, selected_año, selected_trimestre)
else:
    fig_map = create_map(filtered_df, selected_provincia, selected_año, selected_trimestre)
    fig_bar_habitantes, fig_bar_hogares = create_bar_charts(filtered_df, selected_provincia, selected_año, selected_trimestre)

# Muestra el mapa
# Aplicación Streamlit
def main():
    st.title("Penetración de Internet en Provincias de Argentina")
    st.header("Mapa de Penetración de Internet")
    st.plotly_chart(fig_map)

    # Muestra los gráficos de barras
    st.header("Accesos a Internet por Cada 100 Habitantes")
    st.plotly_chart(fig_bar_habitantes)

    st.header("Accesos a Internet por Cada 100 Hogares")
    st.plotly_chart(fig_bar_hogares)

if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------------------------

# Agrupar por Año y calcular el promedio
df_totales_agrupado = df_totales.groupby(['Año']).agg({
    'Accesos por cada 100 hab': 'mean',
    'Accesos por cada 100 hogares': 'mean'
}).reset_index()

# Crear el gráfico de líneas
fig, ax = plt.subplots(figsize=(14, 7))

# Graficar accesos por cada 100 habitantes
ax.plot(df_totales_agrupado['Año'], df_totales_agrupado['Accesos por cada 100 hab'], marker='o', label='Accesos por cada 100 hab')

# Graficar accesos por cada 100 hogares
ax.plot(df_totales_agrupado['Año'], df_totales_agrupado['Accesos por cada 100 hogares'], marker='o', label='Accesos por cada 100 hogares')

# Añadir título y etiquetas
ax.set_title('Penetración de Internet en Argentina (Nivel Nacional)')
ax.set_xlabel('Año')
ax.set_ylabel('Accesos por cada 100')
ax.legend(title='Metricas')
ax.grid(True)

# Ajustar el layout
plt.tight_layout()

# Mostrar gráfico en Streamlit
st.pyplot(fig)

#----------------------------------------------------------------------------------------------

# Gráficos
st.subheader('Distribución de Conexiones por Velocidad')
st.bar_chart(filtered_df[['0-10 Mbps', '+10-25 Mbps', '+25-50 Mbps', '+50-100 Mbps', '+100-250 Mbps', '+250-500 Mbps', '+500-1000 Mbps', '+1000-5000 Mbps', '+5000 Mbps']].sum())

#----------------------------------------------------------------------------------------------

# Agrupar los datos por tecnología y sumar los valores
totales_por_tecnologia = filtered_df[['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless',
                                    'Otras_Tecnologias']].sum()

# Creando el gráfico circular
fig, ax = plt.subplots(figsize=(4, 4))  # Tamaño ajustado

# Crear el gráfico circular
ax.pie(totales_por_tecnologia, 
       labels=totales_por_tecnologia.index, 
       autopct='%1.1f%%', 
       colors=plt.cm.Paired(range(len(totales_por_tecnologia))), 
       startangle=140,
       labeldistance=0.75)  # Ajustar la distancia de las etiquetas

# Configurar el fondo del gráfico
fig.patch.set_facecolor('none')  # Fondo transparente para la figura
ax.set_facecolor('none')  # Fondo transparente para los ejes

# Configurar la visibilidad de bordes y espaciado
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

# Mostrar el gráfico en Streamlit
st.title('Distribución de tecnologías de conexión')
st.pyplot(fig)

#----------------------------------------------------------------------------------------------

# Crear una columna combinada para Año y Trimestre
df_totales['Año-Trimestre'] = df_totales['Año'].astype(str) + '-' + df_totales['Trimestre'].astype(str)

conexiones_por_periodo = df_totales.groupby('Año-Trimestre').agg({
    'ADSL': 'sum',
    'Cablemodem': 'sum',
    'Fibra óptica': 'sum',
    'Wireless': 'sum',
    'Otros': 'sum'
}).reset_index()

# Configurar el gráfico
plt.figure(figsize=(14, 8))

# Graficar la evolución para cada tecnología
for tecnologia in ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']:
    plt.plot(conexiones_por_periodo['Año-Trimestre'], conexiones_por_periodo[tecnologia], marker='o', linestyle='-', label=tecnologia)

# Añadir título y etiquetas
plt.title('Evolución de Conexiones por Tecnología')
plt.xlabel('Año-Trimestre')
plt.ylabel('Cantidad de Conexiones')
plt.xticks(rotation=45, ha='right')  # Rote las etiquetas para mejorar la visibilidad
plt.legend(title='Tecnología')
plt.grid(True)

# Ajustar el diseño
plt.tight_layout()

# Crear la interfaz de Streamlit
st.title('Visualización de Conexiones por Tecnología')
st.pyplot(plt)  # Mostrar el gráfico en Streamlit

#----------------------------------------------------------------------------------------------

# Ordenar el DataFrame por Año-Trimestre para asegurar que las líneas se dibujen en el orden correcto
df_totales = df_totales.sort_values('Año-Trimestre')

# Configurar el gráfico de línea
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar los ingresos por trimestre
ax.plot(df_totales['Año-Trimestre'], df_totales['Ingresos (miles de pesos)'], marker='o', linestyle='-', color='b')

# Configurar el gráfico
ax.set_title(f'Evolución de Ingresos por Trimestre')
ax.set_xlabel('Trimestre')
ax.set_ylabel('Ingresos (miles de pesos)')
ax.grid(True)

# Mostrar el gráfico en Streamlit
st.title('Evolucion de ingresos en el tiempo')
st.pyplot(fig)

#----------------------------------------------------------------------------------------------

# Filtrar el DataFrame para el trimestre actual y el siguiente trimestre
df_current = df[df['Año'] == 2023]
df_next = df[df['Año'] == 2024]

# Asegúrate de que los datos estén alineados correctamente para la comparación
df_comparison = pd.merge(df_current, df_next, on='Provincia', suffixes=('_current', '_next'))

# Calcular el KPI propuesto
df_comparison['KPI (%)'] = ((df_comparison['Accesos por cada 100 hogares_next'] - df_comparison['Accesos por cada 100 hogares_current']) / df_comparison['Accesos por cada 100 hogares_current']) * 100

# Calcular la Tasa de Penetración
# Para simplificar, usamos la misma columna de accesos por cada 100 hogares
df_comparison['Tasa de Penetración (%)'] = df_comparison['Accesos por cada 100 hogares_current']

# Calcular el Crecimiento Anual
# Para simplificar, usamos el crecimiento entre el trimestre actual y el mismo trimestre del año anterior
df_comparison['Crecimiento Anual (%)'] = ((df_comparison['Accesos por cada 100 hogares_next'] - df_comparison['Accesos por cada 100 hogares_current']) / df_comparison['Accesos por cada 100 hogares_current']) * 100

# Configurar el dashboard
st.title('KPIs')

# KPI Propuesto
st.header('KPI: Aumento del Acceso al Servicio de Internet')
st.subheader('Aumentar en un 2% el acceso al servicio de internet para el próximo trimestre, cada 100 hogares, por provincia.')
st.write(df_comparison[['Provincia', 'KPI (%)']])

# Graficar el KPI Propuesto
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_comparison['Provincia'], df_comparison['KPI (%)'], color='skyblue')
ax.set_title('KPI: Aumento en el Acceso a Internet por Provincia')
ax.set_xlabel('Provincia')
ax.set_ylabel('Aumento (%)')
plt.xticks(rotation=45)
st.pyplot(fig)

#----------------------------------------------------------------------------------------------

# Mostrar los datos seleccionados
st.subheader('Datos Filtrados')
st.write(filtered_df)
# Mostrar DataFrame Mapa
st.subheader('Mapa de conectividad')
st.write(data_mapa)
st.subheader('DF')
st.write(df)
st.subheader('combined_df')
st.write(combined_df)
# Datos Totales
st.subheader('Datos Totales Nacionales')
st.write(df_totales)
# Datos de Localidades
localidades_filtered = df_localidades[df_localidades['Provincia'] == selected_provincia]
st.subheader('Datos por Localidades')
st.write(localidades_filtered)
# Mostrar DataFrame 2
st.subheader('Datos del Archivo CSV 2')
st.write(df_totales)
# Mostrar DataFrame 3
st.subheader('Datos del Archivo CSV 3')
st.write(df_localidades)
