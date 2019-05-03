import networkx as nx
from tree import *

class Castle:
    def __init__(self, name):
        self.name = name
        self.heros = []
        self.mission_tree = nx.DiGraph()
        self.castle_tree = nx.DiGraph()
        self.castle_tree.add_node(nodos[0])
        self.nodes = [nodos[0]]
        self.nodes_by_id = {0 : nodos[0]}

    def add_hero(self, hero):
        self.heros.append(hero)

    def set_mission(self, tree):
        self.mission_tree = tree

    def set_edge(self, src_id, dst):
        if not self.nodes.__contains__(dst):
            c = len(self.nodes)
            self.nodes.append(dst)
            self.nodes_by_id[c] = dst

        self.castle_tree.add_node(dst)
        self.castle_tree.add_edge(self.nodes_by_id[src_id], dst)

castles =  {'Fermat'   : Castle('Fermat'), \
            'Lagrange' : Castle('Lagrange'),\
            'Newton'   : Castle('Newton'), \
            'Gauss'    : Castle('Gauss'), \
            'Neumann'  : Castle('Neumann')}