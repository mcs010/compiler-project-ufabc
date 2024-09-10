from isi_symbol import Isi_Symbol

class Isi_Variable(Isi_Symbol):
    Number = 0
    Text = 1
    Bool = 2

    def __init__(self, id, type, value):
        super().__init__(id)
        self.type = type
        self.value = value

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Isi Variable name:{self.id} | type:{self.type} | value={self.value}]"
    
    def java_generator_code(self):
        if self.type == Isi_Variable.Number:
            return f"double {self.id}"
        
        elif self.type == Isi_Variable.Text:
            return f"str {self.id}"
        
        else:
            return f"bool {self.id}"
        
    