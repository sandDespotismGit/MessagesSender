import os
import smtplib
from email.mime.text import MIMEText
import email

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
    list_email = []
    file_emails = open('email.txt','r+')
    for line in file_emails:
        currentPlace = line[:-1]
        list_email.append(currentPlace)

    with open("message.txt", encoding='UTF-8') as file:
        text_message = file.read()
    message = text_message
    subject = input("Введите тему сообщения: \n>>> ")
    recipients = list_email
    for recipient in recipients:    
        send_email(message, subject, recipients)
    print("Успех!")
    
    
if __name__ == "__main__":
    main()