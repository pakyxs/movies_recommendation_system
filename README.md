# <h1 align=center> **Movies Recommendation System** </h1>


¿Alguna vez te has preguntado cómo Netflix te recomienda películas para ver? ¿Cuál es la idea en la que se basa esta recomendación?

Resulta que existen varios tipos de recomendaciones posibles. Entre ellos, los tres  sistemas de recomendación más populares son:

  1.Motor de recomendación basado en popularidad
  
  2.Motor de recomendación basado en contenido
  
  3.Motor de recomendación basado en filtrado colaborativo

En este proyecto desarrollé y desplegé un modelo de recomendación basado en contenido. Al modelo se le ingresa un nombre de una película, si esta se encuentra en el listado de las películas del dataset devuelve cinco películas recomendadas en base al resumen de la ingresada.

Los datasets que consumí para el modelo fueron movies_dataset.csv y credits.csv  

**`Contenido de la tabla movies_dataset.csv:`**

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



**`Contenido de la tabla credits.csv:`**

| Característica         | Descripción                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------- |
| id                     | ID de la pelicula                                                                     |
| cast                   | Un diccionario que indica el equipo de actores que trabajó en la película             |
| crew                   | Un diccionario que indica el equipo de dirección que trabajó en la película           |

**`Requerimientos:`**

Las librerías que necesité para realizar el EDA y el ETL fueron: Pandas, Numpy , Datetime y Skitlearn.
Para desarrollar la API utilicé FastAPI y para desplegarla Render.


**`Contenido de carpetas:`**

datasets/raw: datasets crudos.

datasets/model: datasets modificados para utilizar con el modelo.

notebooks: notebooks de ETL y EDA y funciones.

main.py: script de funciones para el despliegue.

requirements.txt: librerías necesarias para el proyecto.


**`Instrucciones:`**
1) Instalar las siguientes librerías: Pandas, Numpy , Datetime, Skitlearn y FastAPI.
2) Descargar los archivos movies_dataset.csv y credits.csv del siguiente link en la carpeta datasets/raw:
   [Dataset](https://drive.google.com/drive/folders/1nvSjC2JWUH48o3pb8xlKofi8SNHuNWeu).
3) Ejecutar el archivo EDA.ipynb que se encuentra en la carpeta notebooks:
   En este script se encuentra el análisis de los datos, de aquí sacamos los fundamentos para realizar las transformaciones que vamos a realizar.
4) Ejecutar el archivo ETL.ipynb que se encuentra en la carpeta notebooks:
   En este script se encuentran las transformaciones que le realizamos a los datasets para después ser consumidor por el modelo.


**`API endpoints:`**

+ @app.get('/cantidad_filmaciones_mes/{mes}'): Se ingresa un mes en idioma Español. Devuelve la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
  
+ @app.get('/cantidad_filmaciones_dia{dia}'): Se ingresa un día en idioma Español. Devuelve la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
 
+ @app.get('/score_titulo/{titulo}'): Se ingresa el título de una filmación devuelve como respuesta el título, el año de estreno y el score.
 
+ @app.get('/votos_titulo/{titulo}'): Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones.
    La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende,
    no se devuelve ningun valor.

+ @app.get('/get_actor/{nombre_actor}'): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno.
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno.
  
+ @app.get('/get_director/{nombre_director}'): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
  
+ @app.get('/recomendacion/{titulo}'): Ingresas un nombre de pelicula y te recomienda las cinco más similares en una lista.


**`Link en Render:`**
+ https://pakyxs-movies-recommendation-system.onrender.com/docs

