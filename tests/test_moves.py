import pytest
from src.moves import Move
from src.types import Type

@pytest.fixture
def basic_move():
    return Move("Tackle", "Normal", 40, 100)

def test_move_creation():
    move = Move("Flamethrower", "Fire", 90, 100)
    assert move.name == "Flamethrower"
    assert move.type == Type.FIRE
    assert move.power == 90
    assert move.accuracy == 100

def test_create_move_with_type_enum():
    move = Move("Flamethrower", Type.FIRE, 90, 100)
    assert move.name == "Flamethrower"
    assert move.type == Type.FIRE
    assert move.power == 90
    assert move.accuracy == 100

def test_set_name(basic_move):
    basic_move.set_name("Hyper Beam")
    assert basic_move.name == "Hyper Beam"

def test_set_type_with_string():
    move = Move("Tackle", Type.NORMAL, 40, 100)
    move.set_type("FIRE")
    assert move.type == Type.FIRE

def test_set_type_with_enum():
    move = Move("Tackle", Type.NORMAL, 40, 100)
    move.set_type(Type.FIRE)
    assert move.type == Type.FIRE

def test_invalid_type_creation():
    with pytest.raises(ValueError):
        Move("Test", "NOT_A_TYPE", 40, 100)

def test_move_str_representation(basic_move):
    expected = "Name: Tackle, Type: NORMAL, Power: 40, Accuracy: 100%"
    assert str(basic_move) == expected

def test_move_equality(basic_move):
    same_move = Move("Tackle", "Normal", 40, 100)
    assert basic_move == same_move

def test_move_inequality(basic_move):
    other_move = Move("Pound", "Normal", 40, 100)
    assert basic_move != other_move

def test_move_compare_to_non_move(basic_move):
    assert basic_move != "Not a move"


def test_invalid_power_type():
    with pytest.raises(TypeError):
        Move("Test", Type.NORMAL, "40", 100)  # power as string
    with pytest.raises(TypeError):
        Move("Test", Type.NORMAL, 40.5, 100)  # power as float

def test_invalid_power_value():
    with pytest.raises(ValueError):
        Move("Test", Type.NORMAL, -1, 100)
    with pytest.raises(ValueError):
        Move("Test", Type.NORMAL, -100, 100)

def test_invalid_accuracy_type():
    with pytest.raises(TypeError):
        Move("Test", Type.NORMAL, 40, "100")  # accuracy as string
    with pytest.raises(TypeError):
        Move("Test", Type.NORMAL, 40, 95.5)   # accuracy as float

def test_invalid_accuracy_value():
    with pytest.raises(ValueError):
        Move("Test", Type.NORMAL, 40, -1)    # below 0
    with pytest.raises(ValueError):
        Move("Test", Type.NORMAL, 40, 101)   # above 100

def test_set_power(basic_move):
    basic_move.set_power(100)
    assert basic_move.power == 100

def test_set_invalid_power():
    move = Move("Tackle", Type.NORMAL, 40, 100)
    with pytest.raises(TypeError):
        move.set_power("50")
    with pytest.raises(ValueError):
        move.set_power(-10)

def test_set_accuracy(basic_move):
    basic_move.set_accuracy(50)
    assert basic_move.accuracy == 50

def test_set_invalid_accuracy():
    move = Move("Tackle", Type.NORMAL, 40, 100)
    with pytest.raises(TypeError):
        move.set_accuracy("95")
    with pytest.raises(ValueError):
        move.set_accuracy(101)
    with pytest.raises(ValueError):
        move.set_accuracy(-1)