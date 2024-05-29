import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt
import pip
pip.main(["install", "openpyxl"])

##############
st.sidebar.image("excel.png",
                 caption="Jesus Alvarado H, MSc, PhDc")

##############Pagina 1##############
def Home():
    st.markdown("# Temario")
    st.sidebar.markdown("# Química I")

    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('Unidad 1: REACCIONES QUÍMICAS')
        st.write('''Generalidades sobre las reacciones químicas y ecuaciones químicas. 
                    Clasificación de las reacciones químicas. 
                    Reacciones endotérmicas y exotérmicas, cálculo de la entalpía de la reacción, 
                    entalpía de reacción estándar, ejercicios.
                    Métodos de balanceo de la reacciones químicas (redox – ion electrón).
                    Estequiometria I y las leyes ponderales, ley de conservación de la masa y de 
                    las proporciones definidas, problemas. 
                    Estequiometría II, ley de las relaciones sencillas, problemas con gases 
                    ideales, masa equivalente.''')
        
    with total2:
        st.info('Unidad 2: SOLUCIONES')
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
        st.info('Unidad 3: CINÉTICA QUÍMICA')
        st.write('''Definición, generalidades / Cálculo de la velocidad de una reacción química / Velocidades de reacción de orden cero, de 1° y 2º orden, ejercicios / Cálculo de la vida media de una reacción química / Factores que modifican la velocidad de reacción (temperatura, presión, concentración y catalizador).''')
        
    with total4:
        st.info('Unidad 4: EQUILIBRIO QUÍMICO ')
        st.write ('''Definición, características / Cálculo de la constante de equilibrio químico Kp y Kc / Relación de las constantes Kp y Kc / Grado de reacción (a) y cociente de reacción (Q) / relaciones entre 𝛼, Q y Kc 1 teoría de ácidos y bases / teoría de constante de acides y basicidad, Ka y Kb, teoría de auto- ionización del agua, Kw / Potencial del ión hidrogeno (pH), problemas / hidrólisis (Kh), soluciones buffer o tampón /cálculo del pH / Producto de solubílidad (Kps), efecto del ion común, solubilidad molar/ precipitación selectiva de iones (cationes y aniones).''')

    
    
##############Pagina 2##############
def page2():
    st.markdown("# Actividad: 25/03/2024")
    st.sidebar.markdown("# Deadline: 31/03/2024")
    
    st.info('Individual')
    st.write('''Tiempo estimado: 1 hora''')
    st.write('''Fecha de entrega: No aplica''')
    st.write ('''Repasar material introductorio sobre python en Google Colab''')
    st.write('Puede ser útil')
    st.write(pd.DataFrame({'Notebook': ['https://github.com/inefable12/CQCPE_2023_jesus/blob/main/1_ABC_Python_github.ipynb', 'https://github.com/inefable12/balanceo_rxn_combustion_espanol']}))
  
    st.info('Grupal')
    st.write('''Tiempo estimado: 1 hora''')
    st.write('''Por grupo resolver los ejercicios asignados (capítulo 3 de Brown) empleando python desde Google Colab.''')
    st.write('''Presentación: Enviar al delegado(a) el enlace al archivo: "nombre_grupo.ipynb"''')  
    st.write('''Fecha máxima de entrega: Domingo 31/03/2024 a las 23:59''')

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
  "Actividad": page2,
  "Asistencia": page3,
  "Consultas": page4,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
