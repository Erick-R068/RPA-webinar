from flask import Flask, jsonify
from google.oauth2 import service_account

from webscraping.checkStock import check_stock  # Importa la función desde script.py
from mail.sendMail import send_mail
from logs.logToFirestore import log_to_firestore


# Descomendar para testing local
#####################
#import os
#script_directory = "ruta/a/carpeta"        # Modificar segun ubicacion de directorio del RPA
#os.chdir(script_directory)
#####################


url = 'https://articulo.mercadolibre.cl/MLC-992215914-blade-hp-bl460c-octava-generacion-_JM#polycard_client=search-nordic&position=28&search_layout=stack&type=item&tracking_id=2a2f503b-2ef4-4d2c-9c47-1cce65f2b191'

credentials_json_path = "<credenciales>.json"        # Modificar segun nombre de archivo de claves generado

# Autenticación con Google Cloud usando el archivo de credenciales
credentials = service_account.Credentials.from_service_account_file(credentials_json_path)

app = Flask(__name__)

# Ruta para verificar el stock de Mercadolibre
@app.route('/check_stock', methods=['GET'])
def check_stock_route():
    
    stock_status = check_stock(url)
    log_to_firestore("ProLiant DL360 Gen10", stock_status)
    send_mail(stock_status)
    
    return jsonify({"stock_status": stock_status})

# Iniciar el servidor de Flask solo si el archivo es ejecutado directamente
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


