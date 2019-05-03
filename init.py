import telebot
from telebot import types
from json import loads
from hero import Hero
from castle import *
from initialize import *
from utils import *
import console
import data_handler
import re

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
    except Exception as identifier:
        bot_send_message(user.id, user.username + ' papa dale /start primero' +'\n' +identifier.__str__())

@bot.message_handler(commands = ['set_node'])
def set_node(message):
    try:
        user = message.from_user

        nodes = users[user.id].nodes
        new_nodes = []

        count = 0
        text = 'Escoja un nodo:\n'
        for node in nodes:
            text += '/node_' + str(count) + '\n'
            count += 1

        bot_send_message(user.id, text)
    except Exception as identifier:
        bot_send_message(user.id, 'Error en set_node\n' + str(identifier))

@bot.message_handler(commands = ['node_0', 'node_1', 'node_2', 'node_3', 'node_4', 'node_5', 'node_6'])
def chose_node(message):
    try:
        user = message.from_user

        chose = int(message.text.split('_')[-1])
        users[user.id].current_node.value = users[user.id].nodes[chose]
        bot_send_message(user.id, 'Nodo escogido')
    except Exception as identifier:
        bot_send_message(user.id, 'Error en chose_node con node\n' + str(identifier))

@bot.message_handler(commands = ['back_to_father'])
def back_to_father(message):
    try:
        user = message.from_user

        users[user.id].current_node = users[user.id].current_node.father
        bot_send_message(user.id, 'Nodo actual ' + str(users[user.id].current_node))
    except Exception as identifier:
        bot_send_message(user.id, 'Error en back_to_father\n' + str(identifier))

@bot.message_handler(commands = ['Fermat', 'Lagrange', 'Newton', 'Gauss', 'Neumann'])
def chose_target(message):
    try:
        user = message.from_user

        target = message.text[1:]
        hero = users[user.id]

        if hero.castillo == target:
            bot_send_message(user.id, "Castillo incorrecto")
            hero.chose_target()
            return

        path = get_path(castles[target].castle_tree)
        photo = open(path, 'rb')
        bot.send_photo(user.id, photo)
        photo.close()
    except Exception as identifier:
        bot_send_message(user.id, 'Error en chose_target\n' + str(identifier))

@bot.message_handler(commands = ['me'])
def me(message):
    try:        
        user = message.from_user

        bot_send_message(user.id, users[user.id])
    except Exception as e:
        bot_send_message(user.id, 'Cancio papa dale /start primero')

@bot.message_handler(commands = ['inv'])
def inv(message):
    print('entro en el metodo inv')
    try:
        user = message.from_user

        print('user id ', user.id)
        l = users[user.id].nodes
        print(l)
        result = ''
        count = 0

        for i in l:
            result += i + ' /i' + str(count) + '\n'
            count += 1
        print('termino de armar el inv ' + result)
        bot_send_message(user.id, result)
    except Exception as identifier:
        bot_send_message(user.id, 'aqui se rompe\n' + str(identifier))

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

@bot.message_handler(commands = ['set_edge'])
def set_edge(message):
    try:
        user = message.from_user

        src = message.text.split()[1]
        dst = message.text.split()[2]

        item = users[user.id].nodes[int(dst[1:])]
        castles[users[user.id].castillo].set_edge(int(src), item)
    except Exception as identifier:
        bot_send_message(user.id, 'Error, el uso correcto es /set_edge {padre id} {hijo id}\n' + str(identifier))

@bot.message_handler(commands = ['update_tree'])
def update_tree(message):
    user = message.from_user
    path = get_path(castles[users[user.id].castillo].castle_tree)
    
    photo = open(path, 'rb')
    bot.send_photo(user.id, photo)
    photo.close()
    bot_send_message(user.id, '/update_tree\n/set_edge {src id} {dst id}')

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
    
