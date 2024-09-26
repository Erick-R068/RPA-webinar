import datetime
import pytz
from flask import request
from google.oauth2 import service_account
from firebase_admin import firestore

credentials_json_path = "<credenciales>.json"        # Modificar segun nombre del archivo json generado


# Inicializar el cliente de Firestore (base de datos)
def init_db():
    global db
    try:
        credentials = service_account.Credentials.from_service_account_file(credentials_json_path)
        db = firestore.Client(credentials=credentials)
        print("Base de datos Firestore inicializada exitosamente.")
    except:
        print("Error al inicializar la base de datos Firestore.")



def log_to_firestore(product, stock_status):
    # Inicializar la base de datos Firestore
    try:
        init_db()
    except Exception as e:
        print(f"Error al inicializar la base de datos Firestore: {e}")
        return False

    # Agregar el registro a Firestore
    try:
        now = datetime.datetime.utcnow()
        gmt_4 = pytz.timezone('Etc/GMT+4')
        now_gmt_4 = now.astimezone(gmt_4)
        timestamp_str = now_gmt_4.strftime('%Y-%m-%dT%H:%M:%S')  # Sin decimas de segundo
        doc_name = f"{timestamp_str}__Stock"

        doc_ref = db.collection('logs').document(doc_name)
        doc_ref.set({
            'timestamp': timestamp_str,
            'product': product,
            'stock': stock_status,
        })
        print("Registro agregado a Firestore exitosamente.")
    except Exception as e:
        print(f"Error al agregar el registro a Firestore: {e}")



