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
        
    @classmethod
    def get_effectiveness(cls, attacking_type: 'Type', defending_type: 'Type') -> float:
        """
        Get the effectiveness multiplier when attacking_type moves are used against defending_type.
        Returns:
        - 2.0 for super effective
        - 1.0 for normal effectiveness
        - 0.5 for not very effective
        - 0.0 for no effect
        """
        try:
            return cls.TYPE_CHART[attacking_type][defending_type]
        except KeyError:
            return 1.0  # default to normal effectiveness
        
    def __str__(self):
        return self.name
    



Type.TYPE_CHART = {
    Type.NORMAL: {
        Type.ROCK: 0.5,
        Type.STEEL: 0.5,
        Type.GHOST: 0.0,
    },
    Type.FIRE: {
        Type.GRASS: 2.0,
        Type.ICE: 2.0,
        Type.BUG: 2.0,
        Type.STEEL: 2.0,
        Type.FIRE: 0.5,
        Type.WATER: 0.5,
        Type.ROCK: 0.5,
        Type.DRAGON: 0.5,
    },
    Type.WATER: {
        Type.FIRE: 2.0,
        Type.GROUND: 2.0,
        Type.ROCK: 2.0,
        Type.WATER: 0.5,
        Type.GRASS: 0.5,
        Type.DRAGON: 0.5,
    },
    Type.ELECTRIC: {
        Type.WATER: 2.0,
        Type.FLYING: 2.0,
        Type.GROUND: 0.0,
        Type.GRASS: 0.5,
        Type.ELECTRIC: 0.5,
        Type.DRAGON: 0.5,
    },
    Type.GRASS: {
        Type.WATER: 2.0,
        Type.GROUND: 2.0,
        Type.ROCK: 2.0,
        Type.FIRE: 0.5,
        Type.GRASS: 0.5,
        Type.POISON: 0.5,
        Type.FLYING: 0.5,
        Type.BUG: 0.5,
        Type.DRAGON: 0.5,
        Type.STEEL: 0.5,
    },
    Type.ICE: {
        Type.GRASS: 2.0,
        Type.GROUND: 2.0,
        Type.FLYING: 2.0,
        Type.DRAGON: 2.0,
        Type.FIRE: 0.5,
        Type.WATER: 0.5,
        Type.ICE: 0.5,
        Type.STEEL: 0.5,
    },
    Type.FIGHTING: {
        Type.NORMAL: 2.0,
        Type.ICE: 2.0,
        Type.ROCK: 2.0,
        Type.DARK: 2.0,
        Type.STEEL: 2.0,
        Type.POISON: 0.5,
        Type.FLYING: 0.5,
        Type.PSYCHIC: 0.5,
        Type.BUG: 0.5,
        Type.FAIRY: 0.5,
        Type.GHOST: 0.0,
    },
    Type.POISON: {
        Type.GRASS: 2.0,
        Type.FAIRY: 2.0,
        Type.POISON: 0.5,
        Type.GROUND: 0.5,
        Type.ROCK: 0.5,
        Type.GHOST: 0.5,
        Type.STEEL: 0.0,
    },
    Type.GROUND: {
        Type.FIRE: 2.0,
        Type.ELECTRIC: 2.0,
        Type.POISON: 2.0,
        Type.ROCK: 2.0,
        Type.STEEL: 2.0,
        Type.GRASS: 0.5,
        Type.BUG: 0.5,
        Type.FLYING: 0.0,
    },
    Type.FLYING: {
        Type.GRASS: 2.0,
        Type.FIGHTING: 2.0,
        Type.BUG: 2.0,
        Type.ELECTRIC: 0.5,
        Type.ROCK: 0.5,
        Type.STEEL: 0.5,
    },
    Type.PSYCHIC: {
        Type.FIGHTING: 2.0,
        Type.POISON: 2.0,
        Type.PSYCHIC: 0.5,
        Type.STEEL: 0.5,
        Type.DARK: 0.0,
    },
    Type.BUG: {
        Type.GRASS: 2.0,
        Type.PSYCHIC: 2.0,
        Type.DARK: 2.0,
        Type.FIRE: 0.5,
        Type.FIGHTING: 0.5,
        Type.POISON: 0.5,
        Type.FLYING: 0.5,
        Type.GHOST: 0.5,
        Type.STEEL: 0.5,
        Type.FAIRY: 0.5,
    },
    Type.ROCK: {
        Type.FIRE: 2.0,
        Type.ICE: 2.0,
        Type.FLYING: 2.0,
        Type.BUG: 2.0,
        Type.FIGHTING: 0.5,
        Type.GROUND: 0.5,
        Type.STEEL: 0.5,
    },
    Type.GHOST: {
        Type.PSYCHIC: 2.0,
        Type.GHOST: 2.0,
        Type.DARK: 0.5,
        Type.NORMAL: 0.0,
    },
    Type.DRAGON: {
        Type.DRAGON: 2.0,
        Type.STEEL: 0.5,
        Type.FAIRY: 0.0,
    },
    Type.DARK: {
        Type.PSYCHIC: 2.0,
        Type.GHOST: 2.0,
        Type.FIGHTING: 0.5,
        Type.DARK: 0.5,
        Type.FAIRY: 0.5,
    },
    Type.STEEL: {
        Type.ICE: 2.0,
        Type.ROCK: 2.0,
        Type.FAIRY: 2.0,
        Type.FIRE: 0.5,
        Type.WATER: 0.5,
        Type.ELECTRIC: 0.5,
        Type.STEEL: 0.5,
    },
    Type.FAIRY: {
        Type.FIGHTING: 2.0,
        Type.DRAGON: 2.0,
        Type.DARK: 2.0,
        Type.FIRE: 0.5,
        Type.POISON: 0.5,
        Type.STEEL: 0.5,
    },
}