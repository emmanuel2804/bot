from initialize import *
from telebot import types

def create_markup(*args):
    # print(args)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    for i in args[0]:
        # print('tecla ', i, ' agregada')
        markup.add(types.KeyboardButton(i))

    return markup

def bot_send_message(id, message, reply_markup=None):
    if reply_markup is None:
        reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        reply_markup.add(
            types.KeyboardButton('/me'),
            types.KeyboardButton('/forest')
        )

    bot.send_message(id, message, reply_markup=reply_markup)

def chosen_casttle(msg):
    user = msg.from_user

    users[user.id].set_casttle(msg.text)
    users[user.id].set_name(user.username)

    bot_send_message(user.id, users[user.id])

def check_answer(rigth, message):
    bot.register_next_step_handler(message, checker, [rigth])

def checker(msg, *args):
    # print(type(msg.text))
    # print(type(args[0][0]))
    # print(msg.text[1:] == str(args[0][0]))
    if msg.text == str(args[0][0]):
        response = 'Bravo valiente guerrero, el conocimiento es poder'
        response += '\nPregunta agregada a tu conocimiento'
        response += '\nHas ganado 2 exp'

        users[msg.from_user.id].exp += 2
        bot_send_message(msg.from_user.id, response)