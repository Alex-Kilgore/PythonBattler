import pytest
from src.battle_pokemon import BattlePokemon

@pytest.fixture
def charizard():
    return BattlePokemon("Charizard", 50)

def test_create_battle_pokemon(charizard):
    assert charizard.level == 50
    assert charizard.current_hp == charizard.stats['hp']
    assert not charizard.is_fainted

def test_stat_calculation(charizard):
    assert charizard.stats['hp'] == 153
    assert charizard.stats['attack'] == 104
    assert charizard.stats['defense'] == 98
    assert charizard.stats['sp_atk'] == 129
    assert charizard.stats['sp_def'] == 105
    assert charizard.stats['speed'] == 120

def test_level_bounds():
    with pytest.raises(ValueError):
        BattlePokemon("Charizard", 0)
    with pytest.raises(ValueError):
        BattlePokemon("Charizard", 101)

def test_set_level(charizard):
    old_hp = charizard.stats['hp']
    charizard.set_level(100)
    assert charizard.level == 100
    assert charizard.stats['hp'] > old_hp

def test_take_damage(charizard):
    initial_hp = charizard.current_hp
    charizard.take_damage(10)
    assert charizard.current_hp == initial_hp - 10
    assert not charizard.is_fainted

def test_faint(charizard):
    charizard.take_damage(charizard.current_hp)  # Take all HP as damage
    assert charizard.current_hp == 0
    assert charizard.is_fainted
    assert not charizard.can_fight()

def test_heal(charizard):
    charizard.take_damage(20)
    initial_hp = charizard.current_hp
    charizard.heal(10)
    assert charizard.current_hp == initial_hp + 10

def test_heal_not_exceed_max(charizard):
    max_hp = charizard.stats['hp']
    charizard.take_damage(10)
    charizard.heal(1000)  # Try to heal by a large amount
    assert charizard.current_hp == max_hp

def test_calculate_all_stats(charizard):
    """Test that calculate_all_stats updates all stats correctly"""
    old_stats = charizard.stats.copy()
    charizard.level = 75  # Manually change level
    charizard.calculate_all_stats()  # Recalculate stats
    assert charizard.stats != old_stats
    assert charizard.stats['hp'] > old_stats['hp']

def test_set_level_no_change(charizard):
    """Test that set_level doesn't recalculate when level doesn't change"""
    old_stats = charizard.stats.copy()
    charizard.set_level(50)  # Same level
    assert charizard.stats == old_stats

def test_set_level_invalid():
    charizard = BattlePokemon("Charizard", 50)
    with pytest.raises(ValueError):
        charizard.set_level(0)
    with pytest.raises(ValueError):
        charizard.set_level(101)

def test_heal_when_fainted(charizard):
    """Test that healing doesn't work when fainted"""
    charizard.take_damage(charizard.current_hp)  # Faint the Pokemon
    initial_hp = charizard.current_hp
    charizard.heal(50)
    assert charizard.current_hp == initial_hp  # HP shouldn't change

def test_calculate_stat_hp(charizard):
    """Test that calculate_stat handles 'hp' correctly"""
    hp = charizard.calculate_stat('hp')
    assert hp == charizard.calculate_hp()

def test_str_representation(charizard):
    """Test both normal and fainted string representations"""
    normal_str = str(charizard)
    assert f"Level: {charizard.level}" in normal_str
    assert "HP:" in normal_str
    
    charizard.take_damage(charizard.current_hp)  # Faint the Pokemon
    fainted_str = str(charizard)
    assert "Fainted" in fainted_str