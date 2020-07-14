# S M T P

import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

msg = MIMEMultipart()  # Объект почтового сообщения

# Почтовый аккаунт отправтеля
login = 'for.maks.ever@gmail.com'
with open('password.txt', 'r', encoding='utf-8') as f:
    data = f.read()
password = data

# Параметры почтового сообщения
msg['From'] = login
msg['To'] = input('Введите адрес получателя: ')
msg['Subject'] = input('Введите тему сообщения: ')
choice = int(input('Выберите формат сообщения (PlainText-1, HTML-2): '))
if choice == 1:
    message = input('Введите текст сообщения: ')
    msg.attach(MIMEText(message, 'plain'))
else:
    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body{
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h2>Message</h2>
        <hr>
        <main>
            <ol>
                <li><a href="https://www.ukr.net">Ukrainian info portal</a></li>
                <li><a href="https://www.bing">Searchable service of Microsoft</a></li>
                <li><a href="https://www.yahoo.com">American searchable service</a></li>
            </ol>
        </main>
    </body>
    </head>
    """
    msg.attach(MIMEText(html, 'html'))

# Вставка сообщения и прикрепленных файлов
with open('smile1.jpg', 'rb') as image:
    attachment = MIMEImage(image.read())
attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename('smile1.jpg'))
msg.attach(attachment)

# Процедура отправки сообщения
try:
    sender = smtplib.SMTP('smtp.gmail.com:587')  # Запуск сервера
    sender.starttls()
    sender.login(login, password)
    sender.sendmail(msg['From'], msg['To'], msg.as_string())
    sender.quit()
    print('Ваше сообщение успешно отправлено')
except Exception as err:
    print(err)
