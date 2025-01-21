class Move:
    def __init__(self, name: str, type: str, power: int, accuracy: int):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy

    def set_name(self, name: str):
        self.name = name
    def set_type(self, type: str):
        self.type = type
    def set_power(self, power: int):
        self.power = power
    def set_accuracy(self, accuracy: int):
        self.accuracy = accuracy
    
    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Power: {self.power}, Accuracy: {self.accuracy}%"
    
    def __eq__(self, other):
        if not isinstance(other, Move):
            return False
        return (self.name == other.name and 
                self.type == other.type and 
                self.power == other.power and 
                self.accuracy == other.accuracy)