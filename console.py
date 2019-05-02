from time import sleep 
import data_handler
from initialize import bot

down = 'shutdown'
status = 'status'
hlp = 'help' 

def shell():
    while True:
        print ('=>:')
        cmd = input()
        if(cmd == down):
            data_handler.save_heros_states()
            print('ShutingDown...')
            bot.stop_polling()
            sleep(2)
            print('exiting...')
            exit()
        if(cmd == status):
            print('running...')
        if( cmd == hlp):
            print('Commands: \n1: shutdown\n2: status\n3: help\n')

# test 
# shell()