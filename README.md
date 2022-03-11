# Project charter

## Antecedentes empresariales

* **Quién es el cliente, en qué ámbito empresarial se encuentra el cliente.**  
El cliente es la Contraloría Delegada para el Sector Salud (CDSS) dentro de un estudio que se encuentra en desarrollo acerca de la Evaluación de la Intervención de Entidades Administradoras de Planes de Beneficios (EAPB: EPS, Entidades Adaptadas y Cajas de Compensación que prestan servicios de salud) por parte de la Superintendencia Nacional de Salud (SNS)
* **¿Qué problemas empresariales se pretenden resolver?**  
El principal problema es el desconocimiento de las EAPB entraran en la medida de *Intervención forzosa para liquidar*, por parte de la SNS, que afectaría a los afiliados, a los prestadores (IPS y proveedores) y a los empleados, dentro del marco del estudio sectorial.

## Alcance
* **¿Qué soluciones de ciencia de datos estamos tratando de construir?**  
Un algoritmo que nos permita medir la probabilidad de entrar a la medida especial de *Intervención forzosa para liquidar* por parte de la SNS dentro del próximo trimestre.

* **¿Qué vamos a hacer?**  
Un predictor de probabilidad de entrar en liquidación dentro del próximo trimestre.

* **¿Cómo va a ser consumido por el cliente?**  
Mensualmente se emitirá la probabilidad de entrar en liquidación forzosa de cada EAPB que se encuentra en operación.

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
Poder predecir las EAPB que entrarán en la medida especial de *Intervención Forzosa Administrativa para Liquidar* por parte de la SNS dentro del próximo trimestre.
* **¿Cuáles son las métricas cuantificables (por ejemplo, reducir la fracción de usuarios con 4 semanas de inactividad)**    
[Valor o puntaje F<sub>1</sub>](https://es.wikipedia.org/wiki/Valor-F "Wikipedia:Valor F") máximo (F<sub>1 máx</sub>) definido como la media armonica máxima de precisión y exhaustividad (precision and recall)
* **Cuantificar qué mejora de los valores de la métrica es útil para el escenario del cliente (por ejemplo, reducir la fracción de usuarios con inactividad de 4 semanas en un 20%)**  
* **¿Cuál es el valor de referencia (actual) de la métrica? (por ejemplo, fracción actual de usuarios con inactividad de 4 semanas = 60%)**  
Actualmente, no existe un predictor de medidas especiales de EAPB, por lo tanto, no existe un valor de refencia de la métrica. No obstante, se puede encontrar la probabilidad *a priori* de que una EAPB entre en liquidación del 3,44% que retornaría un F<sub>1 máx</sub> de 0,33;
* **¿Cómo mediremos la métrica? (por ejemplo, prueba A/B en un subconjunto específico durante un periodo determinado; o comparación del rendimiento después de la implementación con la línea de base)**  
Se realizará una división de los datos de entrenamiento, validación y prueba de 80%, 10% y 10%, respectivamente. Se comparará la predicción con la etiqueta de cada dato obteniendo la curva de *precision-recall* para posteriormente encontrar el valor de F<sub>1</sub> más alto.
## Plan
* Fases (hitos), calendario, breve descripción de lo que haremos en cada fase.

## Arquitectura
* **Datos**
	* **¿Qué datos esperamos? Datos en bruto en las fuentes de datos del cliente (por ejemplo, archivos on-prem, SQL, Hadoop on-prem, etc.)**  
	Archivos .csv, .xls y/o .xlsx con información de los catalogos trimestrales de información financiera e informes ejecutivos mensuales de Preguntas, Quejas, Reclamos y/o 	Denuncias (PQRD) formuladas por los usuarios. Los archivos se encuentran disponibles en la sección *Estadisticas de los Sujetos Vigilados* de las [Cifras y Estadisticas de la SNS](https://www.supersalud.gov.co/es-co/nuestra-entidad/cifras-y-estadisticas "Supersalud: Cifras y Estadisticas").
* **Movimiento de datos desde on-prem a Azure utilizando ADF u otras herramientas de movimiento de datos (Azcopy, EventHub, etc.) para mover**
  * Los datos se descargaran y se transformaran para su uso tanto de entrenamiento como validación
  * Los datos se copiarán al servidor facilitado para el desarrollo del curso
  * Se realizará el entrenamiento y validación del modelo en el servidor. 
  * El modelo entrenado se copiará a los computadores locales para realizar su despliegue a traves de una API.

* **Qué herramientas y recursos de almacenamiento/análisis de datos se utilizarán en la solución, por ejemplo**
  * Microsoft Excel® y Microsoft Power BI® para la transformación de los datos.
  * Python con la libreria TensorFlow para el diseño, entrenamiento y validación del modelo
* **¿Cómo se consumirá la puntuación o el servicio(s) web operacionalizado(s) (RRS y/o BES) en el flujo de trabajo empresarial del cliente? Si procede, escriba el pseudocódigo de las API de las llamadas al servicio web.**
  * **¿Cómo utilizará el cliente los resultados del modelo para tomar decisiones?**
  	El cliente emitirá recomendaciones a sus sujetos de control para prevenir contratiempos tanto a los usuarios del Sistema General de Seguridad Social en Salud (SGSSS) y evitar un detrimento de los recusos de la salud en Colombia
  * **Canalización del movimiento de datos en producción**
  	
  * **Haga un diagrama de 1 diapositiva que muestre el flujo de datos de extremo a extremo y la arquitectura de decisiones**
  
  * **Si hay un cambio sustancial en el flujo de trabajo del negocio del cliente, haga un diagrama antes/después que muestre el flujo de datos.**

## Comunicación
* **¿Cómo nos mantendremos en contacto? ¿Reuniones semanales?**
Se realizará, por lo menos, una reunión semanal de una hora, exclusiva para coordinar y desarrollar el proyecto. Las reuniones se realizaran mediante la plataforma Microsoft Teams® en el horario acordado por el personal que no se cruce con las labores propias de su trabajo como funcionario.
* **¿Quiénes son las personas de contacto de ambas partes?**
El ingeniero Carlos Arturo Acosta Herrera, al hacer parte tanto del grupo desarrollador como del cliente, fungirá funciones como el enlace entre las partes.

