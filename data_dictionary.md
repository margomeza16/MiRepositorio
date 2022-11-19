# Data Dictionary

In this document you must describe the tables, collections or files that you are using in the project. You can describe each databased provide UML diagrams for a better design description.
EL conjunto de datos esta integrado por imagenes endoscopicas gastrointestinales que de acuerdo a la fuente original (https://dl.acm.org/doi/pdf/10.1145/3083187.3083212), corresponden a imágenes reales, verificadas y etiquetadas por médicos especialistas en endoscopias. La clasificación de las imágenes corresponde a la patalogía médica encontrada, a saber:
/0_normal/: Contiene las imágenes con diagnostico normal (Sin
enfermadad).

/1_ulcerative_colitis/: Contiene las imágenes con diagnóstico de colitis ulcerosa.

/2_polyps/: Contiene las imágenes con diagnóstico de pólipos.

/3_esophagitis/: Contiene las imágenes con diagnóstio de esofagitis.

Los imagenes se encuentran en formato .JPG, que de acuerdo a la fuente original ((https://dl.acm.org/doi/pdf/10.1145/3083187.3083212), diferente resolución desde 720x576 hasta 1920x1072
píxeles y organizados de una manera en la que se ordenan por separado
carpetas nombradas de acuerdo con el contenido.  y se encuentran agrupadas en tres archivos .zip a saber:

Un archivo .zip con las imágenes de entrenamiento.

Un Archivo .zip con las imágenes de test.

Un archivo .zip con las imágenes de validación.


# Database Name 1

Description of the database.
A continuación se describe el conjunto de imagenes de entrenamiento

![UML Diagram](/file/uml/database1)

## Table 1

Here you must describe the table

| column | type | description |
| --- | --- | --- |
| col1 | INT | Example column |

# Database Name 2

Description of the database.

![UML Diagram](/file/uml/database1)

## Table 2

Here you must describe the table

| column | type | description |
| --- | --- | --- |
| col1 | INT | Example column |
