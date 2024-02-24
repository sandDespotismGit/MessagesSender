import os
import pandas as pd

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
    
    excel_data = pd.read_excel('data.xlsx')
    e = excel_data['Почта'].tolist()
    with open("index.html") as file:
        template = file.read()
        message = MIMEText(template, "html")
    subject = input("Введите тему сообщения: \n>>> ")
    for recipient in e:
        send_email(message, subject, recipient)
    print("Успех!")

if __name__ == "__main__":
    main()