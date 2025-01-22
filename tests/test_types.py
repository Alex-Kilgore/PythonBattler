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