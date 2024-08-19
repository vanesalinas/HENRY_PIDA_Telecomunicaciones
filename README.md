# <h1 align=center> **Telecomunicaciones en Argentina** </h1>
<p align="center"><img src='/src/img/descarga.jpeg'></p>

## <p align="center">PROYECTO INDIVIDUAL Nº2<br/>SOY HENRY DATA-PT09</p>

### Tabla de contenido
+	Estructura del repositorio.
+	Contexto.
+	Tecnologías utilizadas
+	Objetivo.
+	Introducción.
+	Análisis exploratorio de los datos (EDA).
+	Evolución del acceso a internet.
+	Velocidades de conexión.
+	Tecnologías.
+	Ingresos del sector.
+	KPIs.
+	Recomendaciones y conclusiones.
+	Dashboard.

### Estructura del repositorio ###

En este repositorio encontrarás los siguientes archivos:

+ .devcontainer: Carpeta donde se almacenan los datos cache de Python para mejorar su proceso de ejecución.
+ .github:
+ .streamlit:
+ Data: carpeta donde se encuentran las fuentes de datos utilizadas.
+ Notebook: Carpeta que almacena los archivos para el ETL y el EDA.
+ src: carpeta que almacena imagenes que se encuentran en el repositorio.
+ .gitignore: archivo que indica lo que no debe ser rastreado por git
+ LICENCE: 
+ README.md: archivo con el readme del proyecto donde podras ver la presentacion del mismo.
+ requirements.txt: librerias requeridas para el deploy en Streamlit

### Contexto

<p align="justify">Las telecomunicaciones se refieren al conjunto de tecnologias y sistemas que pemriten la transmision y recepcion de informacion a distancia. Dentro de las telecomunicaciones podemos encontrar numerosas tecnologias, desde la radio, television, telefonia, redes informaticas e internet, hasta la radionavegacion, GPS y telemetria.<br/>
   En esta oportunidad nos centraremos en el internet. Hoy en dia, la conectividad tiene un papel crucial en la vida cotidiana; ya sea para el trabajo, educacion u ocio. No solo conecta a las personas sino que tambien contribuye al progreso y la inclusion en una sociedad cada vez mas digitalizada.<br/>
   El acceso a internet es de vital importancia ya que es esencial para la comunicacion en todas las regiones de Argentina, superar las barreras geograficas y permitir la colaboracion a distancia o el trabajo remoto por ejemplo. Ademas tiene un impacto directo en el desarrollo economico. Garantizar una cobertura y acceso a ainternet para toda la poblacion es fundamental en esta era digital.<br/>
   En este contexto y en mi rol de Data Analyst, realice una anlisis completo de los datos publicados por ENACOM para conocer el comportamiento a nivel nacional de las telecomunicaciones, enfocada puntualmente en el acceso a internet; con el fin de orientar a una empresa del sector respecto a la calidad de sus servicios, identificar oportunidades de crecimiento y plantear soluciones a sus posibles clientes.<br/></p>

***Este proyecto fue desarrollado durante la etapa de Labs del Bootcamp de Henry.*** 

### Tecnologias utilizadas
<div>
  <img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlquQbehFaMuUwUN32KhAS4AxK7WTUtKuZBQ&s width=11%>
  <img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7aUXKTQOQ9aOm7BiBYfZN56MIwj7EgLRlkQ&s>
  <img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLTxw2beQD1IF8lRC2Vlf7E1QKH6opErAGKA&s width=15%>
  <img src=https://seeklogo.com/images/S/streamlit-logo-B405F7E2FC-seeklogo.com.png width=20%>
</div>

### Objetivo

<p align="justify">Realizr un analisis exploratorio de datos (EDA) detallado para comprender el comportamiento del sector de telecomunicaciones a nivel nacional, enfocandose en el acceso a internet, y extraer conclusiones relevantes</p>  

### Introducción 

<p>
   Desde el año 2014, Argentina ha experimentado un crecimiento significativo en el acceso a internet. 11.5 millones de personas con acceso a internet, 14 millones de hogares, todas las provincias del país con conectividad.<br/>
   Este informe presenta un análisis detallado sobre la evolución del acceso a internet, centrándose en la velocidad de descarga, las tecnologías utilizadas y las disparidades regionales.<br/>
   como empresa dedicada a ofrecer acceso a internet, es importante comprender no sólo el presente, sino también el pasado y el futuro del mercado porque esto permite generar estrategias efectivas y aprovechar las oportunidades de crecimiento.
</p>

### Análisis exploratorio de los datos (EDA). ###

<p align="justify"> Se realizo un Analisis Exploratorio de Datos (EDA) y esto permitio visualizar un panorama bastante completo de la conexion a internet en Argentina<br/>
   Siguiendo los pasos basicos de un EDA como la carga de datos, la limpieza de estos datos, analisis descriptivos y estadisticos y la visualizacion de datos, nos permitio llegar a conclusiones relevantes.<br/>
   Puedes ver el analisis de cada uno de ellos en el notebook EDA_Telecomunicaciones</p>

