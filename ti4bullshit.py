# caculator and battle simulator for Twilight Imperium 4th Edition.
# Duncan Sage
# 2025-04-05

# classes

class Unit:
    def __init__(self):
        self.name = ''
        self.unit_type = ''
        self.abilities = []
        self.capacity = 0

class Structure(Unit):
    def __init__(self):
        super().__init__()
        self.name = ''
        self.unit_type = 'Structure'
        self.abilities = []

class Ship(Unit):
    def __init__(self, name, unit_type, abilities, capacity):
        super().__init__()
        self.name = name
        self.unit_type = unit_type
        self.abilities = abilities
        self.capacity = capacity
        self.movement = 0
        self.hit_on = 0
        self.combat_dice_number = 0



