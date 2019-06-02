import telebot
from telebot import types, apihelper
from json import loads
from hero import Hero
from castle import *
from initialize import *
from utils import *
from sys import argv
import console
import data_handler
import re

@bot.message_handler(func=lambda message: True)
def not_start(message):
    user = message.from_user

    if(not users.keys().__contains__(user.id)):
        start(message)
        return

    text = message.text

    if text == '/me': me(message)
    elif text == '/start' and not users.keys().__contains__(user.id) : start(message)
    elif text == '/forest' : forest(message)
    elif text == '/arena' : arena(message)
    elif text == '/inv' : inv(message)
    elif text == '/back_to_father' : back_to_father(message)
    elif text == '/chose_node' : chose_node(message)
    elif text == '/chose_target' : chose_target(message)
    elif text == '/set_edge' : set_edge(message)
    elif text == '/set_node' : set_node(message)
    elif text == '/update_tree' : update_tree(message)
    else:
        bot_send_message(user.id, "Comando desconocido")

@bot.message_handler(commands = ['forest'])
def forest(message):
    try:
        user = message.from_user

        bot_send_message(user.id, users[user.id].Forest(message))
    except Exception as e:
        print("Un error ha ocurrido en el metodo Forest de init.py:\n", e)

@bot.message_handler(commands = ['arena'])
def arena(message):
    try:
        user = message.from_user

        bot_send_message(user.id, users[user.id].Arena(message))
    except Exception as e:
        print("Un error ha ocurrido en el metodo Arena de init.py:\n", e)

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
    except Exception as e:
        print("Un error ha ocurrido en el metodo set_node de init.py:\n", e)

@bot.message_handler(commands = ['node_0', 'node_1', 'node_2', 'node_3', 'node_4', 'node_5', 'node_6'])
def chose_node(message):
    try:
        user = message.from_user

        chose = int(message.text.split('_')[-1])
        users[user.id].current_node.value = users[user.id].nodes[chose]
        bot_send_message(user.id, 'Nodo escogido')
    except Exception as e:
        print("Un error ha ocurrido en el metodo chose_node de init.py:\n", e)

@bot.message_handler(commands = ['back_to_father'])
def back_to_father(message):
    try:
        user = message.from_user

        users[user.id].current_node = users[user.id].current_node.father
        bot_send_message(user.id, 'Nodo actual ' + str(users[user.id].current_node))
    except Exception as e:
        print("Un error ha ocurrido en el metodo back_to_father de init.py:\n", e)

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
    except Exception as e:
        print("Un error ha ocurrido en el metodo chose_target de init.py:\n", e)

@bot.message_handler(commands = ['me'])
def me(message):
    try:        
        user = message.from_user

        bot_send_message(user.id, users[user.id])
    except Exception as e:
        print("Un error ha ocurrido en el metodo me de init.py:\n", e)

@bot.message_handler(commands = ['inv'])
def inv(message):
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
        bot_send_message(user.id, result)
    except Exception as e:
        print("Un error ha ocurrido en el metodo inv de init.py:\n", e)

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

    try:
        bot_send_message(user.id, 'Escoge un castillo', reply_markup=kb_castles)
        bot.register_next_step_handler(message, chosen_casttle)
    except Exception as e:                                # to be handled next
        print("An error occurred when processing 'Language Selector':", e)

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
    if len(argv) > 1 and argv[1] == '--proxy':
        addproxy()

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
    
