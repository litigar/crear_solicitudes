# Descargar pdfs de solicitudes de Radicaciones
> Aplicacion cliente que consume servicio de la api de litigar, para descargar los pdfs asociados a las solicitudes de radicaciones.
## 1 Video explicativo de la instalación
[![Alt text](https://img.youtube.com/vi/TWMNQ5hEILA/0.jpg)](https://www.youtube.com/watch?v=TWMNQ5hEILA)
## 2 Video de configuración y ejecución para la descarga de los pdfs
[![Alt text](https://img.youtube.com/vi/im43fsOfZSg/0.jpg)](https://www.youtube.com/watch?v=im43fsOfZSg)
# Versionamiento
- Fecha primera versión: 24/03/2022
* Python >3.6.2 +
# Instalación
## 1. Instale python desde la siguiente ruta:
> https://www.python.org/downloads/
## 2. Descargue y Descomprima el proyecto
- Descargue en la carpeta el proyecto desde github, ya sea desde un archivo zip (descomprímirlo) o por github
> https://github.com/litigar/descargar_solicitudes.git
- Descomprima el archivo zip 
## 3. Instale el entorno virtual:
- Abra una terminal e ingrese a la carpeta donde descomprimió el archivo zip 
> python -m pip install virtualenv
> - Si no funciona la instrucción con la palabra python, utilice la palabra py
> - py -m pip install virtualenv
- Cree un entorno virtual
> python -m venv venv_descarga
> - Si no funciona la instrucción con la palabra python, utilice la palabra py
> - py -m venv venv_descarga
- Activar El Entorno Virtual
> venv_descarga\Scripts\activate
> - Para el ejemplo del video, ejecutar:
> - C:\descargar_solicitudes-main\venv_descarga\Scripts\activate
- Entorno Virtual Activo (Ejemplo del video)
> - debe aparacer entre paréntesis al lado izquierdo de la ruta el nombre del entorno.
> - (venv_descarga) C:\descargar_solicitudes-main>
## 4. Instale los componentes
Con el entorno virtual activo ejecute el siguiente comando
> pip install -r requirements.txt
# Configuración inicial
- Abra el archivo .env
- Ingrese el usuario y password de litigar inmediatamente al frente de caracter igual (=)
> - user_name=
> - password=
# Funcionalidad
## 1. Selección de solicitudes para descargar pdfs
- En el archivo solicitudes.txt se deben ingresar los numero de solicitudes.
- En cada fila del archivo se debe ingresar un numero de solicitud.
- Los números de solicitud no se deben separar con caracteres adicionales como la coma, punto y coma o pipes.
## 2. Descargue de pdfs de las solicitudes
- Los archivos pdfs quedan ubicados en la carpeta pdfs.
- El nombre del archivo descargado tiene la siguiente estructura:
> Solicitud_id_Historia_id_estadoSolicitud.pdf
## 3. Logs:
- Los logs de la ejecución de la aplicación quedan ubicados en la carpeta logs.
# Ejecución de la aplicación
Estando en la terminal en la ruta principal del proyecto, ejecute los siguientes pasos:
## 1. Asegurese de tener el entorno virtual activo
- Activar El Entorno Virtual
> venv_descarga\Scripts\activate
> - Para el ejemplo del video, ejecutar:
> - C:\descargar_solicitudes-main\venv_descarga\Scripts\activate
- Entorno Virtual Activo
> - Debe aparacer entre paréntesis al lado izquierdo de la ruta el nombre del entorno.
> - (venv_descarga) C:\descargar_solicitudes-main>
## 2. realizar la descarga de pdfs de las solicitudes
> python descargar_solicitudes.py
- Si no funciona la instrucción con la palabra python, utilice la palabra py
> py descargar_solicitudes.py

