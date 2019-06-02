import telebot
# from emoji import emojize
import threading as thr
from json import loads

bot = telebot.TeleBot("878916725:AAGpCSgEJB3UvmEUexOkSPmuIWiJcnBenJ0")

print('Starting!')

users = {}

# tree_emoji = emojize(":evergreen_tree:", use_aliases=True)

def addproxy():
    file = open('proxy.json', 'r')
    text = file.read()
    file.close()

    config = loads(text)

    # bot.apihelper.proxy = {'https' : 'socks5://' + config['userproxy'] + ':' + config['passproxy'] + 
    #     '@' + config['proxy_address'] + ':' + config['proxy_port']}

    telebot.apihelper.proxy = {'https' : 'socks5://' + config['userproxy'] + ':' + config['passproxy'] + 
        '@' + config['proxy_address'] + ':' + config['proxy_port']}