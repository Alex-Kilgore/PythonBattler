import pytest
from src.moves import Move

@pytest.fixture
def basic_move():
    return Move("Tackle", "Normal", 40, 100)

def test_move_creation():
    move = Move("Flamethrower", "Fire", 90, 100)
    assert move.name == "Flamethrower"
    assert move.type == "Fire"
    assert move.power == 90
    assert move.accuracy == 100

def test_move_str_representation(basic_move):
    expected = "Name: Tackle, Type: Normal, Power: 40, Accuracy: 100%"
    assert str(basic_move) == expected

def test_move_equality(basic_move):
    same_move = Move("Tackle", "Normal", 40, 100)
    assert basic_move == same_move

def test_move_inequality(basic_move):
    other_move = Move("Pound", "Normal", 40, 100)
    assert basic_move != other_move

