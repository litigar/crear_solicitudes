import csv
import os
import requests
import re
from dotenv import load_dotenv

# from base64 import b64decode
from datetime import date
from concurrent.futures import ProcessPoolExecutor
from liti_log import UtilLog
from admin_user import admin_user
from file_system import getCsvToBase64, getPdfToBase64, crear_directorio


# C:\DocJairo\desarrollo\consumirApiPy\ve_cons\Scripts\activate


class crear_solicitudes(object):
    """Obtiene los pdfs de una solicitud de radicaciones"""

    def __init__(self):
        # super(crear_solicitudes, self).__init__()
        crear_directorio("logs")
        self.path_logs = "logs/"
        crear_directorio("pdfs")
        self.path_pdfs = "pdfs/"
        # Para que funcionen los hilos NLS_LANG
        os.environ["NLS_LANG"] = "SPANISH_SPAIN.UTF8"
        load_dotenv()
        file_log = "crear-solicitud" + str(date.today()) + ".log"
        UtilLog.get_instance().set_file_name(self.path_logs + file_log)

        self.file_csv = "cargue_masivo.csv"
        # print(f"local_path {self.local_path}")
        # print(f"init username {self.username}")
        # print(f"init usr_dicc {self.usr_dicc}")
        self.masivo_file_id = os.environ.get("numero_ejecucion")

    __instance = None
    Lista = []

    def __str__(self):
        return "crear_solicitudes Singleton "

    def __new__(cls):
        if not crear_solicitudes.__instance:
            crear_solicitudes.__instance = object.__new__(cls)
        return crear_solicitudes.__instance

    @staticmethod
    def get_instance():
        if not crear_solicitudes.__instance:
            crear_solicitudes.__instance = crear_solicitudes()
        return crear_solicitudes.__instance

    def generar_resumen(self):
        # UtilLog.get_instance().write(f"generar_resumen INICIO ")
        endpoint = admin_user.get_instance().url + "resumen_ida_vuelta/"
        token = "Token " + admin_user.get_instance().get_token()
        # print(f"generar_resumen " + "b" * 10)
        # token='Token c3a16a55b7ebdc559c65a0e17c58197dc719061f'
        headers = {"Content-Type": "application/json;", "Authorization": token}
        # reponse=requests.get(endpoint, params={'pk':2})
        # print(f"generar_resumen radicacion_id {radicacion_id}")
        reponse = requests.post(
            endpoint,
            headers=headers,
            json={"masivo_file_id": self.masivo_file_id, "len_solicitudes": len(self.lista_solicitudes) - 1},
        )
        UtilLog.get_instance().write(
            f"generar_resumen reponse.status_code {str(reponse.status_code)} masivo_file_id {str(self.masivo_file_id)}"
        )
        # print(reponse)
        # print(reponse.url)
        json_item = reponse.json()
        # print(f"enviar_solicitud_y_pdf json_item {json_item}")

        if reponse.status_code == 201:
            # print(f"generar_resumen nombre_archivo {json_item['nombre_archivo']}")
            # UtilLog.get_instance().write(f"generar_resumen solicitud_id {str(json_item['radicado_id'])}")
            if json_item["estado"] == "ok":
                mensaje = f"generar_resumen masivo_file_id {str(self.masivo_file_id)} "
                mensaje += f" resumen {str(json_item['resumen'])} - ok"
                UtilLog.get_instance().write(mensaje)
                return True
            else:
                mensaje = f"generar_resumen masivo_file_id {str(self.masivo_file_id)} "
                mensaje += f" resumen {str(json_item['resumen'])} - error"
                UtilLog.get_instance().write(mensaje)
                return False
        else:
            UtilLog.get_instance().write(
                f"generar_resumen Else {str(reponse.status_code)} - masivo_file_id {str(self.masivo_file_id)}"
            )
            return False

    def enviar_solicitud_y_pdf(self, payload):
        # UtilLog.get_instance().write(f"enviar_solicitud_y_pdf payload ")
        endpoint = admin_user.get_instance().url + "crear_ida_vuelta/"
        token = "Token " + admin_user.get_instance().get_token()
        # print(f"enviar_solicitud_y_pdf " + "b" * 10)
        # token='Token c3a16a55b7ebdc559c65a0e17c58197dc719061f'
        headers = {"Content-Type": "application/json;", "Authorization": token}
        # reponse=requests.get(endpoint, params={'pk':2})
        # print(f"enviar_solicitud_y_pdf radicacion_id {radicacion_id}")
        reponse = requests.post(endpoint, headers=headers, json=payload)
        UtilLog.get_instance().write(
            f"enviar_solicitud_y_pdf status_code {reponse.status_code} numero_fila {str(payload['numero_registro'])}"
        )
        # print(reponse)
        # print(reponse.url)
        json_item = reponse.json()
        # print(f"enviar_solicitud_y_pdf json_item {json_item}")

        if reponse.status_code == 201:
            # print(f"enviar_solicitud_y_pdf nombre_archivo {json_item['nombre_archivo']}")
            # UtilLog.get_instance().write(f"enviar_solicitud_y_pdf solicitud_id {str(json_item['radicado_id'])}")
            mensaje = f"enviar_solicitud_y_pdf numero_fila {str(payload['numero_registro'])}"
            mensaje += f" solicitud_id {str(json_item['radicado_id'])}"
            if json_item["estado"] == "ok":
                UtilLog.get_instance().write(mensaje + " - ok")
                return True
            else:
                UtilLog.get_instance().write(mensaje + " - error")
                return False
        else:
            mensaje = f"enviar_solicitud_y_pdf Else {str(reponse.status_code)} "
            mensaje += f"- numero_fila {str(payload['numero_registro'])}"
            UtilLog.get_instance().write(mensaje)
            return False

    def get_json_solicitudes(self, registro, numero_fila, file_name, file_64):
        columnas = []
        columnas.append(registro.split(";"))
        # print(f"registro {registro}")
        # print(f"columnas[0] {columnas[0]}")
        # print(f"columnas[0][1] {columnas[0][1]}")

        proceso_id = ""  # 0
        radicacion = ""  # 20189999992018999999
        localidad = ""  # MEDELLIN
        despacho = ""  # CIVIL CIRCUITO No. 2
        cliente_id = ""
        demandante = ""  # | PRUEBA JAVIER ALFONSO 2 | PRUEBA5 PRUEBA6 PRUEBA7 PRUEBA8
        demandado = ""  # | MINISTERIO DE CULTURA Y OTROS | PRUEBA DDO JAVIER ALFONSO
        tipo_documento = ""  # MEMORIAL DE CESION
        tipo_envio = ""  # DIGITAL
        fecha_termino = ""  # 31/03/2022
        hora = "00:00"  # 12 =00
        localidad_origen = ""  # BOGOTA
        otra_entidad_lugar_radicacion = ""  # CENTRO DE CONCILIACION RESOLVER
        paquetes = ""  # 1
        cantidad_folios = ""  # 1
        retornar_acuse = ""  # N
        destinatario_retorno = ""  # N/A
        telefono_retorno = ""  # N/A
        direccion_retorno = ""  # N/A
        observaciones = ""  # POR RAVOR RADICAR EL MEMORIAL DE CESION
        codigo_cliente = ""  # cc123
        cedula_cliente = ""  # 55988756

        try:
            proceso_id = columnas[0][0]  # 0
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes proceso_id {e}")
        try:
            radicacion = columnas[0][1]  # 20189999992018999999
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes radicacion {e}")
        try:
            localidad = columnas[0][2]  # MEDELLIN
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes localidad {e}")
        try:
            despacho = columnas[0][3]  # CIVIL CIRCUITO No. 2
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes despacho {e}")
        try:
            cliente_id = columnas[0][4]
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes cliente_id {e}")
        try:
            demandante = columnas[0][5]  # | PRUEBA JAVIER ALFONSO 2 | PRUEBA5 PRUEBA6 PRUEBA7 PRUEBA8
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes demandante {e}")
        try:
            demandado = columnas[0][6]  # | MINISTERIO DE CULTURA Y OTROS | PRUEBA DDO JAVIER ALFONSO
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes demandado {e}")
        try:
            tipo_documento = columnas[0][7]  # MEMORIAL DE CESION
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes tipo_documento {e}")
        try:
            tipo_envio = columnas[0][8]  # DIGITAL
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes tipo_envio {e}")
        try:
            fecha_termino = columnas[0][9]  # 31/03/2022
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes fecha_termino {e}")
        try:
            hora = columnas[0][10]  # 12 =00
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes hora {e}")
        try:
            localidad_origen = columnas[0][11]  # BOGOTA
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes localidad_origen {e}")
        try:
            otra_entidad_lugar_radicacion = columnas[0][12]  # CENTRO DE CONCILIACION RESOLVER
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes otra_entidad_lugar_radicacion {e}")
        try:
            paquetes = columnas[0][13]  # 1
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes paquetes {e}")
        try:
            cantidad_folios = columnas[0][14]  # 1
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes cantidad_folios {e}")
        try:
            retornar_acuse = columnas[0][15]  # N
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes retornar_acuse {e}")
        try:
            destinatario_retorno = columnas[0][16]  # N/A
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes destinatario_retorno {e}")
        try:
            telefono_retorno = columnas[0][17]  # N/A
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes telefono_retorno {e}")
        try:
            direccion_retorno = columnas[0][18]  # N/A
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes direccion_retorno {e}")
        try:
            observaciones = columnas[0][19]  # POR RAVOR RADICAR EL MEMORIAL DE CESION
        except Exception as e:
            UtilLog.get_instance().write(f"get_json_solicitudes observaciones {e}")
        try:
            codigo_cliente = columnas[0][20]  # cc123
        except IndexError as e:
            UtilLog.get_instance().write(f"get_json_solicitudes codigo_cliente {e}")
        try:
            cedula_cliente = columnas[0][21]  # 55988756
        except IndexError as e:
            UtilLog.get_instance().write(f"get_json_solicitudes cedula_cliente {e}")

        datos = {
            "masivo_file_id": self.masivo_file_id,
            "numero_registro": numero_fila,
            "proceso_id": proceso_id,  # 0,
            "radicacion": radicacion,  # "20189999992018999999",
            "localidad": localidad,  # "MEDELLIN",
            "despacho": despacho,  # "CIVIL CIRCUITO No. 2",
            "cliente_id": cliente_id,
            "demandante": demandante,  # "| PRUEBA JAVIER ALFONSO 2 | PRUEBA5 PRUEBA6 PRUEBA7 PRUEBA8",
            "demandado": demandado,  # "| MINISTERIO DE CULTURA Y OTROS | PRUEBA DDO JAVIER ALFONSO",
            "tipo_documento": tipo_documento,  # "MEMORIAL DE CESION",
            "tipo_envio": tipo_envio,  # "DIGITAL",
            "fecha_termino": fecha_termino,  # "31/03/2022",
            "hora": hora,  # "12:00",
            "localidad_origen": localidad_origen,  # "BOGOTA",
            "otra_entidad_lugar_radicacion": otra_entidad_lugar_radicacion,  # "CENTRO DE CONCILIACION RESOLVER",
            "paquetes": paquetes,  # 1,
            "cantidad_folios": cantidad_folios,  # 1,
            "retornar_acuse": retornar_acuse,  # "N" ,
            "destinatario_retorno": destinatario_retorno,  # "N/A",
            "telefono_retorno": telefono_retorno,  # "N/A",
            "direccion_retorno": direccion_retorno,  # "N/A",
            "observaciones": observaciones,  # "POR RAVOR RADICAR EL MEMORIAL DE CESION" ,
            "codigo_cliente": codigo_cliente,  # "cc123" ,
            "cedula_cliente": cedula_cliente,  # "55988756",
            "creado_desde": "api",
            "username": admin_user.get_instance().username,  # "JVEGA",
            "archivo_name": file_name,  # "algun_nombre.pdf",
            "archivo_64": file_64,
        }

        # print(datos)
        return datos

    def get_file_row(self, numero_fila):
        """
        Obtiene el archivo pdf/zip del numero de la fila a procesar
        """
        # print(f"get_file_row numero_fila {numero_fila} inicio")
        for archivo in self.lista_archivos:
            if numero_fila == int(archivo.split("_")[0]):
                mensaje = f"Buscando archivo - row_num {str(numero_fila)} | "
                mensaje += f"num_file {str(archivo.split('_')[0])} | archivo {archivo} --> encontrado"
                UtilLog.get_instance().write(mensaje)
                return archivo
        # print(f"get_file_row numero_fila {numero_fila} no encontrado")
        return ""

    def fila_fue_creada(self, numero_fila):
        UtilLog.get_instance().write("fila_fue_creada - inicio")
        endpoint = admin_user.get_instance().url + "fila_fue_creada_ida_vuelta/"
        token = "Token " + admin_user.get_instance().get_token()
        # token='Token c3a16a55b7ebdc559c65a0e17c58197dc719061f'

        """
        print(f'* fila_fue_creada - masivo_file_id {self.masivo_file_id}')
        print(f'* fila_fue_creada - numero_fila {numero_fila}')
        print(f'* fila_fue_creada - token {token}')
        print(f'* fila_fue_creada - endpoint {endpoint}')
        """

        headers = {"Content-Type": "application/json;", "Authorization": token}
        reponse = requests.get(
            endpoint, headers=headers, params={"masivo_file_id": self.masivo_file_id, "numero_fila": numero_fila}
        )
        UtilLog.get_instance().write(
            f"fila_fue_creada reponse.status_code {reponse.status_code} numero_fila {str(numero_fila)}"
        )
        # print(reponse)
        # print(reponse.url)
        json_item = reponse.json()
        print(f"fila_fue_creada json_item {json_item}")

        if reponse.status_code == 200:
            # print(f"fila_fue_creada nombre_archivo {json_item['nombre_archivo']}")
            # UtilLog.get_instance().write(f"enviar_solicitud_y_pdf solicitud_id {str(json_item['radicado_id'])}")
            if json_item["estado"] == "ok":
                mensaje = f"fila_fue_creada numero_fila {str(numero_fila)}"
                mensaje += f" solicitud_id {str(json_item['radicado_id'])} - fila ya habia sido creada"
                UtilLog.get_instance().write(mensaje)
                return True
            else:
                UtilLog.get_instance().write(
                    f"fila_fue_creada numero_fila {str(numero_fila)} - fila no ha sido creada, se procede a crear"
                )
                return False
        else:
            mensaje = f"fila_fue_creada numero_fila {str(numero_fila)}"
            mensaje += f" - error {str(reponse.status_code)} - se intentara crear fila"
            UtilLog.get_instance().write(mensaje)
            return False

    def add_solicitud(self, dato):
        registro = dato["registro"]
        numero_fila = dato["fila"]
        if not self.fila_fue_creada(numero_fila):
            file_pdf_zip = self.get_file_row(numero_fila)
            if len(file_pdf_zip) > 0:
                file_64 = getPdfToBase64(self.path_pdfs + file_pdf_zip)
                datos = self.get_json_solicitudes(registro, numero_fila, file_pdf_zip, file_64)

                # print(f"add_solicitud {datos}")
                # print(f"add_solicitud intento 1 fila ({numero_fila})")
                # Realiza dos intentos de descarga
                if not self.enviar_solicitud_y_pdf(datos):
                    # print(f"add_solicitud intento 2 fila ({numero_fila})")
                    if not self.enviar_solicitud_y_pdf(datos):
                        UtilLog.get_instance().write(f"No se proceso el registro {numero_fila}")
                        return False
                return True
            else:
                UtilLog.get_instance().write(f"No se encontró registro para el registro {numero_fila}")
                return False
        return False

    def procesar_solicitudes(self):
        i = 0
        for dato in self.lista_solicitudes:
            i = dato["fila"]
            if i > 1:  # La primera fila son los títulos
                UtilLog.get_instance().write(f"procesar_solicitudes --> add_solicitud fila ({i})")
                self.add_solicitud(dato)

    def getListaSolicitudes(self):
        # print(f"getListaSolicitudes")
        lista = []
        i = 0
        with open(self.file_csv, encoding="utf-8") as fname:
            for registro in fname:
                i += 1
                # print(registro)
                dato = {"registro": registro, "fila": i}
                lista.append(dato)
        return lista

    def getListaArchivos(self):
        lista = []
        for file in os.listdir(self.path_pdfs):
            if ".pdf" in file.lower() or ".zip" in file.lower():
                # print(file)
                lista.append(str(file))
        return lista

    def procesar_solicitudes_hilos(self):
        # print("procesar_solicitudes __name__ ({__name__})")
        if __name__ == "__main__":
            cores = int(os.cpu_count() / 2 + 1)
            # UtilLog.get_instance().write("Nucleos a utilizar " + str(cores) + "/" + str(os.cpu_count()))
            UtilLog.get_instance().write(f"lista_solicitudes cantidad {str(len(self.lista_solicitudes))}")
            with ProcessPoolExecutor(max_workers=cores) as executor:
                [executor.map(self.add_solicitud, self.lista_solicitudes)]

    def subir_csv(self):
        if int(self.masivo_file_id) > 0:
            UtilLog.get_instance().write(f"subir_csv - numero_ejecucion: {str(self.masivo_file_id)}")
            return True

        UtilLog.get_instance().write("subir_csv - procesando archivo csv")

        secuencia = admin_user.get_instance().get_secuencia("SQ_FILE_API_ID")
        if secuencia == 0:
            UtilLog.get_instance().write("subir_csv - error secuencia - Fin programa")
            return False

        UtilLog.get_instance().write(f"subir_csv - secuencia_file_api {secuencia}")
        UtilLog.get_instance().write(f"subir_csv - file_csv - {self.file_csv}")
        csv_base_64 = getCsvToBase64(self.file_csv)
        # UtilLog.get_instance().write("subir_csv - base 64")

        payload = {
            "username": admin_user.get_instance().username,
            "archivo_name": "cargue_masivo_" + str(secuencia) + ".csv",
            "archivo_csv_64": csv_base_64
            # "archivo_csv_64": "YXJjaGl2b19jc3ZfNjQ="
        }

        endpoint = admin_user.get_instance().url + "cargar_ida_vuelta/"
        token = "Token " + admin_user.get_instance().get_token()
        # UtilLog.get_instance().write(f"subir_csv - token {token}")
        # print(f"subir_csv " + "b" * 10)
        # token='Token c3a16a55b7ebdc559c65a0e17c58197dc719061f'
        headers = {"Content-Type": "application/json;", "Authorization": token}
        # reponse=requests.get(endpoint, params={'pk':2})
        # print(f"subir_csv radicacion_id {radicacion_id}")
        reponse = requests.post(endpoint, headers=headers, json=payload)
        print(f"subir_csv reponse.status_code {reponse.status_code}")
        # print(reponse)
        # print(reponse.url)
        json_item = reponse.json()
        UtilLog.get_instance().write(f"subir_csv list_json {json_item}")

        if reponse.status_code == 200:
            # print(f"generar_pdfs nombre_archivo {json_item['nombre_archivo']}")
            UtilLog.get_instance().write(
                f"subir_csv masivo_file {json_item['masivo_file_id']} archivo {json_item['archivo_name']}"
            )
            # UtilLog.get_instance().write(f"subir_csv solicitud_id {radicacion_id} {json_item}")
            if json_item["estado"] == "ok":
                self.masivo_file_id = json_item["masivo_file_id"]
                UtilLog.get_instance().write("-------------------------------------------------------------")
                UtilLog.get_instance().write(
                    f"******** numero ejecucion ({json_item['masivo_file_id']}) *********"
                )
                UtilLog.get_instance().write("-------------------------------------------------------------")
                return True
            else:
                UtilLog.get_instance().write(f"subir_csv solicitud_id json_item {json_item}")
                return False
        else:
            UtilLog.get_instance().write(f"subir_csv list_json json_item {json_item}")
            return False

    def validar_long_registros_archivos(self):
        self.lista_solicitudes = self.getListaSolicitudes()
        self.lista_archivos = self.getListaArchivos()
        l_solicitudes = len(self.lista_solicitudes) - 1
        l_archivos = len(self.lista_archivos)

        if l_solicitudes > l_archivos:
            UtilLog.get_instance().write(f"registros csv: {str(l_solicitudes)}")
            UtilLog.get_instance().write(f"cantidad archivos: {str(l_archivos)}")
            UtilLog.get_instance().write("cantidad registros es diferente a la cantidad archivos")
            return False
        return True

    def run(self):
        if self.validar_long_registros_archivos():
            # print("Inicio")
            admin_user.get_instance().autentication()
            admin_user.get_instance().get_token()
            # self.procesar_solicitudes()
            # self.fila_fue_creada(2)

            # Procesa los archivos uno a uno
            if self.subir_csv():
                self.procesar_solicitudes()
                self.generar_resumen()

            """
            if self.subir_csv():
                self.procesar_solicitudes_hilos()
            """

            UtilLog.get_instance().write("-------------------------------------------------------------")
            UtilLog.get_instance().write("NO OLVIDE DEJAR EN CERO 0 EL PARAMETRO --> numero_ejecucion=0")
            UtilLog.get_instance().write("-------------------------------------------------------------")
            UtilLog.get_instance().write("Para ver resumen desde litiradicaciones")
            UtilLog.get_instance().write("masivos->Cargar archivos masivos->Consultar ultimos cargues")
            UtilLog.get_instance().write(f"*** numero ejecucion: ({self.masivo_file_id}) ***")


crear_solicitudes().run()
