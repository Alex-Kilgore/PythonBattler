import pypokedex as pokedex

class Pokemon:
    def __init__(self, name):
        p = pokedex.get(name=name)
        self.name = p.name
        self.dex = p.dex
        self.types = p.types
        self.base_stats = p.base_stats
        self.moves = ["move1", "move2", "move3", "move4"]
    
    def __str__(self):
        return f"#{self.dex} {self.name} -- {self.types}\n{self.base_stats}\n{self.moves}"