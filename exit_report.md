# Informe de salida del proyecto **Clasificador de EAPB** para el cliente **Contraloría Delegada para el Sector Salud (CDSS)**

Instrucciones: Plantilla de criterios de salida para proyectos de ciencia de datos. Se trata de un documento conciso que incluye una visión general de todo el proyecto, con detalles de cada etapa y aprendizaje. Si una sección no es aplicable (por ejemplo, el proyecto no incluyó un modelo ML), simplemente marque esa sección como "No aplicable". Se sugiere una longitud de entre 5 y 20 páginas. El código debe estar en su mayor parte en el repositorio de código (no en este documento).

**Cliente:** Contraloría Delegada para el Sector Salud (CDSS)

**Miembros del equipo:**
* Ing. David Hernández Chinchilla (Jefe de proyecto, director de cuentas y cientifico de datos)
* Ing. Carlos Arturo Acosta Herrera (PM, enlace con el cliente y cientifico de datos)

## Resumen

El clasificador segmenta las EAPB en cuatro subconjuntos de entidades con caracteristicas similares entre ellas con el fin de identificar las EPS y CCF en las que se deben dedicar una mayor cantidad de recursos para la IVC.

## Dominio de negocio
El cliente desarrolla la investigación, vigilancia y control (IVC) de las entidades que administran recursos del sector salud o relacionados con el Sistema General de Seguridad Social en Salud de Colombia (SGSSS). Entre los sujetos de control del cliente se encuentran las Entidades Administradoras de Planes de Beneficios (EAPB) entre las que se encuentran las Empresas Promotoras de Salud (EPS) y algunas Cajas de Compensación Familar (CCF) que prestan servicios de salud.

## Problema de negocio
La CDSS en la actualidad tiene 57 sujetos de control entre los que se encuentran 34 EPS, en operación o en liquidación, sumado al hecho que debe vigilar los recursos de salud de 11 CCF (sujetos de control de la Contraloría Delegada para el Sector Trabajo como entidad, pero la CDSS vigila los recursos del SGSSS). La CDSS intenta realizar la IVC de todas las EAPB, sin embargo, debido a la limitación de recursos, solo puede realizar anualmente auditorias a un número limitado de ellas, usualmente siguiendo un cronograma. La CDSS necesita identificar un subconjunto de EAPB con ciertas caracteristicas que las hacen más suceptibles a un manejo inadecuado de recursos para invertir una mayor cantiad de recursos en la IVC.

## Procesamiento de datos
El modelo tiene 2 bases de datos:
* Base de Datos Única de Afiliados, BDUA: Reporte de todos los afiliados al SGSSS en Colombia. Confidencial administrada por la ADRES.
* Catalogos de información financiera: Planes únicos de cuentas de frecuencia trimestral. Público reportado por las EAPB a la SNS.
La información se procesa mediente SQL, Microsft Excel y Microsoft Power BI para obtener:
* Ingresos
* Gastos
* Costos
* Patrimonio
* Utilidad bruta
* Utilidad neta
* Siniestralidad contable
* Número de afiliados

## Modelización, validación
La categorización se realiza mediante un k-means usando las variables Utilidad Neta, Siniestralidad y número de afiliados. El número de clusters, k, se determina mediante la suma de error cuadrado o SSE.

## Arquitectura de la solución
![Diagrama de la arquitectura](https://github.com/CarlosAAcostaH/MAML/blob/main/arquitectura.png)

## Beneficios
	
### Beneficio para el cliente
La CDSS puede identificar las EAPB a las cuales debe aumentar la IVC, ergo, puede disminuir el riesgo de perdidas de los recursos del SGSSS y aumentar la productividad de las auditorias a realizar.

## Aprendizajes

### Ejecución del proyecto
En el sector salud, la decisión acerca de la intervención de la SNS a una EAPB depende de muchas variables, algunas de ellas no cuantificables, por lo que no se recomienda hacer un predictor de las acciones de la SNS, sino una descripción de las EAPB que permita enfocar los recursos que se usan en la IVC.

### Ciencia de los datos / Ingeniería
En la medida de lo posible, se debe realizar el modelado con base en información no confidencial que no comprometa o limite el entrenamiento y/o distribución de las bases de datos

## Próximos pasos
Se debe incluir información de otras bases de datos como la cantidad de PQRS o indicadores de calidad de atención.
