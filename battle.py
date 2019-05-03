from castle import *
import threading as thr
from hero import Hero

class Battle:
    def __init__(self):
        self.run_battle_thread = thr.Thread(target= self.run_battle)
        self.run_battle_thread.start()

    def tree_construction(self):
        threads = []

        for castle in castles.keys:
            for hero in castles[castle]:
                # hero.in_quest = "Armando arbol de defensa"
                threads.append(thr.Thread(target=hero.put_node))
                threads[-1].start()