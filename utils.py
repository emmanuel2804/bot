from initialize import *
from telebot import types

exp_for_lvl = {1:0,     11:721,	    21:6719, 	31:54934, 	41:192353,\
               2:5,     12:902,	    22:8399, 	32:63979, 	42:213765,\
               3:15,    13:1127, 	23:10498, 	33:73838, 	43:237105,\
               4:38,    14:1409, 	24:13123, 	34:84584, 	44:262545,\
               5:79,    15:1761, 	25:16404, 	35:96297, 	45:290275,\
               6:142,   16:2202, 	26:20504, 	36:109065, 	46:320501,\
               7:227,   17:2752, 	27:25631, 	37:122982, 	47:353447,\
               8:329,   18:3440, 	28:32038, 	38:138151, 	48:389358,\
               9:444,   19:4300, 	29:39023, 	39:154685, 	49:428501,\
               10:577, 	20:5375, 	30:46636, 	40:172708, 	50:471167}

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
            types.KeyboardButton(tree_emoji+'forest'),
            types.KeyboardButton('/arena')
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

def chose_attack(message):
    return bot.register_next_step_handler(message,return_next_message)

def return_next_message(msg):
    return msg