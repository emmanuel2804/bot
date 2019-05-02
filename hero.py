from quest import Forest
from arena import *
from threading import Timer
from utils import *

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

        # Dictionary<int, List<Tuple<string, int, List<posibles respuestas>>>> questions
        self.ACK = {}

    def set_name(self, name):
        self.Name = name

    def set_casttle(self, casttle):
        self.castillo = casttle

    def __str__(self):
        result = ''
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

        # TODO: hacer aqui la pincha con hilos, crear un metodo que cuando
        # se cumpla t tiempo ponga en falso self.in_quest, sume la exp y
        # gold obtenido en el quest y te realice la pregunta en caso de que
        # te toque alguna. Si aceptaste en la pregunta agregarla a tus
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

        check_answer(question[1], message)
        # if respuesta == question[1]:
        #     print('Bravo valiente guerrero, el conocimiento es poder')
        #     print('Pregunta agregada a tu conocimiento')
        #     self.exp += 2
        #     print('Has ganado 2 exp')

    def Arena(self, message):
        result = matching(self, message)

        if not result:
            t = Timer(10, no_oponente)

    def no_oponente(self):
        bot_send_message(self.player_id, 'No se encontro oponente')
        self.in_quest = None

    def lvl_up(self):
        if self.exp >= exp_for_lvl[self.lvl + 1]:
            bot_send_message(self.player_id, "Felicitaciones, has subido de nivel")

            self.lvl += 1
            self.attack +=1
            self.defense += 1