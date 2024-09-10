from typing import Dict
from isi_symbol import Isi_Symbol

class Isi_Symbol_Table():
    def __init__(self) -> None:
        self.symbol_table: Dict[str, Isi_Symbol] = {}

    def add(self, symbol):
        self.symbol_table[symbol.getIdentifier()] = symbol

    def exists(self, symbol: str):
        return symbol in self.symbol_table
    
    def get(self, symbol: str) -> Isi_Symbol:
        return self.symbol_table.get(symbol)
    
    def get_all(self):
        return self.symbol_table.values()