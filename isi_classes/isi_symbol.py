from abc import ABC
from abc import abstractmethod

class Isi_Symbol(ABC):
    def __init__(self, id):
        self.id = id

    def getIdentifier(self):
        return self.id
    
    def setIdentifier(self, id):
        self.id = id

    def __str__(self) -> str:
        return f"Isi Symbol ID: {self.id}"
    
    @abstractmethod
    def java_generator_code(self):
        return