# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

For each data, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided. 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided. 

_**For ease of modifying this report, placeholder links are included in this page, for example a link to dataset 1, but they are just placeholders pointing to a non-existent page. These should be modified to point to the actual location.**_

## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
|train |Los datos para entrenamiento se descargan manualmente,  como archivo zip, con la opción "Download" de la siguiente página de Kaggle, ingresando con usuario registrado,  https://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning. Posteriormente se suben manualmente a la siguiente dirección de GoogleDrive: https://drive.google.com/file/d/1BwSoPrJzTLndqMjBMThOWr-qQe7FbOyU/view?usp=share_link, para de allí ser descargados en ruta temporal de GoogleColab.  | El archivo train.zip se descarga y descomprime en la siguiente ruta temporal de GoogleColab: /tmp/train/  | [descarga_file.py](https://github.com/margomeza16/mlds6_proyecto/blob/master/docs/data/descarga_file.py) | [Dataset 1 Report](https://github.com/margomeza16/mlds6_proyecto/blob/master/docs/data/data_dictionary.md)|
| test| Los datos para test se descargan manualmente,  como archivo zip, con la opción "Download" de la siguiente página de Kaggle, ingresando con usuario registrado,  https://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning. Posteriormente se suben manualmente a la siguiente dirección de GoogleDrive: https://drive.google.com/file/d/1AQWlyBOm9EG6tQOSk5HNbpHkpSCSVr0Y/view?usp=share_link, para de allí ser cargados en ruta temporal de GoogleColab.| El archivo test.zip se descarga y descomprime en la siguiente ruta temporal de GoogleColab: /tmp/test/ | [descarga_file.py](https://github.com/margomeza16/mlds6_proyecto/blob/master/docs/data/descarga_file.py) | [Dataset 2 Report](https://github.com/margomeza16/mlds6_proyecto/blob/master/docs/data/data_dictionary.md)|
| val| Los datos para validación se descargan manualmente,  como archivo zip, con la opción "Download" de la siguiente página de Kaggle, ingresando con usuario registrado, https://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning. Posteriormente se suben manualmente a la siguiente dirección de    GoogleDrive: https://drive.google.com/file/d/1TBS_el84d3lEgrNTbXezzLt6T1SYk0mV/view?usp=share_link, para de allí ser descargados en ruta temporal de GoogleColab.| El archivo val.zip se descarga y descomprime en la siguiente ruta temporal de GoogleColab: /tmp/val/ | [descarga_file.py](https://github.com/margomeza16/mlds6_proyecto/blob/master/docs/data/descarga_file.py) | [Dataset 3 Report](https://github.com/margomeza16/mlds6_proyecto/blob/master/docs/data/data_dictionary.md)|

* Dataset1 summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset1 Report.>

train.zip: Archivo zip descargado de la página de Kaggle, desde la dirección indicada en el cuadro anterior. Contiene 3200 imágenes de endoscopías en formato JPG, con diferentes resoluciones, que van desde 720x576 hasta 1920x1072 píxeles, que corresponden al conjunto de entrenamiento, separadas en 4 carpetas según el diagnóstico del especialista, cada clase de diagnóstico contiene 800 imágenes. El archivo se encuentra en GoogleDrive y se puede acceder  a través del siguiente link: https://drive.google.com/file/d/1BwSoPrJzTLndqMjBMThOWr-qQe7FbOyU/view?usp=share_link.

* Dataset2 summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset2 Report.> 

test.zip: Archivo zip descargado de la página de Kaggle, desde la dirección indicada en el cuadro anterior. Contiene 800 imágenes de endoscopías en formato JPG, con diferentes resoluciones, que van desde 720x576 hasta 1920x1072 píxeles, que corresponden al conjunto de pruebas, separadas en 4 carpetas según la clase de diagnóstico del especialista, cada clase de diagnóstico contiene 200 imágenes. El archivo se encuentra en GoogleDrive y se puede acceder  a través del siguiente link: https://drive.google.com/file/d/1AQWlyBOm9EG6tQOSk5HNbpHkpSCSVr0Y/view?usp=share_link.

* Dataset3 summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset3 Report.> 

val.zip: Archivo zip descargado de la página de Kaggle, desde la dirección indicada en el cuadro anterior. Contiene 2000 imágenes de endoscopías en formato JPG, con diferentes resoluciones, que van desde 720x576 hasta 1920x1072 píxeles, que corresponden al conjunto de pruebas, separadas en 4 carpetas según la clase de diagnóstico del especialista, cada clase de diagnóstico contiene 500 imágenes. El archivo se encuentra en GoogleDrive y se puede acceder  a través del siguiente link: https://drive.google.com/file/d/1TBS_el84d3lEgrNTbXezzLt6T1SYk0mV/view?usp=share_link.

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset 1 | [Dataset1](link/to/dataset1/report), [Dataset2](link/to/dataset2/report) | [Python_Script1.py](link/to/python/script/file/in/Code) | [Processed Dataset 1 Report](link/to/report1)|
| Processed Dataset 2 | [Dataset2](link/to/dataset2/report) |[script2.R](link/to/R/script/file/in/Code) | [Processed Dataset 2 Report](link/to/report2)|
* Processed Data1 summary. <Provide brief summary of the processed data, such as why you want to process data in this way. More detailed information about the processed data should be in the Processed Data1 Report.>
* Processed Data2 summary. <Provide brief summary of the processed data, such as why you want to process data in this way. More detailed information about the processed data should be in the Processed Data2 Report.> 

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|
| Feature Set 2 | [Processed Dataset2](link/to/dataset2/report) |[SQL_Script2.sql](link/to/sql/script/file/in/Code) | [Feature Set2 Report](link/to/report2)|

* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>
* Feature Set2 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set2 Report.> 
