import telebot
from telebot import types
from json import loads
from hero import Hero
from initialize import *
from utils import *

@bot.message_handler(commands = ['forest'])
def forest(message):
    user = message.from_user

    bot_send_message(user.id, users[user.id].Forest(message))

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

bot.polling()