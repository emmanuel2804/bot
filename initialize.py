import telebot
from emoji import emojize
import threading as thr

bot = telebot.TeleBot("878916725:AAGpCSgEJB3UvmEUexOkSPmuIWiJcnBenJ0")

print('Starting!')

users = {}

tree_emoji = emojize(":evergreen_tree:", use_aliases=True)
