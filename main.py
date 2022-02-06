import telebot
from fastapi import FastAPI, Request
import requests

bot = telebot.TeleBot('1551417672:AAHpCgSQ-ipMD5RSqPjSPTjqUT5EBBZWA-8')
app = FastAPI()
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)

keyboard1.row('Обо мне', 'Успехи', 'Опыт работы', 'Образование', 'Навыки', 'Сертификаты', 'FastAPI Quote')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте.Это бот-резюме расскажет обо мне, покажет мои сертификаты, и продемонстрирует крошечку мудрости.', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Обо мне':
        bot.send_message(message.chat.id, '''Наталья Козулина
36 лет, замужем, 2 детей.
Проживаю в Алматы.
Обожаю горы и велопрогулки.

Мечтаю работать в самой сильной и прогрессивной команде Data Science в Казахстане. Люди из Kolesa Group очень вдохновляют меня. Обожаю подкаст "Код и Кофе". Благодаря курсу от Рауана и American Space Almaty изучила FastAPI. Вот цитата, которую я извлекаю при помощи FastAPI:''')
        url = 'https://api.quotable.io/random'
        result = requests.get(url).json()['content']
        bot.send_message(message.chat.id, result)

    elif message.text == 'Сертификаты':
        certif1 = open('4.jpg', 'rb')
        certif2 = open('5.jpg', 'rb')
        certif3 = open('6.jpg', 'rb')
        certif4 = open('7.jpg', 'rb')
        certif5 = open('1.jpg', 'rb')
        bot.send_photo(message.chat.id, certif1)
        bot.send_photo(message.chat.id, certif2)
        bot.send_photo(message.chat.id, certif3)
        bot.send_photo(message.chat.id, certif4)
        bot.send_photo(message.chat.id, certif5)

    elif message.text == 'Успехи':
        bot.send_message(message.chat.id, 'Пройдя трехдневный марафон по программированию, в котором участвовало около 200 человек, решила 21 урок, заняла первое место и выиграла курс по Data Science от ABLE Academy. Также самостоятельно изучаю программирование, статистику, теорию вероятности и многое другое на таких ресурсах как Stepik, Udemy, Coursera, freeCodeCamp, Sololearn etc.')

    elif message.text == 'Опыт работы':
        bot.send_message(message.chat.id, '''
Курс по анализу данных
от Able Academy
2021-2022
В данный момент я прохожу третий модуль курса,
посвященный машинному обучению. Мною
пройдены первые два модуля курса, в которых
рассматривались вопросы языка программирования
Python, ООП, работа с данными при помощи
библиотек Numpy, Pandas, Matplotlib
''')
        bot.send_message(message.chat.id, '''
ТОО НПП «ФИИТ»
2009-2019
Инженер-конструктор. Расчёт и разработка систем
сжигания топлива, промышленных горелочных
устройств и систем подготовки топлива.
''')
        bot.send_message(message.chat.id, '''
ТОО ТехнологииKZ
2008-2009
Инженер-проектировщик систем отопления.
Расчет теплопотерь зданий по СНиП, разработка
проектной и рабочей документации, чертежей,
планов, подбор специального оборудования систем
теплоснабжения и отопления. Использовала в
работе программы: AutoCAD и Microsoft Excel
''')

    elif message.text == 'Образование':
        bot.send_message(message.chat.id, '''
Алматинский институт
энергетики и связи
2003-2008
Инженер-теплоэнергетик
''')
        bot.send_message(message.chat.id, '''
Python for Data Science and Machine Learning Bootcamp
2021-2022

Курс посвящен основам работы с данными и моделями машинного обучения.
''')
        bot.send_message(message.chat.id, '''
Python for Everyone
2021
Курс от American Space Almaty и Rawan Qurmet 
''')
    elif message.text == 'Навыки':
        bot.send_message(message.chat.id, '''
— Python
— Numpy
— Pandas
— Matplotlib
— SQL
— Google Sheets
— Jupyter-notebook
— Github
— Статистика
— Теория вероятности
— Коммуникабельность
— Целеустремленность
''')

    elif message.text == 'FastAPI Quote':
        url = 'https://api.quotable.io/random'
        result = requests.get(url).json()['content']
        bot.send_message(message.chat.id, result)

    else:
        bot.send_message(message.chat.id, 'Ой! Не знаю как ответить. Сейчас погуглю!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMOYCkAAcOU8T-4VXdQ37mE7cTSX6nLAAKGAQACFkJrCi576oRhXPHGHgQ')

bot.polling()