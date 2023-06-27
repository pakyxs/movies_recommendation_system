# Movies Recommendation System


¿Alguna vez te has preguntado cómo Netflix te recomienda películas para ver? ¿Cuál es la idea en la que se basa esta recomendación?

Resulta que existen tres tipos de recomendaciones posibles. Veamos cuáles son.

Tres sistemas de recomendación populares:

  1.Motor de recomendación basado en popularidad
  
  2.Motor de recomendación basado en contenido
  
  3.Motor de recomendación basado en filtrado colaborativo

En este proyecto desarrollé y desplegé un modelo de recomendación basado en contenido. Al modelo se le ingresa un nombre de una película, si esta se encuentra en el listado de las películas del dataset devuelve cinco películas recomendadas en base al resumen de la ingresada.

Los datasets que consumí para el modelo fueron movies_dataset.csv y credits.csv  

Contenido de la tabla movies_dataset.csv:

| Característica         | Descripción                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------- |
| adult                  | Indica si la película tiene califiación X, exclusiva para adultos.                    |
| belongs_to_collection  | Un diccionario que indica a que franquicia o serie de películas pertenece la película |
| budget                 | El presupuesto de la película, en dólares                                             |
| genres                 | Un diccionario que indica todos los géneros asociados a la película                   |
| homepage               | La página web oficial de la película                                                  |
| id                     | ID de la pelicula                                                                     |
| imdb_id                | IMDB ID de la pelicula                                                                |
| original_language      | Idioma original en la que se grabo la pelicula                                        |
| original_title         | Titulo original de la pelicula                                                        |
| overview               | Pequeño resumen de la película                                                        |
| popularity             | Puntaje de popularidad de la película, asignado por TMDB (TheMoviesDataBase)          |
| poster_path            | URL del póster de la película                                                         |
| production_companies   | Lista con las compañias productoras asociadas a la película                           |
| production_countries   | Lista con los países donde se produjo la película                                     |
| release_date           | Fecha de estreno de la película                                                       |
| revenue                | Recaudación de la pelicula, en dolares                                                |
| runtime                | Duración de la película, en minutos                                                   |
| spoken_languages       | Lista con los idiomas que se hablan en la pelicula                                    |
| status                 | Estado de la pelicula actual (si fue anunciada, si ya se estreno, etc)                |
| tagline                | Frase celebre asociadaa la pelicula                                                   |
| title                  | Titulo de la pelicula                                                                 |
| video                  | Indica si hay o no un trailer en video disponible en TMDB                             |
| vote_average           | Puntaje promedio de reseñas de la pelicula                                            |
| vote_count             | Numeros de votos recibidos por la pelicula, en TMDB                                   |



Contenido de la tabla credits.csv:

| Característica         | Descripción                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------- |
| id                     | ID de la pelicula                                                                     |
| cast                   | Un diccionario que indica el equipo de actores que trabajó en la película             |
| crew                   | Un diccionario que indica el equipo de dirección que trabajó en la película           |

Requerimientos:
Las librerías que necesité para realizar el EDA y el ETL fueron: Pandas, Numpy y Skitlearn.
Para desarrollar la API utilicé FastApi y para desplegarla Render.


Contenido de carpetas

datasets/raw: datasets crudos.
datasets/model: datasets modificados para utilizar con el modelo.
notebooks: notebooks de ETL y EDA y funciones.
main.py: script de funciones para el despliegue.
requirements.txt: librerías necesarias para el proyecto.


Instrucciones de Ejecución
Para disponibilizar los datos es necesario: a) Correr previamente el notebook etl.ipynb, el cual extrae y transforma los datatasets originales. b) Ejecutamos el notebook eda.ipynb donde buscamos la relación entre el budget y la revenue, analizamos los datos atípicos con la variable popularity, por último generamos una nube de palabras de la columna 'title'.

API endpoints
API en Render: 

