from castle import *
import threading as thr
from hero import Hero
from datetime import datetime, timedelta
from time import sleep

class Battle:
    def __init__(self):
        self.run_battle_thread = thr.Thread(target= self.run_battle)
        self.run_battle_thread.start()

    def run_battle(self):
        work_in_tree = False
        # OJO quitar el comentario de esta linea y ponerlo en la de abajo
        # para que el juego funcione correctamente
        # now = datetime.now()
        now = datetime(2019, 5, 3, 11, 51)

        if now.hour == 11 and now.minute >= 30 and now.minute < 50 and not work_in_tree:
            work_in_tree = True
            self.tree_construction()
        
        if now.hour == 11 and now.minute >= 50 and not chose_atack:
            chose_atack = True
            self.sharing_tree()

        sleep(10)

    def tree_construction(self):
        threads = []

        for castle in castles.keys():
            for hero in castles[castle]:
                # hero.in_quest = "Armando arbol de defensa"
                threads.append(thr.Thread(target=hero.put_node))
                threads[-1].start()

    def sharing_tree(self):
        threads = []

        for castle in castles.keys():
            for hero in castles[castle]:
                # hero.in_quest = "Armando arbol de defensa"
                threads.append(thr.Thread(target=hero.chose_target))
                threads[-1].start()