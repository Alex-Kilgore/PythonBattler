import pytest
from src.pokemon import Pokemon
from src.moves import Move
from src.types import Type

@pytest.fixture
def charizard():
    return Pokemon("Charizard")

@pytest.fixture
def flamethrower():
    return Move("Flamethrower", "Fire", 90, 100)

@pytest.fixture
def four_moves():
    flamethrower = Move("Flamethrower", "Fire", 90, 100)
    surf = Move("Surf", "Water", 90, 100)
    leaf_blade = Move("Leaf Blade", "Grass", 90, 100)
    thunderbolt = Move("Thunderbolt", "Electric", 95, 100)
    return [flamethrower, surf, leaf_blade, thunderbolt]

def test_create_pokemon(charizard):
    assert charizard.dex == 6
    assert charizard.name.lower() == "charizard"
    assert Type.FIRE in charizard.types
    assert Type.FLYING in charizard.types

def test_pokemon_equality(charizard):
    same_pokemon = Pokemon("Charizard")
    assert charizard == same_pokemon

def test_pokemon_inequality(charizard):
    other_pokemon = Pokemon("Pikachu")
    assert charizard != other_pokemon

def test_pokemon_equality_not_pokemon(charizard):
    assert charizard != "not a pokemon"

def test_add_move(charizard, flamethrower):
    charizard.add_move(flamethrower)
    assert flamethrower in charizard.moves
    assert len(charizard.moves) == 1

def test_add_duplicate_move(charizard, flamethrower):
    charizard.add_move(flamethrower)
    charizard.add_move(flamethrower)
    assert len(charizard.moves) == 1
    assert charizard.moves.count(flamethrower) == 1

def test_add_four_moves(charizard, four_moves):
    for move in four_moves:
        charizard.add_move(move)
    assert charizard.moves == four_moves
    assert len(charizard.moves) == 4

def test_pokemon_string_representation(charizard, four_moves):
    for move in four_moves:
        charizard.add_move(move)
    pokemon_str = str(charizard)
    assert str(charizard.dex) in pokemon_str
    assert charizard.name in pokemon_str
    assert str(charizard.base_stats) in pokemon_str
    assert all(move.name in pokemon_str for move in charizard.moves)

def test_exceed_move_limit(charizard, four_moves):
    # Add four moves
    for move in four_moves:
        charizard.add_move(move)
    # Try to add a fifth move
    extra_move = Move("Dragon Claw", "Dragon", 80, 100)
    charizard.add_move(extra_move)
    assert len(charizard.moves) == 4
    assert extra_move not in charizard.moves

def test_delete_move_by_instance(charizard, four_moves):
    for move in four_moves:
        charizard.add_move(move)
    charizard.delete_move(four_moves[0])
    assert charizard.moves == [four_moves[1], four_moves[2], four_moves[3]]
    assert len(charizard.moves) == 3

def test_delete_move_by_name(charizard, four_moves):
    for move in four_moves:
        charizard.add_move(move)
    charizard.delete_move("flamethrower")
    assert charizard.moves == [four_moves[1], four_moves[2], four_moves[3]]
    assert len(charizard.moves) == 3

def test_delete_nonexistent_move_by_name(charizard):
    # Try to delete a move that doesn't exist
    charizard.delete_move("nonexistent")
    assert len(charizard.moves) == 0

def test_delete_nonexistent_move_by_instance(charizard, flamethrower):
    """Test deleting a move by instance that Pokemon doesn't know"""
    charizard.delete_move(flamethrower)
    assert len(charizard.moves) == 0