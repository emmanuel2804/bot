from quest import *
from arena import *
import time
import threading as thr
from utils import *
from datetime import datetime, timedelta
from math import floor
from castle import *

class Hero:

    def __init__(self, id):
        self.player_id = id
        self.lvl = 1
        self.attack = 1
        self.defense = 1
        self.stamina = 3
        self.stamina_base = 5
        self.exp = 0
        self.mana = 0
        self.mana_base = 0
        self.gold = 0
        self.in_quest = None
        self.regenerating = False
        self.stamina_regen_thread = thr.Thread(target= self.stamina_regen)
        self.stamina_regen_thread.start()
        self.current_node = None
        self.nodes = ['nodo1', 'nodo2']
        # self.t = thr.Thread(target = self.testing)
        # self.t.start()

        # Dictionary<int, List<Tuple<string, int, List<posibles respuestas>>>> questions
        self.ACK = questions

    def set_name(self, name):
        self.Name = name

    def set_casttle(self, casttle):
        self.castillo = casttle

    def __str__(self):
        result = ''
        result += self.time_for_next_battle()[2] + '\n'
        result += self.Name + ' del castillo ' + str(self.castillo) + '\n'
        result += 'Level: ' + str(self.lvl) + '\n'
        result += 'Atk: ' + str(self.attack) + ' Def: ' + str(self.defense) + '\n'
        result += 'Exp: ' + str(self.exp) + '/' + str(exp_for_lvl[self.lvl + 1]) + '\n'
        result += 'Stamina: ' + str(self.stamina) + '/' + str(self.stamina_base) + '\n'
        
        if self.lvl >= 10:
            result += 'Mana: ' + str(self.mana) + '/' + str(self.mana_base) + '\n'

        result += 'Gold: ' + str(self.gold)

        result += '\nState:\n'
        if self.in_quest is None:
            result += 'Rest In Peace'
        else:
            result += self.in_quest

        return result

    def Forest(self, message):
        if self.stamina == 0:
            return self.NoStamina()

        if self.in_quest != None:
            return self.in_quest

        self.stamina -= 1
        question = Forest(self.lvl)

        # Si aceptaste en la pregunta agregarla a tus
        # posibles preguntas
        self.in_quest = 'Viajando por el bosque en busca de nuevos conocimientos'
        t = Timer(10, self.time_gone, [question, message], {})
        t.start()

        return self.in_quest

    def NoStamina(self):
        # TODO: averiguar como sacar un hash para que cada jugador tenga
        # un codigo unico para invitar a otroas personas para conseguir
        # mas stamina base
        return 'El jugador no dispone de stamina, vuelva mas tarde'

    # metodo que es llamado cuando se termina el tiempo de un quest
    def time_gone(self, question, message):
        self.in_quest = None

        self.exp += 1
        self.gold += 1
        bot_send_message(self.player_id, 'Ganaste 1 exp y 1 gold')
        self.lvl_up()

        if question == None:
            return

        # bot_send_message(self.player_id, 'En tu viaje te has encontrado con un antiguo sabio')

        # TODO: hacerle shuffle a las posibles respuestas
        text = 'En tu viaje te has encontrado con un antiguo sabio\n' + \
            'Este te hace la siguiente pregunta\n' + '\"' + question[0] + '\"'

        bot_send_message(self.player_id, text, create_markup(question[2]))
        # respuesta = int(input('Cual es tu respuesta?: '))

        check_answer(question, message)
        # if respuesta == question[1]:
        #     print('Bravo valiente guerrero, el conocimiento es poder')
        #     print('Pregunta agregada a tu conocimiento')
        #     self.exp += 2
        #     print('Has ganado 2 exp')

    def Arena(self, message):
        if self.in_quest != None:
            return self.in_quest
            
        print('Entrando a arena llamando a matching')
        result = matching(self, message)

        if not result:
            t = Timer(120, self.no_oponente)
            t.start()
            return 'El campo de batalla esta desolado ,no hay indicios de oponentes, esperemos...'

    def no_oponente(self):
        bot_send_message(self.player_id, 'No se encontro oponente')
        self.in_quest = None

    def stamina_regen(self):
        
        while(True):
            if(self.stamina < self.stamina_base and not self.regenerating):
                print('regenerando stamina')
                timer = thr.Timer(30,self.add_stamina_point,args=None)
                timer.start()
                self.regenerating = True
                

    def add_stamina_point(self):
        self.regenerating = False
        self.stamina+=1
        print(self.stamina)
    

    def lvl_up(self):
        if self.exp >= exp_for_lvl[self.lvl + 1]:
            bot_send_message(self.player_id, "Felicitaciones, has subido de nivel")

            self.lvl += 1
            self.attack +=1
            self.defense += 1

    def time_for_next_battle(self):
        now = datetime.now()
        
        if now.hour >= 12:
            next_battle = datetime(now.year, now.month, now.day + 1, 12)
        else:
            next_battle = datetime(now.year, now.month, now.day, 12)

        diff = next_battle - now

        l_min = floor((diff.seconds / 60) % 60)
        l_hour = floor(diff.seconds / 3600)

        result = "Batalla en "

        if l_hour == 0:
            result += str(l_min) + " minutos"
        else:
            result += str(l_hour) + " h " + str(l_min) + " minutos"

        return (l_hour, l_min, result)

    def put_node(self):
        self.in_quest = 'La batalla se acerca, saca tus nodos y arma un buen arbol de defensa.\n'\
            + 'Recuerda que tus enemigos pueden encontrar brechas en tu arbol de defensa'
        bot_send_message(self.player_id, self.in_quest)

        if self.current_node is None:
            self.current_node = castles[self.castillo].castle_tree

        mk = create_markup('/set_node', '/left_child', '/rigth_child')
        bot_send_message(self.player_id, self.current_node, reply_markup=mk)

    def chose_target(self):
        text = "Escoge un castillo para atacar\n"

        for castle in castles.keys():
            if castle != self.castillo:
                text += '\\' + castle + '\n'

        bot_send_message(self.player_id, text)