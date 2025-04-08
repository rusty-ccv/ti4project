# caculator and battle simulator for Twilight Imperium 4th Edition.
# Duncan Sage
# 2025-04-05

# classes

#import
import json

class CombatAbilities:
    """
    Class to represent combat abilities.
    Antifighter barrage (AFB), bombardment, and space cannon.
    """
    def __init__(self):
        self.combat_values = {"hits_on": 0, "die_count": 0}
        self.afb_values = {"hits_on": 0, "die_count": 0}
        self.bombard_values = {"hits_on": 0, "die_count": 0}
        self.space_cannon_values = {"hits_on": 0, "die_count": 0}


class Production:
    """
    Class to represent production values.
    """
    def __init__(self):
        self.production_value = ''
        self.basic_production = ''


class Unit:
    """
    Base class for all units in the game.
    """

    def __init__(self):
        self.identity = ''
        self.base_type = ''
        self.name = ''
        self.subtitle = ''
        self.source = ''
        self.move_value = 0
        self.capacity_used = 0.0
        self.cost = 0.0
        self.capacity_value = 0
        self.upgrades_to_unit_id = ''
        self.upgrades_from_unit_id = ''
        self.required_tech_id = ''
        self.sustain_damage = False
        self.can_be_direct_hit = False
        self.planetary_shield = False
        self.afb = False
        self.bombard = False
        self.space_cannon = False
        self.deep_space_cannon = False
        self.disables_planetary_shield = False
        self.is_structure = False
        self.ground_force = False
        self.is_ship = False

    def print_unit_info(self):
        return f"Unit({self.identity}, {self.name}, {self.base_type}, {self.cost})"


#read json data
def convert_json_to_units():
    """
    Read JSON data from a file and convert it to Unit objects.
    """
    with open("data/units.json", "r") as file:
        data = json.load(file)
        for unit_data in data:
            unit = Unit()
            unit.identity = unit_data.get("id", "")
            unit.name = unit_data.get("name", "")
            unit.base_type = unit_data.get("baseType", "")
            unit.subtitle = unit_data.get("subtitle", "")
            unit.source = unit_data.get("source", "")
            unit.move_value = unit_data.get("moveValue", 0)
            unit.capacity_used = float(unit_data.get("capacityUsed", 0))
            unit.cost = float(unit_data.get("cost", 0.5))
            unit.capacity_value = unit_data.get("capacityValue", 0)
            unit.is_ship = unit_data.get("isShip", False)

            return unit


unit_object = convert_json_to_units()
print(unit_object.print_unit_info())
#print all unit names

