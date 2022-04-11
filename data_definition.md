# Definiciones de datos y características

Este documento proporciona un eje central para las fuentes de datos brutos, los datos procesados/transformados y los conjuntos de características. En el informe de resumen de datos se ofrecen más detalles de cada conjunto de datos. 

Para cada dato, se proporciona un informe individual en el que se describe el esquema de datos, el significado de cada campo de datos y otra información útil para entender los datos. Si el conjunto de datos es el resultado del procesamiento/transformación/ingeniería de características de conjuntos de datos existentes, también se proporcionan los nombres de los conjuntos de datos de entrada y los enlaces a los scripts que se utilizan para realizar la operación. 

Para cada conjunto de datos, también se proporcionan los enlaces a los conjuntos de datos de muestra en el directorio _**Data**_. 

Para facilitar la modificación de este informe, se incluyen en esta página enlaces a marcadores de posición, por ejemplo, un enlace al conjunto de datos 1, pero sólo son marcadores de posición que apuntan a una página inexistente. Deben modificarse para que apunten a la ubicación real.

## Fuentes de datos brutos

|Nombre del conjunto de datos|Ubicación original|Ubicación de destino|Herramientas de movimiento de datos/Scripts|Enlace al informe |
| --- | --- | --- | --- | --- |
| Catalogos de información financiera | [Página web de la SNS](supersalud.gov.co) | Equipo local | Descarga manual de los libros de Microsoft Excel | [Informe]()
| Base de datos única de afiliados [BDUA](bdua.gov.co) | Confidencial, administrada por la [ADRES](adres.gov.co)| - | No se realiza copia de la base de datos al repositorio por su caracter confidencial | [Informe]()


* **Resumen de los Catalogos de información financiera**. <br> Contienen los planes únicos de cuentas de las EAPB de manera trimestral como tablas cruzadadas entre cada cuenta y entidades.

* **Resuemen de la BDUA**. <br> La BDUA contiene un registro por cada persona afiliada al sistema general de seguridad social en salud en Colombia y contiene campos de identificación y datos personales (nombre, documento, fecha de nacimiento, sitio de residencia entre otros), entidad a la cual se encuentra afilidado, estado de afiliación, etc.

## Datos procesados
| Nombre del conjunto de datos procesado | Conjunto(s) de datos de entrada | Herramientas de procesamiento de datos/Scripts | Enlace al informe
| :---:| :---: | :---: | :--- | 
|Listado de cuentas|Catalogos de información financiera|Organización manual de los datos debido a variaciones de formato entre los Catalogos de información financiera Procesamiento mediante Microsoft Power BI|[Informe]()
|Resumen de afiliados BDUA|BDUA|Procesamiento mediente SQL, Microsoft Excel, Microsoft Power Pivot y Microsoft Power BI (Bajo confidencialidad de la DIARI)|[Informe]()
* **Listado de cuentas**. Es la organización de todas las cuentas reportadas trimestralmente en la [SNS](supersalud.gov.co) con los campos año, trimestre, NIT de la EAPB, número de cuenta y valor.
* **Resumen de afiliados BDUA**. Indica la cantidad de afiliados clasificados por departamento de afiliación, género o sexo, grupo etario, régimen y EAPB

## Conjuntos de características

| Nombre del conjunto de características | Conjunto(s) de datos de entrada | Herramientas/Scripts de ingeniería de características | Enlace al informe
| :---:| :---: | :---: | :---  
| Resultados financeros | Listado de cuentas | [Resultados Financieros.pbix]()|[Informe]()
| Número de afiliados | Resumen de afiliados BDUA|Procesamiento con Microsoft Excel|[Informe]()

* **Resultados financieros**. Corresponden a variables financieras de cada entidad tales como: 
    * Ingresos
    * Gastos
    * Costos
    * Patrimonio
    * Utilidad bruta
    * Utilidad neta
    * Siniestralidad contable

* **Número de afiliados**. Correspondiente a la suma de afiliados de toda una EAPB descartando el resto de campos reportados en la BDUA
