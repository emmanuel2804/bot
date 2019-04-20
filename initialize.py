import telebot
from emoji import emojize

bot = telebot.TeleBot("878916725:AAGpCSgEJB3UvmEUexOkSPmuIWiJcnBenJ0")
users = {}

tree_emoji = emojize(":evergreen_tree:", use_aliases=True)