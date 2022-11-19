# Project Charter

## Business background

* Who is the client, what business domain the client is in. 

Este proyecto esta  dirigido al sector salud, con el objetivo de apoyar el diagnóstico automatizado de enfermedades digestivas y del colon a partir de imágenes endoscópicas gastrointestinales. El cliente son las áreas de gastroenterología de las clinicas y hospitales del sector salud y el usuario directo es el médico especialista en gastroentrologia.
* What business problems are we trying to address?

El problema de negocio a abordar en este proyecto es el diagnóstico automatizado de enfermedades digestivas y del colon a partir de imágenes endoscópicas gastrointestinales. Esto con el propósito de apoyar el diagnóstico temprano y tratamiento oportuno de posibles enfermedades del sistema digestivo, incluido el cancer colorectal, reduciendo costos y tiempos de diagnóstico y tratamientos.

## Scope
* What data science solutions are we trying to build?

Se pretende construir una solución de deep learning, aplicando las técnicas de transfer learning y fine tuning, partiendo de un modelo base de redes convolucionales pre-entrenadas. Para posteriormente evaluarlos y compararlos mediante metricas de desempeño, como las medidas de accuracy, recall, precision y f1, y mediante la interpretación de las funciones de perdida y de accuracy en entrenamiento y validación, con el fin de seleccionar el modelo que mejor permita predecir el diagnóstico médico de nuevas imágenes endoscopicas gastrointestinales.
* What will we do?
* How is it going to be consumed by the customer?

## Personnel
* Who are on this project:
	* Microsoft:
		* Project lead
		* PM
		* Data scientist(s)
		* Account manager
	* Client:
		* Data administrator
		* Business contact
	
## Metrics
* What are the qualitative objectives? (e.g. reduce user churn)

Mejorar el nivel de satisfacción de pacientes del área de gastroenterología en el proceso de diagnóstico de enfermedades gastrointestinales.

Contribuir en el diagnóstico temprano para el tratamiento oportuno de posibles enfermmedades gastrointestinales.

* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)

Reducir el tiempo de generación del diagnóstico de una endoscopía digestiva que tarda en promedio 180 segundos (30 minutos).

Reducir el porcentaje de costo en la generación del diagnístico de una endoscopía digestiva, que corresponde aproximadamente al 20% del salario del gastroenterologo endoscopista.

* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%)

Reducir el tiempo de generación del diagnóstico de una endoscopía digestiva pasando de 180 segundos a 5 segundos. 

Reducir en 20% el costo en la generación del diagnístico de una endoscopía digestiva.

* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)

Tiempo promedio de generación de diagnóstico actual = 2 diagnósticos por hora = 30 minutos (180 segundos) por diagnóstico.

Costo promedio de generación de diagnóstico actual = 20% del salario del gastroenterologo endoscopista.

* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)
* 
Medida de la metrica del tiempo = tiempo promedio de generación de diagnóstico actual / tiempo en segundos de generación de un diagnóstico por parte de la solución


## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.

## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* How will we keep in touch? Weekly meetings?
* Who are the contact persons on both sides?
