class Hero:

    def __init__(self, castillo, name):
        self.lvl = 1
        self.attack = 1
        self.defense = 1
        self.stamina = 3
        self.stamina_base = 5
        self.exp = 0
        self.mana = 0
        self.mana_base = 0
        self.gold = 0
        self.in_quest = False
        self.castillo = castillo
        self.Name = name

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