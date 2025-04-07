# caculator and battle simulator for Twilight Imperium 4th Edition.
# Duncan Sage
# 2025-04-05

# classes

#import
import json

class Unit:
    """
    Base class for all units in the game.
    """

    def __init__(self):
        self._identity = ''
        self._base_type = ''
        self._name = ''
        self._subtitle = ''
        self._source = ''
        self._move_value = 0
        self._capacity_used = 0.0
        self._cost = 0
        self._capacity_value = 0

        self._combat_hits_on = 0
        self._combat_die_count = 0

        self._upgrades_to_unit_id = ''
        self._upgrades_from_unit_id = ''
        self._required_tech_id = ''

        self._afb_hits_on = 0
        self._afb_die_count = 0

        self._bombard_hits_on = 0
        self._bombard_die_count = 0

        self._sustain_damage = False
        self._can_be_direct_hit = False

        self._space_cannon_hits_on = 0
        self._space_cannon_die_count = 0
        self._planetary_shield = False
        self._deep_space_cannon = False

        self._is_structure = False
        self._ground_force = False
        self._is_ship = False

        self._production_value = ''
        self._basic_production = ''
        self._disables_planetary_shield = False

    @property
    def id(self):
        return self._identity

    @id.setter
    def id(self, id):
        if isinstance(id, str) and id:
            self._identity = id
        else:
            raise ValueError("ID must be a non-empty string")

    @property
    def base_type(self):
        return self._base_type

    @base_type.setter
    def base_type(self, base_type):
        if isinstance(base_type, str) and base_type:
            self._base_type = base_type
        else:
            raise ValueError("Base type must be a non-empty string")

    @property
    def upgrades_to_unit_id(self):
        return self._upgrades_to_unit_id

    @upgrades_to_unit_id.setter
    def upgrades_to_unit_id(self, upgrades_to_unit_id):
        if isinstance(upgrades_to_unit_id, str):
            self._upgrades_to_unit_id = upgrades_to_unit_id
        else:
            raise ValueError("Upgrades to unit ID must be a string")

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        if isinstance(source, str) and source:
            self._source = source
        else:
            raise ValueError("Source must be a non-empty string")

    @property
    def move_value(self):
        return self._move_value

    @move_value.setter
    def move_value(self, move_value):
        if isinstance(move_value, int) and move_value >= 0:
            self._move_value = move_value
        else:
            raise ValueError("Move value must be a non-negative integer")

    @property
    def capacity_used(self):
        return self._capacity_used

    @capacity_used.setter
    def capacity_used(self, capacity_used):
        if isinstance(capacity_used, float) and capacity_used >= 0:
            self._capacity_used = capacity_used
        else:
            raise ValueError("Capacity used must be a non-negative float")

    @property
    def combat_hits_on(self):
        return self._combat_hits_on

    @combat_hits_on.setter
    def combat_hits_on(self, combat_hits_on):
        if isinstance(combat_hits_on, int) and combat_hits_on >= 0:
            self._combat_hits_on = combat_hits_on
        else:
            raise ValueError("Combat hits on must be a non-negative integer")

    @property
    def combat_die_count(self):
        return self._combat_die_count

    @combat_die_count.setter
    def combat_die_count(self, combat_die_count):
        if isinstance(combat_die_count, int) and combat_die_count >= 0:
            self._combat_die_count = combat_die_count
        else:
            raise ValueError("Combat die count must be a non-negative integer")

    @property
    def is_ship(self):
        return self._is_ship

    @is_ship.setter
    def is_ship(self, is_ship):
        if isinstance(is_ship, bool):
            self._is_ship = is_ship
        else:
            raise ValueError("Is ship must be a boolean")

    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        if isinstance(subtitle, str):
            self._subtitle = subtitle
        else:
            raise ValueError("Subtitle must be a string")

    @property
    def upgrades_from_unit_id(self):
        return self._upgrades_from_unit_id

    @upgrades_from_unit_id.setter
    def upgrades_from_unit_id(self, upgrades_from_unit_id):
        if isinstance(upgrades_from_unit_id, str):
            self._upgrades_from_unit_id = upgrades_from_unit_id
        else:
            raise ValueError("Upgrades from unit ID must be a string")

    @property
    def required_tech_id(self):
        return self._required_tech_id

    @required_tech_id.setter
    def required_tech_id(self, required_tech_id):
        if isinstance(required_tech_id, str):
            self._required_tech_id = required_tech_id
        else:
            raise ValueError("Required tech ID must be a string")

    @property
    def capacity_value(self):
        return self._capacity_value

    @capacity_value.setter
    def capacity_value(self, capacity_value):
        if isinstance(capacity_value, int) and capacity_value >= 0:
            self._capacity_value = capacity_value
        else:
            raise ValueError("Capacity value must be a non-negative integer")

    @property
    def afb_hits_on(self):
        return self._afb_hits_on

    @afb_hits_on.setter
    def afb_hits_on(self, afb_hits_on):
        if isinstance(afb_hits_on, int) and afb_hits_on >= 0:
            self._afb_hits_on = afb_hits_on
        else:
            raise ValueError("AFB hits on must be a non-negative integer")

    @property
    def afb_die_count(self):
        return self._afb_die_count

    @afb_die_count.setter
    def afb_die_count(self, afb_die_count):
        if isinstance(afb_die_count, int) and afb_die_count >= 0:
            self._afb_die_count = afb_die_count
        else:
            raise ValueError("AFB die count must be a non-negative integer")

    @property
    def bombard_hits_on(self):
        return self._bombard_hits_on

    @bombard_hits_on.setter
    def bombard_hits_on(self, bombard_hits_on):
        if isinstance(bombard_hits_on, int) and bombard_hits_on >= 0:
            self._bombard_hits_on = bombard_hits_on
        else:
            raise ValueError("Bombard hits on must be a non-negative integer")

    @property
    def bombard_die_count(self):
        return self._bombard_die_count

    @bombard_die_count.setter
    def bombard_die_count(self, bombard_die_count):
        if isinstance(bombard_die_count, int) and bombard_die_count >= 0:
            self._bombard_die_count = bombard_die_count
        else:
            raise ValueError("Bombard die count must be a non-negative integer")

    @property
    def sustain_damage(self):
        return self._sustain_damage

    @sustain_damage.setter
    def sustain_damage(self, sustain_damage):
        if isinstance(sustain_damage, bool):
            self._sustain_damage = sustain_damage
        else:
            raise ValueError("Sustain damage must be a boolean")

    @property
    def can_be_direct_hit(self):
        return self._can_be_direct_hit

    @can_be_direct_hit.setter
    def can_be_direct_hit(self, can_be_direct_hit):
        if isinstance(can_be_direct_hit, bool):
            self._can_be_direct_hit = can_be_direct_hit
        else:
            raise ValueError("Can be direct hit must be a boolean")

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, ability):
        if isinstance(ability, str):
            self._ability = ability
        else:
            raise ValueError("Ability must be a string")

    @property
    def is_ground_force(self):
        return self._is_ground_force

    @is_ground_force.setter
    def is_ground_force(self, is_ground_force):
        if isinstance(is_ground_force, bool):
            self._is_ground_force = is_ground_force
        else:
            raise ValueError("Is ground force must be a boolean")

    @property
    def space_cannon_hits_on(self):
        return self._space_cannon_hits_on

    @space_cannon_hits_on.setter
    def space_cannon_hits_on(self, space_cannon_hits_on):
        if isinstance(space_cannon_hits_on, int) and space_cannon_hits_on >= 0:
            self._space_cannon_hits_on = space_cannon_hits_on
        else:
            raise ValueError("Space cannon hits on must be a non-negative integer")

    @property
    def space_cannon_die_count(self):
        return self._space_cannon_die_count

    @space_cannon_die_count.setter
    def space_cannon_die_count(self, space_cannon_die_count):
        if isinstance(space_cannon_die_count, int) and space_cannon_die_count >= 0:
            self._space_cannon_die_count = space_cannon_die_count
        else:
            raise ValueError("Space cannon die count must be a non-negative integer")

    @property
    def planetary_shield(self):
        return self._planetary_shield

    @planetary_shield.setter
    def planetary_shield(self, planetary_shield):
        if isinstance(planetary_shield, bool):
            self._planetary_shield = planetary_shield
        else:
            raise ValueError("Planetary shield must be a boolean")

    @property
    def is_structure(self):
        return self._is_structure

    @is_structure.setter
    def is_structure(self, is_structure):
        if isinstance(is_structure, bool):
            self._is_structure = is_structure
        else:
            raise ValueError("Is structure must be a boolean")

    @property
    def deep_space_cannon(self):
        return self._deep_space_cannon

    @deep_space_cannon.setter
    def deep_space_cannon(self, deep_space_cannon):
        if isinstance(deep_space_cannon, bool):
            self._deep_space_cannon = deep_space_cannon
        else:
            raise ValueError("Deep space cannon must be a boolean")

    @property
    def production_value(self):
        return self._production_value

    @production_value.setter
    def production_value(self, production_value):
        if isinstance(production_value, str):
            self._production_value = production_value
        else:
            raise ValueError("Production value must be a string")

    @property
    def basic_production(self):
        return self._basic_production

    @basic_production.setter
    def basic_production(self, basic_production):
        if isinstance(basic_production, str):
            self._basic_production = basic_production
        else:
            raise ValueError("Basic production must be a string")

    @property
    def disables_planetary_shield(self):
        return self._disables_planetary_shield

    @disables_planetary_shield.setter
    def disables_planetary_shield(self, disables_planetary_shield):
        if isinstance(disables_planetary_shield, bool):
            self._disables_planetary_shield = disables_planetary_shield
        else:
            raise ValueError("Disables planetary shield must be a boolean")
