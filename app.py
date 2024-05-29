import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt
import pip 
pip.main(["instal","openpyxl"])

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
        st.write('''G.''')
        
    with total2:
        st.info('Unidad 2: FUNCIONES CONDICIONALES')
        st.write (pd.DataFrame({'Tema': ['Componentes y clasificación, ley de número equivalente',
                                          'Unidades de concentración, fracción molar, Molaridad', 
                                          'Normalidad y Molalidad, partes por millón',
                                          'Método de dilución y mezcla de soluciones',
                                          'problemas de estequiometria de soluciones',
                                          'titulación acido – base, uso del indicador',
                                          'Propiedades coligativas de las soluciones, ecuación de Vant Hoff'
                                        ], 
                                'Fecha': ["Semana", "Semana", 
                                           "Semana","Semana", "Semana", 
                                           "Semana","Semana",]}))
    
    total3, total4 = st.columns(2, gap='large')
    with total3:
        st.info('Unidad 3: Principales funciones usadas en bases de datos')
        st.write('''Definición, generalidades / Cálculo de la velocidad de una reacción química / Velocidades de reacción de orden cero, de 1° y 2º orden, ejercicios / Cálculo de la vida media de una reacción química / Factores que modifican la velocidad de reacción (temperatura, presión, concentración y catalizador).''')
        
    with total4:
        st.info('Unidad 4: Gráficos ')
        st.write ('''Definición, características / Cálculo de la constante de equilibrio químico Kp y Kc / Relación de las constantes Kp y Kc / Grado de reacción (a) y cociente de reacción (Q) / relaciones entre 𝛼, Q y Kc 1 teoría de ácidos y bases / teoría de constante de acides y basicidad, Ka y Kb, teoría de auto- ionización del agua, Kw / Potencial del ión hidrogeno (pH), problemas / hidrólisis (Kh), soluciones buffer o tampón /cálculo del pH / Producto de solubílidad (Kps), efecto del ion común, solubilidad molar/ precipitación selectiva de iones (cationes y aniones).''')

    
    
##############Pagina 2##############
def page2():
    st.markdown("# Clase 1: 11/05/2024")
    st.sidebar.markdown("Tablas en Excel")
    
    st.info('Generalidades')
    st.write('''
    El formato de tabla en Excel se refiere a una funcionalidad que convierteunrango 
    de datos en una tabla estructurada y con estilo. Esta herramienta nosolomejora la 
    apariencia visual de los datos, sino que también proporciona una seriedecaracterísticas 
    que facilitan la gestión y el análisis de la información. 
    
    Al aplicar el formato de tabla, los datos se organizan en filas y columnas claramente 
    definidas, con la opción de incluir encabezados de fila y columna.''')

    df1 = pd.read_excel('practica_1_datos.xlsx')
    st.write(df1)
  
    st.write('Puede ser útil')
    st.write(pd.DataFrame({'Notebook': ['https://github.com/inefable12/CQCPE_2023_jesus/blob/main/1_ABC_Python_github.ipynb', 'https://github.com/inefable12/balanceo_rxn_combustion_espanol']}))
  
    st.info('Grupal')
    st.write('''Tiempo estimado: 1 hora''')
    st.write('''Por grupo resolver los ejercicios asignados (capítulo 3 de Brown) empleando python desde Google Colab.''')
    st.write('''Presentación: Enviar al delegado(a) el enlace al archivo: "nombre_grupo.ipynb"''')  
    st.write('''Fecha máxima de entrega: Domingo 31/03/2024 a las 23:59''')

##
def page3():
  st.header('# Clase 2: 18/05/2024')

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
