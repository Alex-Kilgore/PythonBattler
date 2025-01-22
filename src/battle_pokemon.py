from src.pokemon import Pokemon

class BattlePokemon(Pokemon):
    def __init__(self, name: str, level: int):
        super().__init__(name)
        if level < 1 or level > 100:
            raise ValueError("Level must be between 1 and 100")
        self.level = level
        
        # Calculate actual stats from base stats
        self.stats = {
            'hp': self.calculate_hp(),
            'attack': self.calculate_stat('attack'),
            'defense': self.calculate_stat('defense'),
            'sp_atk': self.calculate_stat('sp_atk'),
            'sp_def': self.calculate_stat('sp_def'),
            'speed': self.calculate_stat('speed')
        }
        self.current_hp = self.stats['hp']
        self.is_fainted = False

    # Assuming 31 IV, 0 EV and neutral nature
    # TODO: Implement IV, EV, nature logic
    def calculate_hp(self) -> int:
        return ((2 * self.base_stats.hp + 31 + 0) * self.level) // 100 + self.level + 10

    def calculate_stat(self, stat_name: str) -> int:
        if stat_name == 'hp':
            return self.calculate_hp()
        base = getattr(self.base_stats, stat_name)
        return ((2 * base + 31 + 0) * self.level) // 100 + 5

    def calculate_all_stats(self):
        self.stats = {
            'hp': self.calculate_hp(),
            'attack': self.calculate_stat('attack'),
            'defense': self.calculate_stat('defense'),
            'sp_atk': self.calculate_stat('sp_atk'),
            'sp_def': self.calculate_stat('sp_def'),
            'speed': self.calculate_stat('speed')
        }

    def set_level(self, l: int):
        if l < 1 or l > 100:
            raise ValueError("Level must be between 1 and 100")
        elif self.level != l:
            self.level = l
            self.calculate_all_stats()
    
    def take_damage(self, amount: int):
        self.current_hp = max(0, self.current_hp - amount)
        if self.current_hp == 0:
            self.is_fainted = True
            
    def heal(self, amount: int):
        if not self.is_fainted:
            self.current_hp = min(self.stats['hp'], self.current_hp + amount)
            
    def can_fight(self) -> bool:
        return not self.is_fainted
        
    def __str__(self):
        status = "Fainted" if self.is_fainted else f"HP: {self.current_hp}/{self.stats['hp']}"
        return ("-----------------------------------------------------------------------\n"
                f"#{self.dex} {self.name} - {[type.name for type in self.types]}\n"
                f"Level: {self.level}\n"
                f"{status}\n"
                f"Stats: {self.stats}\n"
                f"Moves: {[m.name for m in self.moves]}\n"
                "-----------------------------------------------------------------------")