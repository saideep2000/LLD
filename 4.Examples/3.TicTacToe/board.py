class Board():
    def __init__(self, number):
        self._number = number
        self._boardValues = [[""]*3 for i in range(0,3)]
    
    def make_move(self, mx, my, symbol):
        # come back and see if you need to check if the move is valid or not
        self._boardValues[mx][my] = symbol

    def display_board(self):
        print(f"Tic Tac Toe game : {self._number}")
        print("----------------------------------")
        for i in self._boardValues:
            print(i)
        print("----------------------------------")
        



