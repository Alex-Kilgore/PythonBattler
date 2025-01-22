from src.types import Type

class Move:
    def __init__(self, name: str, type: Type | str, power: int, accuracy: int):
        self.name = name
        self.type = type if isinstance(type, Type) else Type.from_string(type)
         # Validate power
        if not isinstance(power, int):
            raise TypeError("Power must be an integer")
        if power < 0:
            raise ValueError("Power cannot be negative")
        self.power = power
        # Validate accuracy
        if not isinstance(accuracy, int):
            raise TypeError("Accuracy must be an integer")
        if not 0 <= accuracy <= 100:
            raise ValueError("Accuracy must be between 0 and 100")
        self.accuracy = accuracy

        
    def set_name(self, name: str):
        self.name = name
    
    def set_type(self, type: Type | str):
        self.type = type if isinstance(type, Type) else Type.from_string(type)
    
    def set_power(self, power: int):
        if not isinstance(power, int):
            raise TypeError("Power must be an integer")
        if power < 0:
            raise ValueError("Power cannot be negative")
        self.power = power

    def set_accuracy(self, accuracy: int):
        if not isinstance(accuracy, int):
            raise TypeError("Accuracy must be an integer")
        if not 0 <= accuracy <= 100:
            raise ValueError("Accuracy must be between 0 and 100")
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