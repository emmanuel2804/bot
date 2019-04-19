import telebot
from telebot import types
from json import loads
from hero import Hero

bot = telebot.TeleBot("878916725:AAGpCSgEJB3UvmEUexOkSPmuIWiJcnBenJ0")
users = {}

@bot.message_handler(commands = ['start'])
def start(message):
    user = message.from_user.id
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)

    users[user] = Hero()

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
        bot.reply_to(message, 'Escoge un castillo',
                            parse_mode='markdown', reply_markup=kb)
        bot.register_next_step_handler(message, chosen_lang)  # sends the msg, and register the 'chosen_lang' func
    except Exception as e:                                # to be handled next
        print("An error occurred when processing 'Language Selector':", e)
        pass 

def chosen_lang(msg):
    # print('lenguaje escogido ', msg)
    # result = loads(msg)
    print(msg.text)

bot.polling()