# Project Charter

## Business background

* Who is the client, what business domain the client is in. 

Este proyecto esta  dirigido al sector salud, con el objetivo de apoyar en el diagnóstico automatizado de patologías digestivas y del colon, a partir de imágenes endoscópicas gastrointestinales. El cliente son las áreas de gastroenterología de las clinicas y hospitales del sector salud y el usuario directo es el médico especialista en gastroentrologia endoscospica.

* What business problems are we trying to address?

El problema de negocio a abordar en este proyecto es el diagnóstico automatizado de posibles enfermedades en el tracto gastrointestinal, a partir de imágenes endoscópicas gastrointestinales reales, evaluadas y etiquetadas por especialistas en endoscopias gatrointestinales. Esto con el propósito de apoyar el diagnóstico temprano y tratamiento oportuno de posibles enfermedades del sistema digestivo, incluido el cancer de esofago, de estomago y colorrectal, reduciendo costos y tiempos de diagnóstico y tratamiento.

La fuente de inspiración y sustentación  a nivel médico y cientifico del proyecto y de los datos utilizados para la construcción del modelo, se encuentran en el paper: "Kvasir: A Multi-Class Image Dataset for Computer AidedGastrointestinal Disease Detection", cuyo enlace de acceso es: https://dl.acm.org/doi/pdf/10.1145/3083187.3083212. 
A esta fuente llegamos desde el sitio de Kaggle, https://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning/versions/1?resource=download, de donde descargamos los datos.

## Scope
* What data science solutions are we trying to build?

Se pretende construir una solución de deep learning, aplicando las técnicas de transfer learning y fine tuning, partiendo de un modelo base de redes convolucionales pre-entrenadas. Para posteriormente evaluarlos y compararlos mediante metricas de desempeño, como las medidas de accuracy, recall, precision y f1, y mediante la interpretación de las funciones de perdida y de accuracy en entrenamiento y validación, con el fin de seleccionar el modelo que mejor permita predecir el diagnóstico médico de nuevas imágenes endoscopicas gastrointestinales.
* What will we do?

Se partirá de la descarga del conjunto de imágenes de endoscopias gastrointestinales, etiquetadas según su diagnóstico y clasificadas en conjuntos de entrenamiento, test y validación. Cada imágen estan etiquetada con uno de los siguientes 4 posibles hallazgos:

/0_normal/: Corresponde a diagnostico normal (Sin
enfermadad).

/1_ulcerative_colitis/: Corresponde a diagnóstico de colitis ulcerosa.

/2_polyps/: Corresponde a diagnóstico de pólipos.

/3_esophagitis/: Corresponde a diagnóstio de esofagitis.

Como pre-procesamiento, para ampliar la cantidad y variedad de imagenes de entrenamiento, se aplicara data augmentation al conjunto de imagenes de entrenamiento para obtener nuevas imágenes transformadas (cambios en traslación, rotación, intensidad, entre otros). Adicionalmente se aplicara el pre-procesamiento de la red convolucional ResNet50V2 para escalar entre -1 y 1 los pixeles de las imágenes de entrada de los conjuntos de entrenamiento, test y validación. La ResNet50V2 se utilizará como modelo base para la extracción de características generales de las imágenes. Sobre este modelo se adicionaran las siguientes capas para la clasificación:

#Capa de global average pooling

pool = tf.keras.layers.GlobalAveragePooling2D()(extractor.output)

#capa densa con 32 neuronas y activación relu

dense1 = tf.keras.layers.Dense(32, activation="relu")(pool)

#Capa de dropout con taza de 0.2 para regularización

drop1 = tf.keras.layers.Dropout(0.2)(dense1)

#Capa densa de salida con 4 clases con activación softmax

dense2 = tf.keras.layers.Dense(4, activation="softmax")(drop1)

Se construirá un modelo de Transfer Learning y uno de Fine Tunning.

Se realizará entrenamiento de los modelos utilizando los siguientes parámetros:

Como función de perdida se utilizará "categorical_crossentropy". 

Optimizador Adam con lr=1e-3 para el modelo de Transfer Learning y lr=1e-4 para Fine Tunning.

metrics="accuracy"

batch_size = 32

epochs = 20

Se implementará la predicción de los modelos, mediante la cual se realizará la clasificación de diagnóstico de las nuevas imagenes de endoscopias gastrointestinales.


