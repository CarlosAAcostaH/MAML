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
* Arquitectura simple de la solución (fuentes de datos, componentes de la solución, flujo de datos)
* ¿Cuál es la salida?

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
    Año                      int64
    Trim                    object
    Nombre EAPB             object
    Ingresos                 int64
    Costos                   int64
    Gastos                   int64
    Patrimonio               int64
    Utilidad Bruta           int64
    Utilidad Neta            int64
    Siniestralidad         float64
    Número de Afiliados      int64

## Algoritmo
* Descripción o imágenes del gráfico de flujo de datos
  ## Si es AzureML, enlace a:
    * Experimento de entrenamiento
    * Flujo de trabajo de puntuación
* ¿Qué aprendiz(es) se utilizó(n)?
* Hiperparámetros del aprendiz

## Resultados
* Gráficos ROC/Lift, AUC, R^2, MAPE, según proceda
* Gráficos de rendimiento para los barridos de parámetros, si procede
