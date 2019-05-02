import os
import pickle
from initialize import users
from hero import Hero

saved_ids = {}
folder = '__binaries__'
functions_folder = '__functions__'
methods_folder = '__methods__'

#aqui estaran guardadas los fragmentos de las conferencias
#bajo la expresion regular cf_id_fragment
#ejemplo cf_02_07
conference_ack = '__conferences__'

#------------------------------------------------------------------------------------------
def save_heros_states():
    for i in users.keys():
        save_user(users[i])

def save_user(hero):
    
    try:
        fd = os.open(folder + '/' + hero.player_id.__str__(), os.O_WRONLY)
        s = hero.__dict__
        p = pickle.dumps(s)
        os.write(fd, p)
        os.close(fd)
        print('User updated!')

    except Exception as e:
        fd = os.open(folder + '/' + hero.player_id.__str__(), os.O_WRONLY + os.O_CREAT)
        s = hero.__dict__
        p = pickle.dumps(s)
        os.write(fd, p)
        os.close(fd)
        print('User saved!')


def load_user_hero(user_id):
    
    try:
        # abre el archivo y lo lee si lo encuentra
        fd = os.open(folder + '/' + user_id.__str__(), os.O_RDONLY)
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
        print(e.__str__() + '   <----UserNotLoaded')
        return


def save_ids():
    fd = os.open(folder+'/'+'saved_ids', os.O_APPEND + os.O_CREAT + os.O_WRONLY)
    id_list = []
    for i in users.keys():
        id_list.append(i)
    
    try:
        
    except:

    # TODO
    return
    

def init():
    try:
        os.mkdir(folder)
    except Exception as e:
        print(e.__str__() + '       <--Handled!')
    try:
        os.mkdir(functions_folder)
    except Exception as e:
        print(e.__str__() + '       <--Handled!')
    try:
        os.mkdir(methods_folder)
    except Exception as e:
        print(e.__str__() + '       <--Handled!')
    try:
        os.mkdir(conference_ack)
    except Exception as e:
        print(e.__str__() + '       <--Handled!')
    # una vez iniciando entrar a la carpeta __binaries__
    # buscando los usuarios que han sido guardados, q va a estar en un archivito llamado
    # suid (saved user id) que estara en disco tambien
    



# test
# a = Hero(1)
# save_user(a)

# load_user_hero(1)
# print(users[1].NoStamina())