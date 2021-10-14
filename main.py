import sqlalchemy
import sqlite3
import telebot

token = "2069589275:AAEV-G8mZtYZR4P_W7O7ZFFc9zqnw6zbw50"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    return bot.send_message(message.chat.id, "привет пользователь, этот бот сохраняет твои любимые места")

if __name__ == '__main__':
    bot.polling()