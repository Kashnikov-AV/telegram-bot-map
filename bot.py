import telebot
import sqlite3

'''
key = "1f429012d70048e998ac7596c116ea87"

response = requests.get('https://api.github.com')

https://api.opencagedata.com/geocode/v1/json?q=PLACENAME&key=YOUR-API-KEY

https://api.opencagedata.com/geocode/v1/json?q=LAT+LNG&key=YOUR-API-KEY
'''
token = "2069589275:AAEV-G8mZtYZR4P_W7O7ZFFc9zqnw6zbw50"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    return bot.send_message(message.chat.id, "Привет пользователь, этот бот сохраняет названия и адреса твоих любимых мест")

@bot.message_handler(commands=['add'])
def add_place(message):
    msg = bot.send_message(message.chat.id, 'введите название места')
    print(msg.text)
    bot.register_next_step_handler(msg, enter_name_place)


def enter_name_place(message):
    name = message.text
    msg_2 = bot.send_message(message.chat.id, 'введите адрес места')
    bot.register_next_step_handler(msg_2, enter_address_place, name)

def enter_address_place(message, name):
    address = message.text
    print(name, address, message.chat.id)
    try:
        conn = sqlite3.connect('place.db')
        cursor = conn.cursor()

        sql = """INSERT INTO place (user_id, name, address) VALUES (?, ?,?);"""
        param_tuple = (message.chat.id, name, address)
        cursor.execute(sql, param_tuple)
        conn.commit()
        conn.close()
    except:
        print('error')

@bot.message_handler(commands=['list'])
def list_of_place(message):
    bot.send_message(message.chat.id, 'ваши любимые места')
    chat_id = message.chat.id
    try:
        conn = sqlite3.connect('place.db')
        cursor = conn.cursor()
        sql = "SELECT name, address, user_id FROM place WHERE user_id=?  ORDER BY pk DESC LIMIT 10;"
        cursor.execute(sql, (chat_id,))
        list_of_place = []
        list_of_place = cursor.fetchall()

        if len(list_of_place) != 0:
            for pl in list_of_place:
                bot.send_message(message.chat.id, '{} - {}'.format(pl[0], pl[1]))
        else:
            bot.send_message(message.chat.id, 'мест нет')
        conn.close()
    except:
        print('error')

@bot.message_handler(commands=['reset'])
def reset_all(message):
    bot.send_message(message.chat.id, 'ваши места удалены')
    chat_id = message.chat.id
    try:
        conn = sqlite3.connect('place.db')
        cursor = conn.cursor()

        sql = """DELETE from place where user_id = ?;"""
        cursor.execute(sql, (chat_id,))
        conn.commit()
        conn.close()
    except:
        print('error')

if __name__ == '__main__':
    bot.polling()