from fastapi import FastAPI
import pandas as pd
import numpy as np
import ast
from datetime import datetime
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import os
app = FastAPI()

# Asignamos el path relativo a la variable dir para utilizarla a la hora de consumir los datasets
dir = os.getcwd()+'/datasets/model' 

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes:str):
    "Se ingresa un mes en idioma Español. Devuelve la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset."

    # Cargando datos del archivo csv
    df = pd.read_csv(dir+"/movies.csv", sep=",", low_memory=False)

    
    def obtain_month_number(mes):
        months = {
            "enero": 1,
            "febrero": 2,
            "marzo": 3, 
            "abril": 4,
            "mayo": 5,
            "junio": 6,
            "julio": 7,
            "agosto": 8,
            "septiembre": 9,
            "octubre": 10,
            "noviembre": 11,
            "diciembre": 12,
        }

        mes = mes.lower()  # Convertimos el mes ingresado a minúsculas
        month_number = months.get(
            mes
        )  # Buscamos en el diccionario el número correspondiente al mes ingresado y lo asignamos a la variable month_number

        if month_number:
            return month_number
        else:
            return None

    month_number = obtain_month_number(mes)
    # Ponemos la condición que si no encuentra el mes retorne un mensaje para que lo ingrese correctamente, sino nos retorna la cantidad de películas estrenadas en ese mes.
    if month_number == None:
        return print(
            month_number,
            "no es un mes del año, por favor ingrese de nuevo correctamente.",
        )
    else:
        count = 0  # Iniciamos el contador
        for row in df[
            "release_date"
        ]:  # Recorremos los valores de la columna release_date
            if (
                pd.to_datetime(row).month == month_number
            ):  # Ponemos la condición que si número del mes coincide con el de la variable month_number, entonces aumenta el contador en una unidad
                count += 1
    response = {'mes': mes.lower(), 'cantidad': count}
    return response


@app.get('/cantidad_filmaciones_dia{dia}')
def cantidad_filmaciones_dia(dia:str):
    "Se ingresa un día en idioma Español. Devuelve la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset."

    # Cargando datos del archivo csv
    df = pd.read_csv(dir+"/movies.csv", sep=",", low_memory=False)
    
    def obtain_day_number(dia):
        days = {
            "lunes": 1,
            "martes": 2,
            "miercoles": 3,
            "jueves": 4,
            "viernes": 5,
            "sabado": 6,
            "domingo": 7,
        }

        dia = dia.lower()  # Convertimos el día ingresado a minúsculas
        day_number = days.get(
            dia
        )  # Buscamos en el diccionario el número correspondiente al día ingresado y lo asigna a la variable day_number

        if day_number:
            return day_number
        else:
            return None

    day_number = obtain_day_number(dia)
    # Ponemos la condición que si no encuentra el día retorne un mensaje para que lo ingrese correctamente, sino nos retorna la cantidad de películas estrenadas en ese día.
    if day_number == None:
        return print(
            day_number,
            "no es un día de la semana, por favor ingrese de nuevo correctamente.",
        )
    else:
        count = 0  # Iniciamos el contador
        for row in df[
            "release_date"
        ]:  # Recorremos los valores de la columna release_date
            if (
                pd.to_datetime(row).day == day_number
            ):  # Ponemos la condición que si número del día coincide con el de la variable day_number, entonces aumenta el contador en una unidad
                count += 1
    response = {'dia': dia.lower(), 'cantidad': count}
    return response




@app.get('/score_titulo/{titulo}')
def score_titulo(titulo_de_la_filmacion:str):
    "Se ingresa el título de una filmación devuelve como respuesta el título, el año de estreno y el score"

    # Cargamos datos del archivo csv
    df = pd.read_csv(dir+"/movies.csv", sep=",", low_memory=False)
    
    # Convertimos el titulo a minúsculas para evitar errores
    df['title'] = df['title'].str.lower()
    
    # Creamos un df_match en el cual guardamos las filas que coinciden con el titulo
    df_match = df[df["title"].str.contains(titulo_de_la_filmacion.lower())]

    # Si el df_match está vacío quiere decir que la película no se encuentra en el dataframe
    if len(df_match) == 0: 
        return print(f"La película {titulo_de_la_filmacion} no se encontró, por favor ingrese otra.")
    
    response = {"título": titulo_de_la_filmacion.title(),
                "anio": df_match["release_year"].iloc[0],
                "popularidad": df_match["popularity"].iloc[0]}
    return response






@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo_de_la_filmacion:str):
    """Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones.
    La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende,
    no se devuelve ningun valor."""

    # Carganmos datos del archivo csv
    df = pd.read_csv(dir+"/movies.csv", sep=",", low_memory=False)
    
    response = []
    for idx, row in enumerate(df['title']):
        if (row.lower() == titulo_de_la_filmacion.lower()):
            if df['vote_count'][idx] >= 2000:
                response.append({
                "título": df["title"][idx],
                "anio": df["release_year"][idx],
                "voto_total": df["vote_count"][idx],
                "voto_promedio": df["vote_average"][idx]
                })
          
    if len(response) == 0: # Si la lista está vacía quiere decir que no se encontró ningun valor, devuelve el siguiente mensaje.
        respuesta = f'La película {titulo_de_la_filmacion} no cuenta con al menos 2000 valoraciones, por favor ingrese otra.'
        return {'error not found': respuesta}
    
    else:
        return response
    




