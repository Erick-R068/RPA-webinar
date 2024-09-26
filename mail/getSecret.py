from google.cloud import secretmanager

def get_secret(secret_id, project_id, version="latest"):
    """
    Recupera un secreto del Google Secret Manager.
    
    Parámetros:
        secret_id (str): ID del secreto en Google Secret Manager.
        project_id (str): ID del proyecto de Google Cloud.
        
    Retorna:
        str: El valor del secreto recuperado.
    """
    try:
        # Crear cliente de Secret Manager
        client = secretmanager.SecretManagerServiceClient()
        
        # Construir el nombre del recurso de la versión del secreto
        name = f"projects/{project_id}/secrets/{secret_id}/versions/{version}"

        # Recuperar el secreto
        response = client.access_secret_version(request={"name": name})
        secret = response.payload.data.decode('UTF-8')
        return secret
    
    except Exception as e:
        print(f"Error al obtener el secreto: {e}")
        return None