### Evolución del acceso a internet

<p>
   Capital Federal, La Pampa y Tierra del Fuego son las provincias que cuentan con mayor cantidad de población con acceso a internet.<br/>
   Las provincias de Santiago del Estero, San Juan y Formosa son las que presentan desafíos importantes en términos de conectividad.<br/>
   Por otra parte, en líneas generales, los indicadores de acceso por cada 100 habitantes mostraron un crecimiento constante, alcanzando un promedio de 72,04% en 2023. Sin embargo, el primer trimestre de 2024 tiene un leve aumento del 0,05%.
</p>

### Velocidades de conexión 

<p>
   Al profundizar en la velocidad de conexión, nos encontramos con muchos altibajos. Las gráficas de velocidad de descarga y el análisis temporal, indican un aumento en las conexiones de alta velocidad, con un declive en las velocidades más bajas.<br/>
   Se pone en evidencia también la variabilidad considerable en las velocidades de descarga entre provincias, con algunas regiones destacándose en términos de velocidad y otras requiriendo mejoras significativas.
</p>

### Tecnologías 

<p>
   Las tecnologías utilizadas en Argentina para el acceso a internet presentan una variedad de opciones,  desde el cablemodem o el ADSL hasta la innovadora fibra óptica y la versátil conexión inalambrica (wireless). Cada una de estas, ofrece diferentes ventajas y enfrenta distintos desafíos, lo que resalta la necesidad de una oferta diversificada y adaptada a las necesidades cambiantes de los usuarios.<br/>
   La fibra óptica, con su velocidad y estabilidad superiores, ha visto un crecimiento importante, alcanzando 7,6 millones de conexiones en 2023 y 2,2 millones en el primer trimestre de 2024. Hoy, la fibra óptica ha tejido una red de alta velocidad que llega a cada rincón del país, permitiendo que descarguemos películas en cuestión de segundos o participemos en videoconferencias de alta definición.<br/>
   ADSL y cablemodem muestran un alto nivel de acceso, con el cablemodem siendo el más utilizado.<br/>
   La tecnología inalambrica wireless también está emergiendo como una opción atractiva. Aprovechar esta tendencia y adaptar nuestras ofertas a las necesidades locales es crucial para capturar una mayor cuota de mercado.
</p>

### Ingresos del sector

<p>
   Los ingresos generados por el sector han mostrado una tendencia constante al alza. En 2023, los ingresos ascendieron a 522,6 millones de pesos, con un prometedor inicio en 2024, alcanzando 280,4 millones de pesos en el primer trimestre. Este crecimiento sostenido refleja la solidez del sector y la capacidad de las empresas para generar ganancias, a pesar de lls desafíos en la prestación del servicio.
</p>

### KPIs ###

<p align="justify"> Se graficaron y midieron los siguientes KPIs:
   + Aumentar en un 2% el acceso al servicio de internet para el próximo trimestre, cada 100 hogares, por provincia. La fórmula es la siguiente:<br/></p>
         <p align="center">KPI = ((Nuevo aceeso - Acceso actual) / Acceso actual) * 100<br/></p>   
Donde:<br/>
+	"Nuevo acceso" se refiere al número de hogares con acceso a Internet después del próximo trimestre.<br/>
+	"Acceso actual" se refiere al número de hogares con acceso a Internet en el trimestre actual.

### Recomendaciones y conclusiones

<p>
   Podemos concluir que Argentina está en un camino prometedor hacia una mayor conectividad, pero la inversión en infraestructura y la expansión de la cobertura son fundamentales para reducir la brecha digital y abordar las disparidades en velocidad y calidad del servicio.<br/>
   Es un sector económico que ofrece numerosas oportunidades de negocio y la adaptación a las nuevas tecnologías y las demandas de los consumidores es esencial para el éxito.<br/>
   Por lo que seria recomendable para cualquier empresa de este sector:</p>

+ Invertir en infraestructura para llevar el acceso a internet de alta velocidad a zonas rurales y subatendidas.
+ Ofrecer servicios más allá del acceso a internet, como telefonía móvil, IP o televisión satelital.
+ Adoptar nuevas tecnologías como la 5G y la inteligencia artificial para mejorar la experiencia del cliente y ofrecer nuevos servicios.

### Dashboard ###

Puedes visualizar los resultados de este proyecto en el siguiente enlace https://henry-pi-da-vanesalinas.streamlit.app/ </p>  

<hr> 

> `AUTOR`<br>
Este proyecto fue realizado por Vanessa Salinas. No dudes en contactarme! https://www.linkedin.com/in/vanesalinas

<p align="center"><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png></p>
