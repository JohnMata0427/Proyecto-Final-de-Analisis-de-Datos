# Proyecto-Final-de-Analisis-de-Datos-2023B
## INTRODUCCIÓN
La gran cantidad de datos generados a diario a través de múltiples fuentes como archivos estáticos, web scraping, entre otros, representa una oportunidad para extraer información valiosa mediante técnicas de análisis y visualización.
En este contexto, la implementación de una arquitectura de Data Lake resulta apropiada para la recolección e integración de grandes volúmenes de datos no estructurados provenientes de extensas fuentes.
# Que es un Data Lake?
Un data lake o lago de datos es un repositorio centralizado que permite almacenar, compartir, gobernar y descubrir todos los datos estructurados y no estructurados de una organización a cualquier escala. 
# Proceso para crear un Data Lake
### Desarrollo
Primero buscamos alrededor de 28 datasets, dada la dificultad encontramos mas csv y json por lo cual, algunos data sets los enviamos a diferentes gestores por ejemplo: 
GESTORES SQL
-SQLite
-My SQL Workbench
-Postgresql
GESTORES NOSQL
-JSON
-CSV
-Mongo DB
Despues de realizar la limpieza necesaria a todos los datset, lo cual se lo realizo en jupyter con la libreria de pandas, a cada datasets se le borro registros duplicados y se le relleno los espacios nulos con 'sin informacion' y mientras tanto los numeros los relleno con 0.
![image](https://github.com/JohnMata0427/Proyecto-Final-de-Analisis-de-Datos-2023B/assets/130105827/b12baa57-f3e3-4fb3-915a-6b86d29a8de0)
![image](https://github.com/JohnMata0427/Proyecto-Final-de-Analisis-de-Datos-2023B/assets/130105827/830b15eb-ef92-4af5-bbaa-92e157b36011)
![image](https://github.com/JohnMata0427/Proyecto-Final-de-Analisis-de-Datos-2023B/assets/130105827/8f6afb89-d97a-43fb-b41a-34f229b05522)
![image](https://github.com/JohnMata0427/Proyecto-Final-de-Analisis-de-Datos-2023B/assets/130105827/a38af36b-202e-4a60-ad45-01b40be757ed)
- Como se puede ver en las imagenes ese es el codigo que se utilizo para limpiar todos los datasets
- Luego se procedio a enviar cada data a diferentes gestores, por ejemplo: Noticias_1 se le envio a MySQLWorkbench
  ![image](https://github.com/JohnMata0427/Proyecto-Final-de-Analisis-de-Datos-2023B/assets/130105827/d98f607c-4d76-474e-81a0-cc76d29a69c8)
  







