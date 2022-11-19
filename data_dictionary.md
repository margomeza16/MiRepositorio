# Data Dictionary

In this document you must describe the tables, collections or files that you are using in the project. You can describe each databased provide UML diagrams for a better design description.

EL conjunto de datos esta integrado por imagenes endoscopicas con diagnósticos de enfermedades gastrointestinales o del colon, que de acuerdo a la fuente original (https://dl.acm.org/doi/pdf/10.1145/3083187.3083212), corresponden a imágenes reales, verificadas y etiquetadas por médicos especialistas en endoscopias. La clasificación de las imágenes corresponde a la patalogía médica encontrada, a saber:

/0_normal/: Corresponde a las imágenes con diagnostico normal (Sin
enfermadad).

/1_ulcerative_colitis/: Corresponde a las imágenes con diagnóstico de colitis ulcerosa.

/2_polyps/: Corresponde a las imágenes con diagnóstico de pólipos.

/3_esophagitis/: Corresponde a las imágenes con diagnóstio de esofagitis.

Los imagenes se encuentran en formato .JPG, que según la fuente original ((https://dl.acm.org/doi/pdf/10.1145/3083187.3083212), tienen diferentes resoluciones, que van desde 720x576 hasta 1920x1072 píxeles y organizadas en carpetas nombradas de acuerdo con la patologia indicada antes.   A su vez, se encuentran agrupadas en tres archivos .zip a saber:

train.zip. Archivo .zip con las imágenes de entrenamiento.

test.zip. Archivo .zip con las imágenes de test.

val.zip. Archivo .zip con las imágenes de validación.

# A continuación se describe el contenido de cada uno de estos archivos:


# train.zip : Archivo zip con imágenes de entrenamiento.

Description of the database.

A continuación se describe el conjunto de imagenes de entrenamiento:

El archivo contiene 3200 imágenes, distribuidas en las siguientes 4 carpetas, que corresponden a las 4 clases de diagnósticos:

/0_normal/: Contiene 800 imágenes con diagnostico normal (Sin
enfermadad).

/1_ulcerative_colitis/: Contiene 800 imágenes con diagnóstico de colitis ulcerosa.

/2_polyps/: Contiene 800 imágenes con diagnóstico de pólipos.

/3_esophagitis/: Contiene 800 imágenes con diagnóstio de esofagitis.




# test.zip : Archivo zip con imágenes de test.

Description of the database.

A continuación se describe el conjunto de imagenes de test:

El archivo contiene 800 imágenes, distribuidas en las siguientes 4 carpetas, que corresponden a las 4 clases de diagnósticos:

/0_normal/: Contiene 200 imágenes con diagnostico normal (Sin
enfermadad).

/1_ulcerative_colitis/: Contiene 200 imágenes con diagnóstico de colitis ulcerosa.

/2_polyps/: Contiene 200 imágenes con diagnóstico de pólipos.

/3_esophagitis/: Contiene 200 imágenes con diagnóstio de esofagitis.


# val.zip : Archivo zip con imágenes de validación.

Description of the database.

A continuación se describe el conjunto de imagenes de validación:

El archivo contiene 2000 imágenes, distribuidas en las siguientes 4 carpetas, que corresponden a las 4 clases de diagnósticos:

/0_normal/: Contiene 500 imágenes con diagnostico normal (Sin
enfermadad).

/1_ulcerative_colitis/: Contiene 5 imágenes con diagnóstico de colitis ulcerosa.

/2_polyps/: Contiene 500 imágenes con diagnóstico de pólipos.

/3_esophagitis/: Contiene 500 imágenes con diagnóstio de esofagitis.
