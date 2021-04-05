from imap_tools import MailBox #, Q
from imap_tools import A, AND, OR, NOT
import datetime
import os


# Получение всех вложений с электронной почты с папки Входящие
with MailBox('imap').login('MAIL@MAIL.COM', 'PASSWORD', 'INBOX') as mailbox:
    for msg in mailbox.fetch((AND(all=True))): # Берет все письма из папки Входящие (INBOX)
            for att in msg.attachments:
                dateSend = str(msg.date)
                dateSend = dateSend[8:10] + '.' + dateSend[5:7] + '.' + dateSend[:4] # Составление даты письма
                path_email = 'C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + msg.from_ # Путь с логином почты
                path_full = 'C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + msg.from_  + '/' + dateSend  # Путь с логином почты и датой
                if os.path.isdir(path_email) == False: # Проверяем существует ли путь к папке с названием почты
                    os.mkdir(path_email)
                if os.path.isdir(path_full) == False: # Проверяем существует ли путь к папке с названием в виде Даты письма
                    os.mkdir(path_full)
                with open(path_full + '/{}'.format(att.filename), 'wb') as f:
                    f.write(att.payload)