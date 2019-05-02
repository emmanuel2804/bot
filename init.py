import telebot
from telebot import types
from json import loads
from hero import Hero
from initialize import *
from utils import *
import console
import data_handler

@bot.message_handler(commands = ['forest'])
def forest(message):
    try:
        user = message.from_user

        bot_send_message(user.id, users[user.id].Forest(message))
    except Exception as e:
        bot_send_message(user.id, user.username + 'papa dale /start primero')

@bot.message_handler(commands = ['arena'])
def arena(message):
    try:
        user = message.from_user

        bot_send_message(user.id, users[user.id].Arena(message))
    except expression as identifier:
        bot_send_message(user.id, user.username + 'papa dale /start primero')

@bot.message_handler(commands = ['me'])
def me(message):
    try:        
        user = message.from_user

        bot_send_message(user.id, users[user.id])
    except Exception as e:
        bot_send_message(user.id, 'Cancio papa dale /start primero')

@bot.message_handler(commands = ['help'])
def help(message):
    user = message.from_user
    bot.send_message(id, 'Hello!! Iam in development phase, anything you can help, notify to my masters :-) ')

@bot.message_handler(commands = ['start'])
def start(message):
    user = message.from_user
    # print(message.chat_id)
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


def main():
    # Start command console
    print('setting environment')
    data_handler.init()
    
    thread_pool = {}

    shell_t = thr.Thread(target=console.shell)
    thread_pool['shell_t'] = shell_t
    shell_t.start()
    
    # start API service
    print('Service Started!')
    bot.polling()
    return


if __name__ == '__main__':
    main()
    
