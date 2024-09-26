import smtplib
from email.mime.text import MIMEText


def mail_script(sender_email, app_password, recipient_email, subject, body):
    """
    Envía un correo electrónico utilizando Gmail SMTP.

    Parámetros:
    sender_email (str): Dirección de correo del remitente.
    app_password (str): App Password generado para la autenticación en Gmail.
    recipient_email (str): Dirección de correo del destinatario.
    subject (str): Asunto del correo.
    body (str): Cuerpo del correo.
    """
    # Crear el mensaje
    msg = MIMEText(body)
    
    # Asunto del correo
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Configuración del servidor SMTP de Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Puerto para TLS

    try:
        # Conectar al servidor SMTP de Gmail
        s = smtplib.SMTP(smtp_server, smtp_port)
        s.starttls()  # Iniciar la conexión TLS
        s.login(sender_email, app_password)  # Autenticarse en Gmail
        s.sendmail(sender_email, [recipient_email], msg.as_string())  # Enviar el correo
        print("###################")
        print(f"Correo enviado exitosamente a {recipient_email}")
        print("###################")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        s.quit()


# Ejemplo de uso
if __name__ == "__main__":
    sender_email = "tucorreo@gmail.com"  # Dirección de correo del remitente
    app_password = "tu_app_password"  # App Password generado en Gmail
    recipient_email = "destinatario@example.com"  # Dirección de correo del destinatario
    subject = "Titulo del correo"
    body = "Este es el cuerpo del correo que se enviará."  # Contenido del mensaje

    # Llamar a la función para enviar el correo
    mail_script(sender_email, app_password, recipient_email, subject, body)
