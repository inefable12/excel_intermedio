import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt
#import pip 
#pip.main(["instal","openpyxl"])

##############
st.sidebar.image("excel.png",
                 caption=" Excel 'nivel intermedio' ")

##############Pagina 1##############
def Home():
    st.markdown("# Temario")
    st.sidebar.markdown("# Excel Nivel Intermedio")

    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('Unidad 1: TABLAS')
        st.write('''Gdf.''')
        
    with total2:
        st.info('Unidad 2: FUNCIONES CONDICIONALES')

    
    total3, total4 = st.columns(2, gap='large')
    with total3:
        st.info('Unidad 3: Principales funciones usadas en bases de datos')
        st.write('''Definición, generalidades''')
        
    with total4:
        st.info('Unidad 4: Gráficos ')
        st.write ('''Definición, características''')
   
##############Pagina 2##############
def page2():
    st.markdown("# Clase 1: 11/05/2024")
    st.sidebar.markdown("Tablas en Excel")
    
    st.info('Generalidades')
    #st.write('''El formato de tabla en Excel se refiere a una funcionalidad que convierteunrango 
    #de datos en una tabla estructurada y con estilo. Esta herramienta nosolomejora la 
    #apariencia visual de los datos, sino que también proporciona una seriedecaracterísticas 
    #que facilitan la gestión y el análisis de la información. 
    #Al aplicar el formato de tabla, los datos se organizan en filas y columnas claramente 
    #definidas, con la opción de incluir encabezados de fila y columna.''')

   # df1 = pd.read_excel('practica_1_datos_1.xlsx')
    #st.write(df1)
  
    st.info('Grupal')
    st.write('''Tiempo estimado: 1 hora''')

##
def page3():
  st.header('# Clase 2: 18/05/2024')

##
def page4():
  st.header('M', divider='rainbow')
   
  st.link_button("Guías", "https://forms.gle/sQj17Weg9dC1kw5a7")
  
##
page_names_to_funcs = {
  "Contenido del Curso": Home,
  "Clase 1": page2,
  "Clase 2": page3,
  "Clase 3": page4,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
