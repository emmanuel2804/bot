import os
import pickle
from initialize import users
from hero import Hero


folder = '__binaries__'

#------------------------------------------------------------------------------------------
def save_heros_states():
    for i in users:
        save_user(i)
        
def save_user(hero):
    
    try:
        fd = os.open(hero.player_id.__str__(), os.O_WRONLY)
        s = hero.__dict__
        p = pickle.dumps(s)
        os.write(fd, p)
        os.close(fd)
        print('User updated!')

    except Exception as e:
        fd = os.open(hero.player_id.__str__(), os.O_WRONLY + os.O_CREAT)
        s = hero.__dict__
        p = pickle.dumps(s)
        os.write(fd, p)
        os.close(fd)
        print('User saved!')


def load_user_hero(user_id):
    
    try:
        # abre el archivo y lo lee si lo encuentra
        fd = os.open(user_id.__str__(), os.O_RDONLY)
        h = os.read(fd,4096)
        os.close(fd)

        # decodifica el contenido y lo almacena en users
        t = pickle.loads(h)
        attrs = []
        for i in t.keys():
            attrs.append(t[i])

        o = Hero.__new__(Hero)
        o.__dict__.update(t)

        users[user_id] = o
        print('User hero loaded')
        


    except Exception as e:
        print(e)
        return e

# test
# a = Hero(1)
# save_user(a)

# load_user_hero(1)
# print(users[1].NoStamina())