from enum import Enum

class Type(Enum):
    NORMAL = 1
    FIRE = 2
    WATER = 3
    ELECTRIC = 4
    GRASS = 5
    ICE = 6
    FIGHTING = 7
    POISON = 8
    GROUND = 9
    FLYING = 10
    PSYCHIC = 11
    BUG = 12
    ROCK = 13
    GHOST = 14
    DRAGON = 15
    DARK = 16
    STEEL = 17
    FAIRY = 18

    @classmethod
    def from_string(cls, type_string: str):
        try:
            return cls[type_string.upper()]
        except KeyError:
            raise ValueError(f"Invalid type: {type_string}")
        
    def __str__(self):
        return self.name