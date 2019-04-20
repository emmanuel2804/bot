import telebot
from telebot import types
from json import loads
from hero import Hero

bot = telebot.TeleBot("878916725:AAGpCSgEJB3UvmEUexOkSPmuIWiJcnBenJ0")
users = {}

def create_markup(*args):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    for i in args:
        markup.add(types.KeyboardButton('/' + i))

def bot_send_message(id, message, reply_markup=None):
    if reply_markup is None:
        reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        reply_markup.add(
            types.KeyboardButton('/me'),
            types.KeyboardButton('/forest')
        )

    bot.send_message(id, message, reply_markup=reply_markup)

@bot.message_handler(commands = ['forest'])
def forest(message):
    user = message.from_user

    bot_send_message(user.id, users[user.id].Forest())

@bot.message_handler(commands = ['me'])
def me(message):
    user = message.from_user

    bot_send_message(user.id, users[user.id])

@bot.message_handler(commands = ['start'])
def start(message):
    user = message.from_user
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    users[user.id] = Hero(user.id)

    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

    kbtn1 = types.KeyboardButton("Fermat")
    kbtn2 = types.KeyboardButton("Lagrange")
    kbtn3 = types.KeyboardButton("Newton")
    kbtn4 = types.KeyboardButton("Gauss")
    kbtn5 = types.KeyboardButton("Neumann")

    kb.add(kbtn2, kbtn1)
    kb.row(kbtn3, kbtn4)
    kb.row(kbtn5)

    try:
        bot_send_message(user.id, 'Escoge un castillo', reply_markup=kb)
        bot.register_next_step_handler(message, chosen_casttle)
    except Exception as e:                                # to be handled next
        print("An error occurred when processing 'Language Selector':", e)
        pass 

def chosen_casttle(msg):
    user = msg.from_user

    users[user.id].set_casttle(msg.text)
    users[user.id].set_name(user.username)

    bot_send_message(user.id, users[user.id])

def check_answer(rigth):
    bot.register_next_step_handler(message, checker, [rigth])

def checker(msg, *args):
    if msg.text[1:] == args[0]:
        response = 'Bravo valiente guerrero, el conocimiento es poder'
        response += '\nPregunta agregada a tu conocimiento'
        response += '\nHas ganado 2 exp'

        bot_send_message(msg.from_user.id, response)
        users[msg.from_user.id].exp += 2

bot.polling()