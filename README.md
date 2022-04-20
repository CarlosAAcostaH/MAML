# Project charter

## Antecedentes empresariales

* **Quién es el cliente, en qué ámbito empresarial se encuentra el cliente.**  
El cliente es la Contraloría Delegada para el Sector Salud (CDSS) dentro de un estudio que se encuentra en desarrollo acerca de la Evaluación de la Intervención de Entidades Administradoras de Planes de Beneficios (EAPB: EPS, Entidades Adaptadas y Cajas de Compensación que prestan servicios de salud) por parte de la Superintendencia Nacional de Salud (SNS)
* **¿Qué problemas empresariales se pretenden resolver?**  
El principal problema es el desconocimiento de las caracteristicas de las EAPB que permita enfocar los recursos para la inspección, vigilacia y control (IVC)  de estas entidades, dentro del marco del estudio sectorial.

## Alcance
* **¿Qué soluciones de ciencia de datos estamos tratando de construir?**  
Un algoritmo que nos permita clasificar de manera trimestral a las entidades con el fin de efocar los recusos para la IVC.

* **¿Qué vamos a hacer?**  
Un categorizador de EAPB de acuerdo a la información financiera y número de afiliados de un trimestre.

* **¿Cómo va a ser consumido por el cliente?**  
Trimestralmente se emitirá la categoriación de las EAPB con la descripción de las varibles para cada categoría que permitan definir un número reducido de entidades donde se va a enfocar la IVC.

## Personal
* **¿Quiénes están en este proyecto?**
	* **Grupo 9:**
		* **Jefe de proyecto:** Ing. David Hernández Chinchilla
		* **PM:** Ing. Carlos Arturo Acosta Herrera
		* **Científico(s) de datos:**
			* Ing. David Hernández Chinchilla
			* Ing. Carlos Arturo Acosta Herrera
		* **Director de cuentas:** Ing. David Hernández Chinchilla
	* **Cliente:**
		* **Administrador de datos:** Dirección de Estudios Sectoriales, Contraloría Delegada para el Sector Salud
		* **Contacto con la empresa:** Ing. Carlos Arturo Acosta Herrera
	
## Métricas
* **¿Cuáles son los objetivos cualitativos? (por ejemplo, reducir la fuga de usuarios)**  
Generar un categorizador de EAPB de acuerdo con la información financiera y número de usuarios de un trimestre.
* **¿Cuáles son las métricas cuantificables (por ejemplo, reducir la fracción de usuarios con 4 semanas de inactividad)**    
Cohesión de los clúster de acuerdo con la suma del error cuadrado. ([SSE](https://disi.unal.edu.co/~eleonguz/cursos/mda/presentaciones/validacion_Clustering.pdf)). SSE se define como la suma de la distancia al cuadrado entre el centroide y cada miembro del clúster.
* **Cuantificar qué mejora de los valores de la métrica es útil para el escenario del cliente (por ejemplo, reducir la fracción de usuarios con inactividad de 4 semanas en un 20%)**  
* **¿Cuál es el valor de referencia (actual) de la métrica? (por ejemplo, fracción actual de usuarios con inactividad de 4 semanas = 60%)**  
Actualmente, no existe categorizador de EAPB, por lo tanto, no existe un valor de refencia de la métrica.
* **¿Cómo mediremos la métrica? (por ejemplo, prueba A/B en un subconjunto específico durante un periodo determinado; o comparación del rendimiento después de la implementación con la línea de base)**  
Se modificarán las variables usadas para la clusterización con el fin de generar el modelo más simple que pueda realizar una categorización.
## Plan
* Fases (hitos), calendario, breve descripción de lo que haremos en cada fase.

## Arquitectura
* **Datos**
	* **¿Qué datos esperamos? Datos en bruto en las fuentes de datos del cliente (por ejemplo, archivos on-prem, SQL, Hadoop on-prem, etc.)**  
	Archivos .csv, .xls y/o .xlsx con información de los catalogos trimestrales de información financiera. Los archivos se encuentran disponibles en la sección *Estadisticas de los Sujetos Vigilados* de las [Cifras y Estadisticas de la SNS](https://www.supersalud.gov.co/es-co/nuestra-entidad/cifras-y-estadisticas "Supersalud: Cifras y Estadisticas").
* **Movimiento de datos desde on-prem a Azure utilizando ADF u otras herramientas de movimiento de datos (Azcopy, EventHub, etc.) para mover**
  * Los datos se descargaran y se transformaran para su uso.
  * Los datos se procesaran en los equipos propios de la CGR debido a la sensibilidad y confidencialidad de parte de ellos.
  * El categorizador se usará trimestralmente y sus resultados se transmitiran al cliente.

* **Qué herramientas y recursos de almacenamiento/análisis de datos se utilizarán en la solución, por ejemplo**
  * SQL, Microsoft Excel® y Microsoft Power BI® para la transformación de los datos.
  * Python para el entrenamiento y evaluación del modelo
* **¿Cómo se consumirá la puntuación o el servicio(s) web operacionalizado(s) (RRS y/o BES) en el flujo de trabajo empresarial del cliente? Si procede, escriba el pseudocódigo de las API de las llamadas al servicio web.**
  * **¿Cómo utilizará el cliente los resultados del modelo para tomar decisiones?**
  	El cliente determinará, a partir de las descripciones de las variables de cada cluster, en cual de ellos debe invertir más recursos para la IVC de las EAPB.
  * **Canalización del movimiento de datos en producción**
  	
  * **Haga un diagrama de 1 diapositiva que muestre el flujo de datos de extremo a extremo y la arquitectura de decisiones**
  
  * **Si hay un cambio sustancial en el flujo de trabajo del negocio del cliente, haga un diagrama antes/después que muestre el flujo de datos.**

## Comunicación
* **¿Cómo nos mantendremos en contacto? ¿Reuniones semanales?**
Se realizará, por lo menos, una reunión semanal de una hora, exclusiva para coordinar y desarrollar el proyecto. Las reuniones se realizaran mediante la plataforma Microsoft Teams® en el horario acordado por el personal que no se cruce con las labores propias de su trabajo como funcionario.
* **¿Quiénes son las personas de contacto de ambas partes?**
El ingeniero Carlos Arturo Acosta Herrera, al hacer parte tanto del grupo desarrollador como del cliente, fungirá funciones como el enlace entre las partes.

