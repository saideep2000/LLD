from typing import List


class Game():
    _instance = None
    def __init__(self):
        if Game._instance is not None:
            raise Exception("This is a singleton pattern !!")
        else:
            Game._instance = self
            self._games = {}
            
    
    @staticmethod
    def get_instance(self):
        if self._instance == None:
            Game()
        return self._instance
    
    