import streamlit as st
import pandas as pd
import pip
pip.main(["install", "openpyxl"])
#from openpyxl import reader,load_workbook,Workbook
import numpy as np
from PIL import Image

##############
st.sidebar.image("excel.png",
                 caption="Jesus Alvarado Huayhuaz, PhDc")

##############Pagina 1###############
def Home():
    st.markdown("# Temario")
    st.sidebar.markdown("# Excel Nivel Intermedio")

    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('Unidad 1: TABLAS')
        st.write('''Diseño. Quitar duplicados. Filtros básicos, filtros avanzados.
        Listas personalizadas. Validación de datos.''')
        
    with total2:
        st.info('Unidad 2: Funciones condicionales')
        st.write (pd.DataFrame({'Tema': ['Función SI',
                                          'Función SI', 
                                          'Formatos'], 
                                'Fecha': ["con varias condiciones", "(Y-O) anidada", 
                                           "condicionales"]}))
    
    total3, total4 = st.columns(2, gap='large')
    with total3:
        st.info('Unidad 3: Principales funciones usadas en bases de datos')
        st.write('''BDCONTAR, BDSUMA, BDMAX, BDMIN, BDPROMEDIO, BDCONTARA y BDEXTRAER. Función BUSCARV, Función BUSCARH''')
        
    with total4:
        st.info('Unidad 4: Gráficos')
        st.write ('''Diagrama de Gantt en Excel. Gráficos de Cumplimiento o de Progreso en EXCEL.''')

    total5, total6 = st.columns(2, gap='large')

    with total5:
        st.info('Unidad 2: Funciones condicionales')
        st.write (pd.DataFrame({'Tema': ['Creación de una Tabla Dinámica',
                                          'Cálculos', 
                                          'Extracción de datos'], 
                                'Fecha': ["Ordenamiento y agrupamiento de datos", "Formato", 
                                           "Modificación y actualización"]}))

    with total6:
        st.info('Unidad 6: Solver Excel')
        st.write ('''Aplicaciones y ejercicios.''')
    
##############Pagina 2##############
def page2():
    st.markdown("Tablas en Excel")
    st.sidebar.markdown("Práctica Nº1")
    
    st.info('Generalidades')
    st.write('''El formato de tabla en Excel se refiere a una funcionalidad que convierte un rango de datos en una tabla estructurada y con estilo. Esta herramienta no solo mejora la apariencia visual de los datos, sino que también proporciona una serie de características que facilitan la gestión y el análisis de la información. Al aplicar el formato de tabla, los datos se organizan en filas y columnas claramente definidas, con la opción de incluir encabezados de fila y columna.''')
    st.write('''Para los siguientes ejercicios usar el libro llamado "practica 1 datos.xlsx" ''')
    st.info('A. Crear tablas y aplicarles formato')  
    #st.write(pd.DataFrame({'Notebook': ['https://github.com/inefable12/CQCPE_2023_jesus/blob/main/1_ABC_Python_github.ipynb', 'https://github.com/inefable12/balanceo_rxn_combustion_espanol']}))

    #df = pd.read_excel('practica_1_datos_1.xlsx')
    df = pd.read_csv('practica_1_datos_1.csv')
    st.write(df)
    st.write('''Para dar el formato de tabla en Excel a un rango de datos se deberá hacer lo siguiente:''')
    st.write('''(a) Seleccionar la lista de datos sea arrastrando con clic derecho sin soltar desde la primera celda hasta la ultima o usando el atajo Ctrl + E. Otra manera de seleccionar todos los datos es usar las teclas Ctrl + Shift + -> y luego Ctrl + Shift + ⭣''')

    st.write('''(b) Luego en la barra de herramientas clic en el icono “Dar formato como tabla” o usar el atajo Ctrl + T. Seleccione el estilo de color que mas le agrade. Finalmente dar aceptar verificando que la casilla de encabezados este marcada.''')    st.info('Grupal')
  
##
def page3():
  st.header('''Asistencia''')

  lista = pd.DataFrame({'Nombre': ['Vilchez Flores Benito Junior',
                                   'Castillo Quesada Sixto Gustavo',
                                   'Zorrilla Calderón Miguel Andrés',
                                   'Obispo Escajadillo Willians Josue',
                                   'Gutierrez Espinoza Nick Anthony',
                                   'Arias Alfaro Astrid Fiorella',
                                   'Vasquez Quispe Anaira Valeria',
                                   'Peña Lajo Jefferson Felipe',
                                   'Maza Angeles Andree Alessandro',
                                   'Cayo Bueno Fabrizio Daniel',
                                   'Herrera Zela Sebastian Andres',
                                   'Venegas Quispe Lucibeth Merliza',
                                   'Alba Astudillos Rolando',
                                   'Manyari Alejandria Peter Isaac',
                                   'Fernandez Herrera Alejandro',
                                   'Suclupe Franco Ashly Glenny',
                                   'Oros Quispe Alexandra Soledad',
                                   'Juarez Torres Saul Esteban',
                                   'Quispe Rojas Sebastian Esteban',
                                   'Cabrera Somoza Edgar Yonatan',
                                   
                                   ], 
                        '18/03/2024': ["X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","X","X",
                                       ],
                        '25/03/2024': ["X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","X","X",
                                       ]
                        })

  st.write(lista)

  st.write('''Bar chart''')
  st.bar_chart(
    lista, x="Nombre", y=["18/03/2024", "25/03/2024"]) #, color=["#FF0000", "#0000FF"])

##
def page4():
  st.header('Más información', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/Quimica_1_FIA_UNI/")
  
##
page_names_to_funcs = {
  "Contenido del Curso": Home,
  "1. Tablas en Excel": page2,
  "Asistencia": page3,
  "Consultas": page4,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
