# Informe del modelo de referencia

El modelo base es el modelo que un científico de datos entrenaría y evaluaría rápidamente después de tener el primer conjunto de características (preliminares) listo para el modelado de aprendizaje automático. A través de la construcción del modelo de referencia, el científico de datos puede tener una evaluación rápida de la viabilidad de la tarea de aprendizaje automático.


## Enfoque analítico
* ¿Cuál es la definición del objetivo?
* Contruir un algoritmo que nos permita clasificar de manera trimestral a las entidades con el fin de efocar los recusos para la IVC
* ¿Cuáles son las entradas (descripción)?
* Archivos xls y/o .xlsx con información de los catalogos trimestrales de información financiera. Los archivos se encuentran disponibles en la sección Estadisticas de los Sujetos Vigilados de las Cifras y Estadisticas de la SNS.
* ¿Qué tipo de modelo se ha construido?
Un modelo de clasificación no supervisado.

## Descripción del modelo

## Datos
* Fuentes:
  *BaseDatosMAML_Pry.xlsx: Tabla de información de cifras estadísticas de la SNS. los campos son los siguientes:
  
|Campo|  
|---|
|Año|
|Trim|
|Nombre EAPB|
|Ingresos|
|Costos|
|Gastos|
|Patrimonio|
|Utilidad Bruta|
|Utilidad Neta|
|Siniestralidad|
|Número de Afiliados|
    
* Selección: Datos desde primer trimestre de 2018 al cuarto trimestre de 2020
* Estadísticas: 43 Entidades Entidades Administradoras de Planes de Beneficios de Salud (EAPB)

## Algoritmo
* Se utiliza un algoritmo no supervisado Kmedias para clasificar de manera trimestral a las entidades con el fin de efocar los recusos para la IVC. Los campos utilizados para el modelo fueron los siguientes:

|Campo|Tipo|
|---|---:|
|Ingresos|int64|
|Costos|int64|
|Gastos|int64|
|Patrimonio|int64|
|Utilidad Neta|int64|
|Siniestralidad|float64|
|Número de Afiliados|int64|

## Resultados (Rendimiento del modelo)

* Métrica de evaluación usada para calcular el número de clusters fue suma del error al cuadrado (SSE).

|Num.|Clusters SSE|
|---|---:|
|1|1.6213123030975614e+27|
|2|6.80481535658991e+26|
|3|3.839870643364861e+26|
|4|2.4425205137292734e+26|
|5|1.8786419820582236e+26|
|6|1.5289181520697006e+26|
|7|1.2566962819578572e+26|
|8|1.0635556954993193e+26|
|9|9.604786788839818e+25|

* En la revisión de resultados se decide usar el modelo configurado en 5 clusters.

![Clusters Modelo base](https://user-images.githubusercontent.com/101413090/164133525-cee3241e-b26a-404c-859a-b30be938dc68.png)

*Se puede obsevar que los clustes se mezclan entre sí tomando un grafico de tres dimensiones enfocado a la Utilidad Neta, la Siniestralidad, y el número de afiliados.


El código de python usado se encuentra en: [Modelo_Base.py](https://github.com/CarlosAAcostaH/MAML/blob/main/Modelo_Base.py)

## Comprensión del modelo

* Importancia de las variables: Si bien todas las variables son importantes para el análsis unas dependen de otras. Un ejmplo es la utilidad neta que depende de los ingresos, los costos, los gastos.

## Conclusión y debates para los próximos pasos

* Conclusión sobre la evaluación de la viabilidad de la tarea de aprendizaje automático: Se verá analiza la posibilidad de disminuir las variables de clasificación del modelo.

* ¿Qué otras características pueden generarse a partir de los datos actuales?: Por ahora ninguna.

* Qué otras fuentes de datos relevantes están disponibles para ayudar al modelado: Por ahora ninguna
