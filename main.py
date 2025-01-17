from src.pokemon import Pokemon
from src.moves import Move


if __name__ == "__main__":
    bulbasaur = Pokemon("bulbasaur")
    flamethrower = Move("Flamethrower", "Fire", 90, 100)
    razor_leaf = Move("Razor Leaf", "Grass", 55, 95)
    tackle = Move("Tackle", "Normal", 50, 100)
    bulbasaur.add_move(flamethrower)
    bulbasaur.add_move(razor_leaf)
    bulbasaur.add_move(tackle)
    print(bulbasaur)
    bulbasaur.delete_move(flamethrower)
    bulbasaur.delete_move("tackle")
    print(bulbasaur)