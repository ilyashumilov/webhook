import telebot
from telebot import types, apihelper

token = '6035518578:AAEkKUp9yai17ljTJUT1vVv3oEh6Zk9XVnU'
bot = telebot.TeleBot(token)


def handler(data: dict) -> None:
    if message['text'] == 'Hellow':
        bot.send_message(data['chat']['id'], text='Hellow')