@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor:str):
    """Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno"""

    # Cargando datos de los archivos csv
    df_cast = pd.read_csv(dir+"/cast.csv", sep=",", low_memory=False)
    df = pd.read_csv(dir+"/movies.csv", sep=",", low_memory=False)
    # Creamos una lista para almacenar los valores de 'movie_id'
    lista_movie_id = []

    # Buscamos el valor en la columna 'name' y extraemos el valor correspondiente en 'movie_id'
    filas_encontradas = df_cast.loc[df_cast['name'].str.lower() == nombre_actor.lower()]

    # Iterar sobre las filas encontradas y extraer los valores de 'movie_id'
    for index, row in filas_encontradas.iterrows():
        lista_movie_id.append(row['movie_id'])
    
    lista_movie_id = list(set(lista_movie_id)) # Quitamos duplicados ya que un actor puede hacer de más de un personaje en una película

    count = len(lista_movie_id) # Asignamos la cantidad de películas que tenemos en la lista a la variable count para usarla como contador de películas
    
    # Con la lista de id de películas calculamos el retorno total sumando los valores de la columna return del dataframe df

    # Filtramos las filas que coinciden con los valores de la lista lista_movie_id
    filas_coincidentes = df[df['id'].isin(lista_movie_id)]

    # Sumamos los valores de la columna return
    total_return = filas_coincidentes['return'].sum()

    # Calculamos el promedio del retorno dividiendo el total en la cantidad de películas
    avg_return = total_return/ count

    response = {'actor':nombre_actor, 'cantidad_filmaciones':count, 'retorno_total':total_return, 'retorno_promedio':avg_return}
    
    return response




@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.'''

    # Cargando datos de los archivos csv
    df_director = pd.read_csv(dir+"/director.csv", sep=",", low_memory=False)
    df = pd.read_csv(dir+"/movies.csv", sep=",", low_memory=False)
    
    # Creamos una lista para almacenar los valores de 'movie_id'
    lista_movie_id = []

    # Buscamos el valor en la columna 'name' y extraemos el valor correspondiente en 'movie_id'
    filas_encontradas = df_director.loc[(df_director['name'].str.lower() == nombre_director.lower())]
    
    # Iterar sobre las filas encontradas y extraer los valores de 'movie_id'
    for index, row in filas_encontradas.iterrows():
        lista_movie_id.append(row['movie_id'])

    response = []
    
    # Con la lista de id de películas calculamos el retorno total sumando los valores de la columna return del dataframe df

    # Filtramos las filas que coinciden con los valores de la lista lista_movie_id
    filas_coincidentes = df[df['id'].isin(lista_movie_id)]

    # Sumamos los valores de la columna return
    total_return = filas_coincidentes['return'].sum()

    movies_list_dict = []

    # Asignamos los valores de las filas al diccionario que va a entregar la función
    for index, row in filas_coincidentes.iterrows():
        title = row['title']
        year = row['release_year']
        return_movie = row['return']
        budget_movie = row['budget']
        revenue_movie = row['revenue']

        movies_dict = {'titulo': title, 'anio': year, 'retorno_pelicula': return_movie,'budget_pelicula':budget_movie,'revenue_pelicula':revenue_movie}
        movies_list_dict.append(movies_dict)

    

    response = {'director':nombre_director, 'retorno_total_director':total_return, 
                'peliculas':movies_list_dict}
    
    return response



@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las cinco más similares en una lista'''
    # Cargando datos del archivo csv
    df = pd.read_csv(dir+"/sample.csv", sep=",", low_memory=False)


    if (df['title'].str.lower()).isin([titulo.lower()]).any():

        tfv = TfidfVectorizer(min_df=3,  max_features=None,
                strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
                ngram_range=(1, 3),
                stop_words = 'english')
        
        # Ajustamos el TF-IDF sobre el texto 'overview'
        tfv_matrix = tfv.fit_transform(df['overview'])

        # Computamos el kernel sigmoide
        sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
        
        
        # Hacemos reverse mapping de los indices y los títulos de las películas
        indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()

        # Obtenemos el indice de la película
        idx = indices[titulo.lower()]

        # Obtenemos la lista de similitud de nuestra película con respecto a las otras
        sig_scores = list(enumerate(sig[idx]))

        # Ordenamos las películas en base al puntaje de similitud en orden descendente
        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

        # Puntajes de las 5 películas mas similares
        sig_scores = sig_scores[1:6]

        # Guardamos los indices de las películas
        movie_indices = [i[0] for i in sig_scores]

        # Guardamos los títulos de las películas en una variable para después mostrarla
        valores_columna = df.loc[movie_indices, 'title'].values
        response = list(valores_columna)
        return response
    else:
        respuesta = f'La película {titulo} no está en la lista, por favor ingrese otra.'
        return {'error not found': respuesta}

