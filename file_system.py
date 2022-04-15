import base64
import os

from liti_log import UtilLog


def crear_directorio(directorio):
    try:
        if not os.path.exists(directorio):
            os.mkdir(directorio)
    except Exception as e:
        print(f"crear_directorio {e}")


def getCsvToBase64(archivo):
    try:
        # print("getCsvToBase64 a")
        if os.path.exists(archivo):
            # print("getCsvToBase64 b")
            with open(archivo, "rb") as file_csv:
                byte_content = file_csv.read()
                # print("getCsvToBase64 c")
            # arcB64 = base64.b64encode(byte_content.encode('utf-8'))
            base64_bytes = base64.b64encode(byte_content)
            base64_string = base64_bytes.decode("utf-8")
            # print("getCsvToBase64 d")
            # print(base64_string)
            return base64_string
        # print("getCsvToBase64 e")
    except Exception as e:
        UtilLog.get_instance().write(f"getCsvToBase64 f {e}")


def getPdfToBase64(archivo):
    # print(f"getPdfToBase64 archivo {archivo}")
    try:
        if os.path.exists(archivo):
            with open(archivo, "rb") as pdf_file:
                arcB64 = base64.b64encode(pdf_file.read())
            base64_string = arcB64.decode("utf-8")
            # print(arcB64)
            return base64_string
    except Exception as e:
        UtilLog.get_instance().write(f"getCsvToBase64 f {e}")


def getBase64ToPdf(nombre_archivo, b64):
    bytes = base64.b64decode(b64, validate=True)

    if bytes[0:4] != b"%PDF":
        raise ValueError("Missing the PDF file signature")

    # Write the PDF contents to a local file
    f = open(nombre_archivo, "wb")
    f.write(bytes)
    f.close()