Los modelos será evaluados mediante las metricas de accuracy, recall, precision y f1, y mediante la interpretación de las funciones de perdida y de accuracy en entrenamiento y validación, con el fin de seleccionar el modelo que mejor permita predecir el diagnóstico médico de nuevas imágenes endoscopicas gastrointestinales.

* How is it going to be consumed by the customer?

## Personnel
* Who are on this project:
	* Microsoft:
		* Project lead
		
		
		* PM
		
		* Data scientist(s)
		
		
		* Account manager
	* Client:
		Clinicas y hospitales con servicios de endoscopía.
	* Data administrator: 
		Área de imagenes diagnósticas
	* Business contact: 
		Gastroenterologo endoscopista
	
## Metrics
* What are the qualitative objectives? (e.g. reduce user churn)

Mejorar la calidad de atención y el nivel de satisfacción de pacientes del área de gastroenterología en el proceso de diagnóstico de enfermedades gastrointestinales.

Contribuir en el diagnóstico temprano para el tratamiento oportuno de posibles enfermmedades gastrointestinales.

* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)

Reducir el tiempo de generación del diagnóstico de una endoscopía digestiva que tarda en promedio 180 segundos (30 minutos).

Reducir el porcentaje de costo en la generación del diagnístico de una endoscopía digestiva, que corresponde aproximadamente al 20% del salario del gastroenterologo endoscopista.

* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%)

Reducir el tiempo de generación del diagnóstico de una endoscopía digestiva pasando de 180 segundos a 10 segundos. 

Reducir en 20% el costo en la generación del diagnístico de una endoscopía digestiva.

* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)

Tiempo promedio de generación de diagnóstico actual = 2 diagnósticos por hora = 30 minutos (180 segundos) por diagnóstico.

Costo promedio de generación de diagnóstico actual = 20% del salario del gastroenterologo endoscopista.

* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)
 
Medida de la metrica del tiempo = tiempo promedio de generación de diagnóstico actual / tiempo en segundos de generación de un diagnóstico por parte de la solución.

Medida de la metrica de costo = costo actual - (costo actual * 20%)


## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.


## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)

Los datos de entrada al modelo corresponden a imágenes de endoscopías gastrointestinales, etiquetadas según el diagnóstico del especialista en gastroenterología endoscópica y a su vez clasificadas en carpetas de entrenamiento, test y validación. El archivo zip con estas imágenes se descargo de la página de Kaggle, en la siguiente ruta: https://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning/versions/1?resource=download.

* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
  * 
  Las herramientas utilizadas en la solución son las siguientes:
  
  Python. Como lenguaje de programación.
  
  Tensorflow. Como plataforma para la implementación de nuestra solución de machine learning.
  
  Keras. Paquete de Tensorflow para el pre-procesamiento de las imágenes, transformaciones con data augmentation, construcción y entrenamiento del modelo de deep learning.
  
  sklearn. Para evaluar el modelo con las metricas de accuracy, precision, recall y f1-score.
  
  numpy. Biblioteca utilizada para construir los arreglos de los conjuntos de imágenes para entrenamiento, test y validación.
  
   matplotlib. Biblioteca utilizada para la visualización de las imágenes y construcción de gráficos para visualizar el desempeño del modelo en términos de predicción, y las funciones de pérdida y accuracy.
  
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  
  El modelo será utilizado para generar de forma rápida el diagnóstico automatizado de una patología gastrointestinal, mediante la clasificación que realice de una imágen de endoscopía digestiva. Este diagnóstico será utilizado para  ofrecer tratamientos oportunos y acordes al diagnóstico generado, contribuyendo a una atención  más rápida a los pacientes que presenten alguna de estas patologías y disminuyendo costos en su atención.
  
    
  Como complemento, trasladamos textualmente del paper fuente (https://dl.acm.org/doi/epdf/10.1145/3083187.3083212), los siguientes aportes de un modelo como el que estamos proponiendo:
  
  "Automatic detection, recognition and assessment of pathological findings will probably contribute to reduce inequalities, improvequality and optimize use of scarce medical resources. Furthermore,since endoscopic examinations are real-time investigations, bothnormal and abnormal findings have to be recorded and documentedwithin written reports. Automatic report generation would proba-bly contribute to reduce doctors’ time required for paperwork andthereby increase time to patient care. Reliable and careful docu-mentation with the use of minimal standard terminology (MST) [1] may also contribute to improved patient follow-up and treatment".
  
 
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* How will we keep in touch? Weekly meetings?
* Who are the contact persons on both sides?
