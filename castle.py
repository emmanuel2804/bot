class Castle:
    def __init__(self, name):
        self.name = name
        self.heros = []
        self.mission_tree = None
        self.castle_tree = None

    def add_hero(self, hero):
        self.heros.append(hero)

    def set_mission(self, tree):
        self.mission_tree = tree

castles =  {'Fermat'   : Castle('Fermat'), \
            'Lagrange' : Castle('Lagrange'),\
            'Newton'   : Castle('Newton'), \
            'Gauss'    : Castle('Gauss'), \
            'Neumann'  : Castle('Neumann')}