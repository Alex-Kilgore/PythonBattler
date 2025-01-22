import pytest
from src.types import Type

def test_valid_type_strings():
    assert Type.from_string("FIRE") == Type.FIRE
    assert Type.from_string("fire") == Type.FIRE
    assert Type.from_string("Fire") == Type.FIRE
    assert Type.from_string("fIRe") == Type.FIRE

def test_invalid_type_strings():
    with pytest.raises(ValueError):
        Type.from_string("not a type")
    with pytest.raises(ValueError):
        Type.from_string("")

def test_type_string_representation():
    assert str(Type.FIRE) == "FIRE"
    assert str(Type.WATER) == "WATER"

def test_type_values():
    assert Type.FIRE.value == 2
    assert Type.WATER.value == 3

def test_type_comparison():
    assert Type.FIRE != Type.WATER
    assert Type.FIRE == Type.FIRE

def test_super_effective():
    assert Type.get_effectiveness(Type.WATER, Type.FIRE) == 2.0
    assert Type.get_effectiveness(Type.GROUND, Type.ELECTRIC) == 2.0
    assert Type.get_effectiveness(Type.FIGHTING, Type.NORMAL) == 2.0

def test_not_very_effective():
    assert Type.get_effectiveness(Type.FIRE, Type.WATER) == 0.5
    assert Type.get_effectiveness(Type.GRASS, Type.FIRE) == 0.5
    assert Type.get_effectiveness(Type.NORMAL, Type.ROCK) == 0.5

def test_no_effect():
    assert Type.get_effectiveness(Type.NORMAL, Type.GHOST) == 0.0
    assert Type.get_effectiveness(Type.ELECTRIC, Type.GROUND) == 0.0
    assert Type.get_effectiveness(Type.FIGHTING, Type.GHOST) == 0.0

def test_normal_effectiveness():
    assert Type.get_effectiveness(Type.FIRE, Type.PSYCHIC) == 1.0
    assert Type.get_effectiveness(Type.WATER, Type.FAIRY) == 1.0
    assert Type.get_effectiveness(Type.NORMAL, Type.GRASS) == 1.0