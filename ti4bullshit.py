# caculator and battle simulator for Twilight Imperium 4th Edition.
# Duncan Sage
# 2025-04-05

# classes

#import
import csv

class Unit:
    '''
    Base class for all units in the game.
    '''
    def __init__(self):
        self._name = ''
        self._unit_type = ''
        self._abilities = []
        self._capacity = 0
        self._faction_specific = False
        self._faction = ''

    # getters and setters with validation
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    def get_unit_type(self):
        return self._unit_type

    def set_unit_type(self, unit_type):
        if isinstance(unit_type, str) and unit_type:
            self._unit_type = unit_type
        else:
            raise ValueError("Unit type must be a non-empty string")

    def get_abilities(self):
        return self._abilities

    def set_abilities(self, abilities):
        if isinstance(abilities, list):
            self._abilities = abilities
        else:
            raise ValueError("Abilities must be a list")

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        if isinstance(capacity, int) and capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity must be a non-negative integer")

    def get_faction_specific(self):
        return self._faction_specific

    def set_faction_specific(self, faction_specific):
        if isinstance(faction_specific, bool):
            self._faction_specific = faction_specific
        else:
            raise ValueError("Faction specific must be a boolean")

class Structure(Unit):
    '''
    Base class for all structures in the game. Inherits from Unit.
    '''
    def __init__(self):
        super().__init__()
        self.name = ''
        self.unit_type = 'Structure'
        self.abilities = []


class Ship(Unit):
    '''
    Base class for all ships in the game. Inherits from Unit.
    '''
    def __init__(self, name, unit_type, abilities, capacity, movement, hit_on, combat_dice_number, ship_type):
        '''
        :param name: Name of the unit in game.
        :param unit_type: Type of the unit (e.g., "Ship").
        :param abilities: A list of abilities the unit has.
        :param capacity: How many units it can carry.
        :param movement: How many systems it can move.
        :param hit_on: What die number it hits on.
        :param combat_dice_number: How many dice it rolls in combat.
        :param ship_type: Further classification of the ship unit type (e.g., "Fighter", "Capital ship").
        '''
        super().__init__()
        self.name = name
        self.unit_type = unit_type
        self.abilities = abilities
        self.capacity = capacity
        self._movement = movement
        self._hit_on = hit_on
        self._combat_dice_number = combat_dice_number
        self._ship_type = ship_type

    # getters and setters with validation
    def get_movement(self):
        return self._movement

    def set_movement(self, movement):
        if isinstance(movement, int) and movement >= 0:
            self._movement = movement
        else:
            raise ValueError("Movement must be a non-negative integer")

    def get_hit_on(self):
        return self._hit_on

    def set_hit_on(self, hit_on):
        if isinstance(hit_on, int) and hit_on >= 0:
            self._hit_on = hit_on
        else:
            raise ValueError("Hit on must be a non-negative integer")

    def get_combat_dice_number(self):
        return self._combat_dice_number

    def set_combat_dice_number(self, combat_dice_number):
        if isinstance(combat_dice_number, int) and combat_dice_number >= 0:
            self._combat_dice_number = combat_dice_number
        else:
            raise ValueError("Combat dice number must be a non-negative integer")

    def get_ship_type(self):
        return self._ship_type

    def set_ship_type(self, ship_type):
        if isinstance(ship_type, str) and ship_type:
            self._ship_type = ship_type
        else:
            raise ValueError("Ship type must be a non-empty string")

with open('data/ships.csv') as csvfile:
