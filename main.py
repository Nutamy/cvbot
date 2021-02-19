import telebot
from fastapi import FastAPI, Request
import requests


app = FastAPI()

bot = telebot.TeleBot('1602979123:AAG_TrU_eeQAdDDzDw8cymyYEtPFDeTtd_0')
# создаём клавиатуру бота
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)

# вводим название кнопок клавиатуры
keyboard1.row('Обо мне', 'Сертификаты', 'Мудрость')

# отвечаем на команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте.', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Обо мне':
        bot.send_message(message.chat.id, '''Наталья Козулина
35 лет
Замужем
2 детей (8 лет, 9 мес).
Алматы

Желаемая должность:
Data Engineer

Навыки:
HTML
CSS
JS
Python
FastAPI

Образование:
Высшее техническое
АУЭС 2003 - 2008 гг
Специальность: Инженер
Опыт работы:
- инженер ОВ (1год)
- инженер-конструктор (5 лет)

Связаться со мной:
@Biscuitty''')

    elif message.text == 'Сертификаты':
        certif1 = open('1.jpg', 'rb')
        certif2 = open('2.jpg', 'rb')
        certif1 = open('3.jpg', 'rb')
        certif2 = open('4.jpg', 'rb')
        bot.send_photo(message.chat.id, certif1)
        bot.send_photo(message.chat.id, certif2)
        bot.send_photo(message.chat.id, certif3)
        bot.send_photo(message.chat.id, certif4)


    elif message.text == 'Мудрость':
        url = 'https://api.quotable.io/random'
        result = requests.get(url).json()['content']
        bot.send_message(message.chat.id, result)

    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMOYCkAAcOU8T-4VXdQ37mE7cTSX6nLAAKGAQACFkJrCi576oRhXPHGHgQ')

bot.polling()





































""" from fastapi import FastAPI, Request
import requests
import telebot

app = FastAPI()

bot = telebot.TeleBot('1635283096:AAG_3Z0iWWMpWAjX-7OhinbU9dOff4S2Trs')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Обо мне', 'Сертификаты', 'Мудрость')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Здравствуйте. Это бот-резюме раскажет обо мне, покажет мои сертификаты, и продемонстрирует крошечку мудрости.', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Обо мне':
        bot.send_message(message.chat.id, '''Наталья Козулина
35 лет
Замужем
2 детей (8 лет, 9 мес).
Алматы

Желаемая должность:
Data Engineer

Навыки:
HTML
CSS
JS
Python
FastAPI

Образование:
Высшее техническое
АУЭС 2003 - 2008 гг
Специальность: Инженер
Опыт работы:
- инженер ОВ (1год)
- инженер-конструктор (5 лет)

Связаться со мной:
@Biscuitty''')
    elif message.text == 'Сертификаты':
        certif1 = open('1.jpg', 'rb')
        certif2 = open('2.jpg', 'rb')
        certif3 = open('3.jpg', 'rb')
        certif4 = open('4.jpg', 'rb')
        bot.send_photo(message.chat.id, certif1)
        bot.send_photo(message.chat.id, certif2)
        bot.send_photo(message.chat.id, certif3)
        bot.send_photo(message.chat.id, certif4)
    elif message.text == 'Мудрость':
        url = 'https://api.quotable.io/random'
        result = requests.get(url).json()['content']
        bot.send_message(message.chat.id, result)

    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMOYCkAAcOU8T-4VXdQ37mE7cTSX6nLAAKGAQACFkJrCi576oRhXPHGHgQ')

bot.polling() """