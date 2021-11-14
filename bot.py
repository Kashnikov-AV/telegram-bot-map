import telebot
import sqlite3
import requests



token = "2069589275:AAEV-G8mZtYZR4P_W7O7ZFFc9zqnw6zbw50"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    return bot.send_message(message.chat.id, "Привет пользователь, этот бот сохраняет координаты и фото твои любимых мест")

@bot.message_handler(commands=['add'])
def add_place(message):
    bot.send_message(message.chat.id, 'введите название места')
    #bot.

    #cursor = sqlite3.connect('place.db')

    bot.send_location(message.chat.id)



@bot.message_handler(commands=['list'])
def list_of_place(message):
    return bot.send_message(message.chat.id, 'ваши любимые места')

@bot.message_handler(commands=['reset'])
def reset_all(message):
    return bot.send_message(message.chat.id, 'очищение')

if __name__ == '__main__':
    bot.polling()