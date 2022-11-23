# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

For each data, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided. 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided. 

_**For ease of modifying this report, placeholder links are included in this page, for example a link to dataset 1, but they are just placeholders pointing to a non-existent page. These should be modified to point to the actual location.**_

## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
|train |Los datos para train se descargan,  como archivo zip, manualmente con la opción "Download" de la siguiente página de Kaggle, ingresando con usuario registrado https://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning, posteriormente se suben a la siguiente dirección de GoogleDrive, https://drive.google.com/file/d/1TBS_el84d3lEgrNTbXezzLt6T1SYk0mV/view?usp=share_link, para de allí ser descargados en ruta temporal de GoogleColab  | Brief description of its destination location | [script1.py](link/to/python/script/file/in/Code) | [Dataset 1 Report](https://github.com/margomeza16/MiRepositorio/blob/main/data_dictionary.md)|
| test| Los datos para test se descargan,  como archivo zip, manualmente con la opción "Download" de la siguiente página de Kagglehttps://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning | Brief description of its destination location | [script2.R](link/to/R/script/file/in/Code) | [Dataset 2 Report](https://github.com/margomeza16/MiRepositorio/blob/main/data_dictionary.md)|
| val| Los datos para validación se descargan,  como archivo zip, manualmente con la opción "Download" de la siguiente página de Kagglehttps://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning | Brief description of its destination location | [script3.py](link/to/R/script/file/in/Code) | [Dataset 3 Report](https://github.com/margomeza16/MiRepositorio/blob/main/data_dictionary.md)|

* Dataset1 summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset1 Report.>
* Dataset2 summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset2 Report.> 

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
