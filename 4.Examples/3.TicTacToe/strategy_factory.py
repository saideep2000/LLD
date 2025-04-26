# Version 2: Adding Strategy Pattern for validation, win and draw conditions

from abc import ABC, abstractmethod
from typing import List, Optional


# Strategy Pattern
class MoveValidationStrategy(ABC):
    @abstractmethod
    def validate_move(self, board: List[Optional[str]], position: int) -> bool:
        pass


class DefaultMoveValidationStrategy(MoveValidationStrategy):
    def validate_move(self, board: List[Optional[str]], position: int) -> bool:
        return 0 <= position < 9 and board[position] is None


class WinConditionStrategy(ABC):
    @abstractmethod
    def check_win(self, board: List[Optional[str]], symbol: str) -> bool:
        pass


class DefaultWinConditionStrategy(WinConditionStrategy):
    def check_win(self, board: List[Optional[str]], symbol: str) -> bool:
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for pattern in win_patterns:
            a, b, c = pattern
            if (board[a] == symbol and 
                board[b] == symbol and 
                board[c] == symbol):
                return True
        return False


class DrawConditionStrategy(ABC):
    @abstractmethod
    def check_draw(self, board: List[Optional[str]]) -> bool:
        pass


class DefaultDrawConditionStrategy(DrawConditionStrategy):
    def check_draw(self, board: List[Optional[str]]) -> bool:
        return all(cell is not None for cell in board)


# Factory Pattern
class PlayerFactory:
    @staticmethod
    def create_player(symbol: str) -> 'Player':
        return Player(symbol)


class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol


class Board:
    def __init__(self):
        import time
        self.id = int(time.time())
        self.cells = [None] * 9
    
    def display(self) -> None:
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("\n-----------")
            elif i != 0:
                print(" | ", end="")
            print(" " if self.cells[i] is None else self.cells[i], end="")
        print("\n")
    
    def reset(self) -> None:
        self.cells = [None] * 9
    
    def update(self, position: int, symbol: str) -> None:
        self.cells[position] = symbol


class Game:
    def __init__(self, 
                 move_validator: MoveValidationStrategy = DefaultMoveValidationStrategy(),
                 win_checker: WinConditionStrategy = DefaultWinConditionStrategy(),
                 draw_checker: DrawConditionStrategy = DefaultDrawConditionStrategy()):
        self.board = Board()
        self.player_factory = PlayerFactory()
        self.player1 = self.player_factory.create_player('X')
        self.player2 = self.player_factory.create_player('O')
        self.current_player = self.player1
        self.game_over = False
        self.winner = None
        
        # Strategy pattern implementations
        self.move_validator = move_validator
        self.win_checker = win_checker
        self.draw_checker = draw_checker
    
    def switch_player(self) -> None:
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
    
    def make_move(self, position: int) -> bool:
        # Check if move is valid using strategy
        if self.game_over or not self.move_validator.validate_move(self.board.cells, position):
            return False
        
        # Update board
        self.board.update(position, self.current_player.symbol)
        
        # Check win condition using strategy
        if self.win_checker.check_win(self.board.cells, self.current_player.symbol):
            self.game_over = True
            self.winner = self.current_player
            return True
        
        # Check draw condition using strategy
        if self.draw_checker.check_draw(self.board.cells):
            self.game_over = True
            return True
        
        # Switch player
        self.switch_player()
        return True
    
    def get_game_status(self) -> str:
        if self.winner:
            return f"Player {self.winner.symbol} wins!"
        if self.game_over:
            return "It's a draw!"
        return f"Player {self.current_player.symbol}'s turn"
    
    def reset_game(self) -> None:
        self.board.reset()
        self.current_player = self.player1
        self.game_over = False
        self.winner = None


# Singleton Pattern
class TicTacToe:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TicTacToe, cls).__new__(cls)
            cls._instance.game = Game()
        return cls._instance
    
    def new_game(self) -> str:
        """Initialize a new game"""
        self.game.reset_game()
        return "New game started! Player X goes first."
    
    def play(self, position: int) -> str:
        """Make a move and return the game status"""
        if not self.game.make_move(position):
            return "Invalid move. Try again."
        
        # Display the board
        self.game.board.display()
        
        return self.game.get_game_status()


# Example usage with a custom win condition strategy
class DiagonalOnlyWinStrategy(WinConditionStrategy):
    def check_win(self, board: List[Optional[str]], symbol: str) -> bool:
        # Only diagonal wins are allowed in this variant
        diagonal_patterns = [
            [0, 4, 8],  # Main diagonal
            [2, 4, 6]   # Anti-diagonal
        ]
        
        for pattern in diagonal_patterns:
            a, b, c = pattern
            if (board[a] == symbol and 
                board[b] == symbol and 
                board[c] == symbol):
                return True
        return False


if __name__ == "__main__":
    # Normal game
    tic_tac_toe = TicTacToe()
    print(tic_tac_toe.new_game())
    
    # Uncomment to use a custom win strategy (diagonal wins only)
    # tic_tac_toe.game = Game(win_checker=DiagonalOnlyWinStrategy())
    # print(tic_tac_toe.new_game())
    
    # Main game loop
    while not tic_tac_toe.game.game_over:
        try:
            position = int(input(f"Player {tic_tac_toe.game.current_player.symbol}, choose a position (0-8): "))
            result = tic_tac_toe.play(position)
            print(result)
        except ValueError:
            print("Please enter a number between 0 and 8.")
    
    print("Game over!")