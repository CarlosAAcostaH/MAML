
#Informe del modelo final
Informe que describe el modelo final que se entregará - normalmente compuesto por uno o más de los modelos construidos durante la vida del proyecto_.

## Enfoque analítico
* ¿Cuál es la definición del objetivo?
* Contruir un algoritmo que nos permita clasificar de manera trimestral a las entidades con el fin de efocar los recusos para la IVC
* ¿Cuáles son las entradas (descripción)?
* Archivos xls y/o .xlsx con información de los catalogos trimestrales de información financiera. Los archivos se encuentran disponibles en la sección Estadisticas de los Sujetos Vigilados de las Cifras y Estadisticas de la SNS.
* ¿Qué tipo de modelo se ha construido?
Un modelo de clasificación no supervisado.

## Descripción de la solución

## Datos
* Fuentes:
  *BaseDatosMAML_Pry.xlsx: Tabla de información de cifras estadísticas de la SNS. los campos son los siguientes:
    Año
    Trim
    Nombre EAPB
    Ingresos
    Costos
    Gastos
    Patrimonio
    Utilidad Bruta
    Utilidad Neta
    Siniestralidad
    Número de Afiliados
    
* Selección: Datos desde primer trimestre de 2018 al cuarto trimestre de 2020
* Estadísticas: 43 Entidades Entidades Administradoras de Planes de Beneficios de Salud (EAPB)

## Características
* Lista de características brutas de los campos:

|Campo|Tipo|
|---|---:|
|Año|int64|
|Trim|object|
|Nombre EAPB|object|
|Ingresos|int64|
|Costos|int64|
|Gastos|int64|
|Patrimonio|int64|
|Utilidad Bruta|int64|
|Utilidad Neta|int64|
|Siniestralidad|float64|
|Número de Afiliados|int64|

## Arqutectura

Se realiza una ejecución local debido a que son datos sensibles.

## Algoritmo
* Se utiliza un algoritmo no supervisado Kmedias para clasificar de manera trimestral a las entidades con el fin de efocar los recusos para la IVC. Los campos utilizados para el modelo fueron los siguientes:

|Campo|Tipo|
|---|---:|
|Utilidad Neta|int64|
|Siniestralidad|float64|
|Número de Afiliados|int64|

## Resultados
* Métrica de evaluación usada para calcular el número de clusters fue suma del error al cuadrado (SSE).

|Num.|Clusters SSE|
|---|---:|
|1 | 1.2032992573181158e+25|
|2 | 5.784851127505816e+24|
|3 | 2.852664430997615e+24|
|4 | 1.6249980121034142e+24|
|5 | 1.16751799728549e+24|
|6 | 7.997256040165846e+23|
|7 | 5.460403211063597e+23
|8 | 3.740920109844167e+23|
|9 | 2.9200992203086773e+23|

* En la revisión de resultados se decide usar el modelo configurado en 4 clusters.

![Clusters Modelo Final](https://user-images.githubusercontent.com/101413090/164131205-6aeafc73-1d7e-4584-92cc-d0ed14fb372b.png)

El código de python usado se encuentra en: [Modelo_Final.py](https://github.com/CarlosAAcostaH/MAML/blob/main/Modelo_Final.py)

## Salidas

Archivo de Excel llamado 'Modelo_Final.xlsx' el cual tiene los cluster de cada registro.
