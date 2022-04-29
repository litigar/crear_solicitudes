# Creación masiva de solicitudes de Radicaciones
> Aplicacion cliente que consume un servicio de la api de litigar, para crear masivamente solicitudes de radicaciones con y sin procesos en vigilancia.
## 1 Instalación
[![Alt text](https://img.youtube.com/vi/IuKBZi6Q6T8/0.jpg)](https://www.youtube.com/watch?v=IuKBZi6Q6T8)
## 2 Configuración 
[![Alt text](https://img.youtube.com/vi/huBIRNwKX2w/0.jpg)](https://www.youtube.com/watch?v=huBIRNwKX2w)
## 3 Ejecución 
[![Alt text](https://img.youtube.com/vi/QhFxCcpSfsg/0.jpg)](https://www.youtube.com/watch?v=QhFxCcpSfsg)
## 4 Actualización 
- Cuando se modifique la funcionalidad al programa, se informará para que descarguen e instalen la nueva versión 
[![Alt text](https://img.youtube.com/vi/qQy0Ja1Xct4/0.jpg)](https://www.youtube.com/watch?v=qQy0Ja1Xct4)
# Versionamiento
- Fecha primera versión: 14/04/2022
- Fecha ultima actualización: 29/04/2022
* Python >3.6.2 +
# Instalación
## 1. Instale python desde la siguiente ruta:
> https://www.python.org/downloads/
## 2. Descargue y Descomprima el proyecto
- Descargue el proyecto desde github, ya sea desde un archivo zip (descomprímirlo) o por github
> https://github.com/litigar/crear_solicitudes.git
- Descomprima el archivo zip
- Copie la carpeta descomprimida en la raíz de alguna unidad, para el ejemplo se coloca en C:\crear_solicitudes-main 
## 3. Instale el entorno virtual:
- Abra una terminal e ingrese a la carpeta donde descomprimió el archivo zip 
> python -m pip install virtualenv
> - Si no funciona la instrucción con la palabra python, utilice la palabra py
> - py -m pip install virtualenv
- Cree un entorno virtual
> python -m venv venv_solicitud
> - Si no funciona la instrucción con la palabra python, utilice la palabra py
> - py -m venv venv_solicitud
- Activar El Entorno Virtual
> venv_solicitud\Scripts\activate
> - Para el ejemplo del video, ejecutar:
> - C:\crear_solicitudes-main\venv_solicitud\Scripts\activate
- Entorno Virtual Activo (Ejemplo del video)
> - debe aparacer entre paréntesis al lado izquierdo de la ruta el nombre del entorno.
> - (venv_solicitud) C:\crear_solicitudes-main>
## 4. Instale los componentes
Con el entorno virtual activo ejecute el siguiente comando
> pip install -r requirements.txt
# Configuración inicial
- Abra el archivo .env
- Ingrese el usuario y password de litigar inmediatamente al frente de caracter igual (=)
> - user_name=
> - password=
- procesar_desde_fila
> procesar_desde_fila --> Inicia la creación de solicitudes, desde el numero de la fila indicado en este campo
- numero_ejecucion
> - numero_ejecucion --> Cuando se ejecuta el programa se genera un numero para poder consultar el resumen del cargue
> - numero_ejecucion=0 --> Si el valor es 0, se crea un nuevo numero_ejecucion carga el archivo cargue_masivo.csv, procesa cada solicitud y asocia el respectivo pdf
> - numero_ejecucion=999 --> Si el valor es diferente de 0, procesa cada solicitud y asocia el respectivo pdf al numero de ejecución indicado
- El numero de ejecución permite ver resumen del cargue desde litiradicaciones desde la siguiente ruta
> masivos -> Cargar archivos masivos -> Consultar ultimos cargues
# Funcionalidad
## 1. Ingreso de registros para crear las solicitudes
- En el archivo plano cargue_masivo.csv se deben colocar los registros con los cuales se van a crear las solicitudes.
- Estructura del Archivo de Cargue: Delimitador punto y coma (;) La primera fila del archivo no se va a procesar, contiene los títulos de los campos.:
> PROCESO_ID; RADICACION; LOCALIDAD; DESPACHO; CLIENTE_ID; DEMANDANTE; DEMANDADO; TIPO_DOCUMENTO; TIPO_ENVIO; FECHA_TERMINO(yyyy-mm-dd o dd/mm/yyyy); HORA(HH:MM); LOCALIDAD_ORIGEN; OTRA_ENTIDAD_LUGAR_RADICACION; PAQUETES; CANTIDAD_FOLIOS; RETORNAR_ACUSE (S/N); DESTINATARIO_RETORNO; TELEFONO_RETORNO; DIRECCION_RETORNO; OBSERVACIONES; CODIGO_CLIENTE; CEDULA_CLIENTE
- En cada fila del archivo se debe ingresar un numero de solicitud.
- Los números de solicitud no se deben separar con caracteres adicionales como la coma, punto y coma o pipes.
## 2. pdfs/zip asociados a las solicitudes
- Los archivos pdfs deben ser ubicados en la carpeta pdfs.
- El archivo debe incluir al inicio del nombre el numero de la fila (seguido de un guión bajo) al cual se le debe asociar la solicitud de radicación a crear. 
> - Ej: FILA_nombreArchivo.pdf 
> - 2_nombreArchivo.pdf 
> - 2_nombreArchivo.zip
- Solo se puede asociar un archivo (zip/pdf) por cada solicitud creada
## 3. Logs:
- Los logs de la ejecución de la aplicación quedan ubicados en la carpeta logs.
# Ejecución de la aplicación
Estando en la terminal en la ruta principal del proyecto, ejecute los siguientes pasos:
## 1. Asegurese de tener el entorno virtual activo
- Activar El Entorno Virtual
> venv_solicitud\Scripts\activate
> - Para el ejemplo del video, ejecutar:
> - C:\crear_solicitudes-main\venv_solicitud\Scripts\activate
- Entorno Virtual Activo
> - Debe aparacer entre paréntesis al lado izquierdo de la ruta el nombre del entorno.
> - (venv_solicitud) C:\crear_solicitudes-main>
## 2. Prepare el archivo cargue_masivo.csv 
- coloque los registros de las solicitudes a crear en el archivo cargue_masivo.csv
## 3. Ubique los archivos pdf/zip en la carpeta pdfs
- Tenga en cuenta la estructura de los nombres de los archivos
## 4. Verifique los valores de las variables en .env
- procesar_desde_fila
- numero_ejecucion
## 5. Ejecute la aplicación
En la terminal, ejecute el siguiente comando
> python crear_ida_vuelta.py
- Si no funciona la instrucción con la palabra python, utilice la palabra py
> py crear_ida_vuelta.py
- Si al realizar una ejeción sale un error y no se crean las solicitudes, intente de nuevo la ejecución.
- Si el error persiste, informe al administrador (grupo de página)

