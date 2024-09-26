from mail.mailScript import mail_script
from mail.getSecret import get_secret



def send_mail(stock_status):

    project_ID = "38302283146"
    version = "latest"

    sender_mail = get_secret("origin_mail", project_ID, version)
    sender_password = get_secret("origin_appPass", project_ID, version)
    recipient_mail = get_secret("target_mail", project_ID, version)
    subject = "RPA - Stock consultado."
    body = stock_status

    mail_script(sender_mail, sender_password, recipient_mail, subject, body)