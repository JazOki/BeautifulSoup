import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

# URL SEMILLA
url = 'https://www.espn.com.mx/futbol/posiciones/_/liga/mex.1'

# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url, headers=headers)

# PARSEO DEL ARBOL CON BEAUTIFUL SOUP
soup = BeautifulSoup(respuesta.content, 'html.parser')
Tabla = soup.find('table', class_='Table Table--align-right Table--fixed Table--fixed-left') #Torneo Clausura - LOGOS Y NOMBRES
fila = Tabla.find('tbody').find_all('tr') 

Tabla2 = soup.find('table', class_= 'Table Table--align-right')#Numeros, Puntuaciones
fila2 = Tabla2.find('tbody').find_all('tr') 
# print(fila)
fila2[0].find_all('td')[0].get_text()

nombres=[]
for x in fila: 
    #append agregar al final 
    nombres.append(x.find_all('td')[0].get_text()) #[1]celda

#________________________________________________________________
#1.- Ordenar de mayor a menor por goles a favor.
gf=[]
for x in fila2:
    gf.append(int(x.find_all('td')[4].get_text()))
df_GF = {"Nombres": nombres,"Goles a Favor": gf}
df1 = pd.DataFrame(df_GF)
# print(df1)
#________________________________________________________________

#________________________________________________________________
#2.- Ordenar de mayor a menor por goles en contra.
gc=[]
for x in fila2:
    gc.append(int(x.find_all('td')[5].get_text()))
df_GC = {"Nombres": nombres,"Goles en Contra": gc}
df2 = pd.DataFrame(df_GC)
# print(df2)
#________________________________________________________________

#________________________________________________________________
#3.- Ordenar por partidos ganados, empatados, perdidos.

#Ganados
ganados=[]
for x in fila2:
    ganados.append(int(x.find_all('td')[1].get_text()))
df_Ganados = {"Nombres": nombres,"Ganados": ganados}
df3 = pd.DataFrame(df_Ganados)

#Empatados
empatados=[]
for x in fila2:
    empatados.append(int(x.find_all('td')[2].get_text()))
df_Empatados = {"Nombres": nombres,"Empatados": empatados}
df4 = pd.DataFrame(df_Empatados)

#Perdidos
perdidos=[]
for x in fila2:
    perdidos.append(int(x.find_all('td')[3].get_text()))
df_Perdidos = {"Nombres": nombres,"Perdidos": perdidos}
df5 = pd.DataFrame(df_Perdidos)

#________________________________________________________________


while True:
    menu = """
    Escoge una opción 1 al 7:
    [1] Ordenar de mayor a menor por goles a favor.
    [2] Ordenar de mayor a menor por goles en contra.
    [3] Ordenar por partidos ganados.
    [4] Ordenar por partidos empatados.
    [5] Ordenar por partidos perdidos.
    [6] Guardar toda la tabla en CSV 
    [7] Salir
    """ 
    print(menu)
    opcion = input("-> ")
    if opcion.isnumeric():
        datos=int(opcion)

        if datos==1:
            df1.sort_values(by=['Goles a Favor'], inplace=True, ascending=False)
            print(df1)
        elif datos==2:
            df2.sort_values(by=['Goles en Contra'], inplace=True, ascending=False)
            print(df2)
        elif datos==3:
            df3.sort_values(by=['Ganados'], inplace=True, ascending=False)
            print(df3)
        elif datos==4:
            df4.sort_values(by=['Empatados'], inplace=True, ascending=False)
            print(df4)
        elif datos==5: 
            df5.sort_values(by=['Perdidos'], inplace=True, ascending=False)
            print(df5)
        elif datos==6:
            # Guardar toda la tabla en CSV
            lista = {'Nombre':nombres,'Goles a Favor':gf,'Goles en Contra':gc,'Ganados':ganados,'Empatados':empatados,'Perdidos':perdidos}
            dfp=pd.DataFrame(lista)
            dfp.to_csv("Tabla_ESPN.csv")
        elif datos==7:
            print("Saliendo . . .")
            break
        else:
            print("Ingresa un numero del menu existente")
    else:
        print("Solo numeros")
        #....



