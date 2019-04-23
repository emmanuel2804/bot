from threading import Timer
from random import Random
from utils import *
import os, time

# Cuando un heroe esta buscando batallas en la arena
# entra en este diccionario y ve si hay alguien de su
# mismo nivel, si hay alguien los empareja para que
# luchen, de lo contrario se agrega este heroe en la
# espera de otro de su mismo nivel
# Dictionary<int(level), Tuple(Hero, message_del_Hero)>
heroes = {}

def matching(hero, message):
    if heroes[hero.lvl] is None:
        heroes[hero.lvl] = (hero, message)
        hero.in_quest = 'Buscando adversario'
        t = Timer()
        return False

    hero2 = heroes[hero.lvl]
    heroes[hero.lvl] = None
    figth(hero, hero2[0], message, hero2[1])

def figth(hero1, hero2, message1, message2):
    hero1_life = 100
    hero2_life = 100

    hero1.in_quest = 'En batalla, vida: ' + str(hero1_life)
    hero2.in_quest = 'En batalla, vida: ' + str(hero2_life)

    while hero1_life > 0 and hero2_life > 0:
        rand = Random()
        # TODO: cambiar ACK[1] para que escoja preguntas de todos
        # los niveles de conocimientos
        questions1 = rand.sample(hero1.ACK[1], 3)
        questions2 = rand.sample(hero2.ACK[1], 3)

        q1 = ['0-' + questions1[0][0][:5], '1-' + questions1[1][0][:5], '2-' + questions1[2][0][:5]]
        q2 = ['0-' + questions2[0][0][:5], '1-' + questions2[1][0][:5], '2-' + questions2[2][0][:5]]

        mark1 = create_markup(q1)
        mark2 = create_markup(q2)

        bot_send_message(hero1.player_id, 'Escoja su ataque', reply_markup=mark1)
        bot_send_message(hero2.player_id, 'Escoja su ataque', reply_markup=mark2)

        atk1 = None
        atk2 = None

        atk1 = chose_attack(message1)
        atk2 = chose_attack(message2)

        time.sleep(10)

        def1 = None
        def2 = None

        if atk1 != None:
            mark1 = create_markup(questions1[int(atk1[:1])][3])
            bot_send_message(hero2.player_id, 'Escoge una respuesta correcta' + \
                ' para defenderte del ataque de tu adversario')

            bot_send_message(hero2.player_id, questions1[int(atk1[:1])][0], mark1)

            def2 = chose_defense(message2)
        else:
            bot_send_message(hero2.player_id, 'Tu enemigo no escogio ningun ataque')

        if atk2 != None:
            mark2 = create_markup(questions2[int(atk2[:1])][3])
            bot_send_message(hero1.player_id, 'Escoge una respuesta correcta' + \
                ' para defenderte del ataque de tu adversario')

            bot_send_message(hero1.player_id, questions2[int(atk2[:1])][0], mark2)

            def1 = chose_defense(message1)
        else:
            bot_send_message(hero1.player_id, 'Tu enemigo no escogio ningun ataque')

        time.sleep(10)

        if atk1 != None:
            if def2 != None:
                if questions1[int(atk1[:1])][1] == int(def2):
                    bot_send_message(hero2.player_id, 'Genial, has usado tu defensa para parar parte del ataque')
                    if hero2.defense < hero1.attack:
                        hero2_life = hero2_life - (hero1.attack - hero2.defense)
                else:
                    bot_send_message(hero2.player_id, 'Respuesta incorrecta, tu enemigo te ataca con toda su fuerza')
                    hero2_life = hero2_life - hero1.attack
            else:
                bot_send_message(hero2.player_id, 'No te has defendido a tiempo, tu enemigo te ataca con toda su fuerza')
                hero2_life = hero2_life - hero1.attack
        else:
            bot_send_message(hero2.player_id, 'Tu enemigo no ataco, no tienes de que preocuparte')

        if atk2 != None:
            if def1 != None:
                if questions2[int(atk1[:1])][1] == int(def1):
                    bot_send_message(hero1.player_id, 'Genial, has usado tu defensa para parar parte del ataque')
                    if hero1.defense < hero2.attack:
                        hero1_life = hero1_life - (hero2.attack - hero1.defense)
                else:
                    bot_send_message(hero1.player_id, 'Respuesta incorrecta, tu enemigo te ataca con toda su fuerza')
                    hero1_life = hero1_life - hero2.attack
            else:
                bot_send_message(hero1.player_id, 'No te has defendido a tiempo, tu enemigo te ataca con toda su fuerza')
                hero1_life = hero1_life - hero2.attack
        else:
            bot_send_message(hero1.player_id, 'Tu enemigo no ataco, no tienes de que preocuparte')