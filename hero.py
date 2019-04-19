from quest import Forest
from threading import Timer

class Hero:

    def __init__(self):
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

    def set_name(self, name):
        self.Name = name

    def set_casttle(self, casttle):
        self.Casttle = casttle

    def __str__(self):
        result = ''
        result += self.Name + ' del castillo ' + self.castillo + '\n'
        result += 'Level: ' + str(self.lvl) + '\n'
        result += 'Atk: ' + str(self.attack) + ' Def: ' + str(self.defense) + '\n'
        result += 'Exp: ' + str(self.exp) + '\n'
        result += 'Stamina: ' + str(self.stamina) + '/' + str(self.stamina_base) + '\n'
        
        if self.lvl >= 10:
            result += 'Mana: ' + str(self.mana) + '/' + str(self.mana_base) + '\n'

        result += 'Gold: ' + str(self.gold)

        return result

    def Forest(self):
        if self.stamina == 0:
            print(self.NoStamina())
            return

        if self.in_quest != None:
            print(self.in_quest)
            return

        self.stamina -= 1
        question = Forest(self.lvl)

        # TODO: hacer aqui la pincha con hilos, crear un metodo que cuando
        # se cumpla t tiempo ponga en falso self.in_quest, sume la exp y
        # gold obtenido en el quest y te realice la pregunta en caso de que
        # te toque alguna. Si aceptaste en la pregunta agregarla a tus
        # posibles preguntas
        self.in_quest = 'Viajando por el bosque en busca de nuevos conocimientos'
        t = Timer(10, self.time_gone, [question], {})
        t.start()

    def NoStamina(self):
        # TODO: averiguar como sacar un hash para que cada jugador tenga
        # un codigo unico para invitar a otroas personas para conseguir
        # mas stamina base
        return 'El jugador no dispone de stamina, vuelva mas tarde'

    # metodo que es llamado cuando se termina el tiempo de un quest
    def time_gone(self, question):
        self.in_quest = None

        self.exp += 1
        self.gold += 1
        print('Ganaste 1 exp y 1 gold')

        if question == None:
            return

        print('En tu viaje te has encontrado con un antiguo sabio')
        print('Este te hace la siguiente pregunta\n', '\"', question[0], '\"')
        respuesta = int(input('Cual es tu respuesta?: '))

        if respuesta == question[1]:
            print('Bravo valiente guerrero, el conocimiento es poder')
            print('Pregunta agregada a tu conocimiento')
            self.exp += 2
            print('Has ganado 2 exp')