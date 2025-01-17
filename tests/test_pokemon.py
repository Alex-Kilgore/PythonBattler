import pytest
from src.pokemon import Pokemon
from src.moves import Move

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
    assert "fire" in [t.lower() for t in charizard.types]
    assert "flying" in [t.lower() for t in charizard.types]

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

def test_delete_nonexistent_move(charizard):
    # Try to delete a move that doesn't exist
    charizard.delete_move("nonexistent")
    assert len(charizard.moves) == 0

    