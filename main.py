from imap_tools import MailBox #, Q
from imap_tools import A, AND, OR, NOT
import datetime
import os

from unrar import rarfile


# # get all attachments for each email from INBOX folder
# with MailBox('imap.yandex.ru').login('gilr@soft-servis.ru', 'E0JFc985', 'INBOX') as mailbox:
#     for msg in mailbox.fetch((AND(all=True))): # Берет все письма из папки Входящие (INBOX)
#             for att in msg.attachments:
#                 #print(att.filename, att.content_type)
#                 dateSend = str(msg.date)
#                 dateSend = dateSend[8:10] + '.' + dateSend[5:7] + '.' + dateSend[:4] # Составление даты письма
#                 path_email = 'C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + msg.from_ # Путь с логином почты
#                 path_full = 'C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + msg.from_  + '/' + dateSend  # Путь с логином почты и датой
#                 if os.path.isdir(path_email) == False: # Проверяем существует ли путь к папке с названием почты
#                     os.mkdir(path_email)
#                 if os.path.isdir(path_full) == False: # Проверяем существует ли путь к папке с названием в виде Даты письма
#                     os.mkdir(path_full)
#                 with open(path_full + '/{}'.format(att.filename), 'wb') as f:
#                     f.write(att.payload)

#Каталог из которого будем брать файлы
directory = 'C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/'

#Получаем список файлов в переменную files
files = os.listdir(directory) # Список с папками, названия из "Электронных адресов"

for email in files: #
    email_files = os.listdir('C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + email) # список папок в папке с названием  Электронной почты
    for name_date in email_files:
        email_files_date = os.listdir('C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + email + '/' + name_date) # список файлов в папке с Датой
        for name_file in email_files_date:
            root_ext = os.path.splitext('C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + email + '/' + name_date + '/' + name_file) # Вывод тип файла
            if root_ext[1] == '.rar':
                #print('Название файла: ' + name_file, '| Тип файла: ' + root_ext[1], '| Отправил: ' + email, '| Дата: ' + name_date)
                #rar = rarfile.RarFile('C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + email + '/' + name_date + '/' + name_file)
                rf = rarfile.RarFile('C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/gilr@soft-servis.ru/Learning-master.rar')
                for f in rf.infolist():
                    print(f.filename)
                #print(rar.namelist())
            #print('C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + email + '/' + name_date + '/' + name_file)
        #root_ext = os.path.splitext('C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + email + '/' + name_date + '/' + email_files_date)

        #print(email_files_date, 'Отправил: ' + email, 'Дата: ' + name_date)
    # email_files_letters = os.listdir('C:/Users/gilr.SOFT-SERVIS.000/Desktop/Python/MailPython/' + email + '/' + email_files)
    # print(email_files_letters)

