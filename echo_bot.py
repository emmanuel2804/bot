import telebot

# TODO: cambiar TOKEN por mi token valido
bot = telebot.TeleBot("878916725:AAGpCSgEJB3UvmEUexOkSPmuIWiJcnBenJ0")

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func = lambda m : True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()