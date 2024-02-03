import os
import smtplib
from email.mime.text import MIMEText

def send_email(message, subject, recipients):
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD_EMAIL')
    server = smtplib.SMTP("smtp.yandex.ru", 587)
    server.starttls()

    try:
        server.login(login, password)
        msg = MIMEText(message)
        msg["From"] = f"{login}"
        msg["Subject"] = subject
        # отправитель, получатели, сообщение
        server.sendmail(login, recipients, msg.as_string())
    except Exception as _ex:
        return f"{_ex}\n Неверный логин или пароль."
 
def main():
    with open("email.txt", "r") as emails:
        e = emails.read().split(" ")
    with open("message.txt", encoding='UTF-8') as file:
        message = file.read()
    subject = input("Введите тему сообщения: \n>>> ")
    for recipient in e:
        send_email(message, subject, recipient)
    print("Успех!")
    
if __name__ == "__main__":
    main()