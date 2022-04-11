# Informe de datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos
Los datos tienen una periodicidad trimestral desde el 2018 hasta el 2021. La cantidad de EAPB reportadas varia de acuerdo con el trimestre reportado debido a pueden crearse o entrar en proceso de liquidación, ya sea voluntaria o mediante la medida de intervención forzosa administrativa para liquidar. La decisión de liquidación forzosa por parte de la SNS, se realiza basado en los indicadores de las EAPB y su evolución, sin embargo, no existe un protocolo o metodología adecuada para definir la liquidación o no de una entidad.

Desde el 2014, han estado en funcionamiento por lo menos 72 entidades diferentes, de las cuales, con corte a enero de 2022, 25 ya se encuentran liquidadas, 1 está en proceso de liquidación voluntaria, 10 estan en proceso de liquidación forzosa y las 36 restantes se encuentran en funcionamiento.


## Resumen de la calidad de los datos
Las bases de datos no tienen datos erroneos o faltantes, sin embargo, una de las bases no tiene un diseño estandarizado para automatizar su preprocesamiento, mientras que la otra, por la información reportada, es confidencial y solo se tiene acceso de manera indirecta.

## Variable objetivo
La variable objetivo es la probabilidad de que se ordene la medida de intervención forzosa administrativa para administrar por parte de la SNS. Para los datos de entrenamiento será una variable dicotomica con valor de cero (0) para las EAPB que no entran en liquidación en los 3 meses siguientes a los datos reportados y uno (1) para las entidades que liquidaron.

## Variables individuales
|Variable|Definición|Tipo|
| --- | --- | --- |
|Ingresos| Ingresos de la EAPB sin importar la fuente de los mismos. Corresponde a la suma de las cuentas que inician por 4101, 4102, 4311, 4312 o 4705. |Decimal fijo con 2 decimales
|Costos| Son los egresos asociados a la prestación de los servicios de salud de sus afiliados. Corresponde a la suma de las cuentas que empiezan por 6, 5372 o 5613. | Decimal fijo con 2 decimales
|Gastos| Desembolsos asociados al funcionamiento de la EAPB, más no directamente con la atención. Corresponde a la suma de las cuentas que empiezan con 5, excepto las que empiezan por 5372, 5613, 5601 o 5905.|Decimal fijo con dos decimales
|Utilidad Neta|Ganancias o perdidas de acuerdo con lo registrado en el plan único de cuentas. Corresponde a la suma de las cuentas que empiezan por 5601 o 5905.|Decimal fijo con 2 decimales
|Utilidad Bruta|Diferencia entre los Ingresos y los Costos.|Decimal fijo con 2 decimales
|Siniestralidad contable|Cociente entre los Costos y los Ingresos, expresado como un porcentaje.|Decimal en punto flotante
|Patrimonio|Correspondiente a la suma de las cuentas que empiezan por 3.|Decimal fijo con 2 decimales
|Número de afiliados|Suma de los afiliados por cada EAPB a nivel nacional para cualquier sexo, grupo etario o región de afiliación|Entero positivo

## Clasificación de las variables

## Relación entre las variables explicativas y la variable objetivo


