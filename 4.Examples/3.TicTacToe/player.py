class Player():
    def __init__(self, name):
        self._name = name
        self._symbol = None
    
    # getter for name
    def get_name(self):
        return self._name
    
    def get_symbol(self):
        return self._symbol

    # setter
    def set_symbol(self, symbol):
        self._symbol = symbol
    
