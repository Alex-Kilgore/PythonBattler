import pypokedex as pokedex
from src.moves import Move

class Pokemon:
    def __init__(self, name: str):
        p = pokedex.get(name=name)
        self.name = p.name
        self.dex = p.dex
        self.types = p.types
        self.base_stats = p.base_stats
        self.moves = []
    
    def add_move(self, move: Move):
        if len(self.moves) == 4:
            print(f"{self.name} already knows four moves")
        elif move not in self.moves:
            self.moves.append(move)
        else:
            print(f"{self.name} already knows {move.name}")
    
    def delete_move(self, move):
        if isinstance(move, str):
            for m in self.moves:
                if m.name.lower() == move.lower():
                    self.moves.remove(m)
                    return
            print(f"{self.name} doesn't know {move}")
        elif isinstance(move, Move):
            if move in self.moves:
                self.moves.remove(move)
            else:
                print(f"{self.name} doesn't know {move.name}")
        
                
    def __str__(self):
        return ("-----------------------------------------------------------------------\n"
                f"#{self.dex} {self.name} - {self.types}\n"
                f"{self.base_stats}\n"
                f"{[m.name for m in self.moves]}\n"
                "-----------------------------------------------------------------------")
    
    def __eq__(self, other):
        if not isinstance(other, Pokemon):
            return False
        return (self.name == other.name and
                self.dex == other.dex and
                self.types == other.types and
                self.base_stats == other.base_stats and
                self.moves == other.moves)
    