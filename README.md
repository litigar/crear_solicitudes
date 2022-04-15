# Creación masiva de solicitudes de Radicaciones
> Aplicacion cliente que consume un servicio de la api de litigar, para crear masivamente solicitudes de radicaciones con y sin procesos en vigilancia.
## 1 Video explicativo de la instalación
[![Alt text](https://img.youtube.com/vi/TWMNQ5hEILA/0.jpg)](https://www.youtube.com/watch?v=TWMNQ5hEILA)
## 2 Video de configuración y ejecución para la creación masiva de solicitudes
[![Alt text](https://img.youtube.com/vi/im43fsOfZSg/0.jpg)](https://www.youtube.com/watch?v=im43fsOfZSg)
# Versionamiento
- Fecha primera versión: 14/04/2022
* Python >3.6.2 +
# Instalación
## 1. Instale python desde la siguiente ruta:
> https://www.python.org/downloads/
## 2. Descargue y Descomprima el proyecto
- Descargue en la carpeta el proyecto desde github, ya sea desde un archivo zip (descomprímirlo) o por github
> https://github.com/litigar/crear_solicitudes.git
- Descomprima el archivo zip 
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
## 2. prepare el archivo cargue_masivo.csv 
- coloque los registros de las solicitudes a crear en el archivo cargue_masivo.csv
## 3. ubique los archivos pdf/zip en la carpeta pdfs
- Tenga en cuenta la estructura de los nombres de los archivos
## 4. Ejecute la aplicaciòn
> python crear_solicitudes.py
- Si no funciona la instrucción con la palabra python, utilice la palabra py
> py crear_solicitudes.py
- Si al realizar una ejeción sale un error y no se crean las solicitudes, intente de nuevo la ejecución.
- Si el error persiste, informe al administrador (grupo de página)

