"""
Features Required:
Board Initialization: A board with a predefined size.

Players: Multiple players can play the game.

Snakes and Ladders: Random placement of snakes and ladders.

Dice Roll: A player can roll a dice and move accordingly.

Game Logic: Movement according to dice roll and handling snakes and ladders.

Design Patterns Involved:
Singleton Pattern: Used for creating a single instance of the board to ensure that all players interact with the same board.

Factory Pattern: Used to create snakes and ladders on the board.

Observer Pattern: Used to notify players about their turns.

Strategy Pattern: Used to define the dice rolling strategy, which can be changed dynamically.

Command Pattern: Used to encapsulate a request as an object to parameterize clients with queues, requests, and operations.



"""


from abc import ABC, abstractmethod
import random
from typing import List, Dict, Optional

"""
Observer pattern: For notifying players, saving game history, etc.
"""

# abstract_observer.py
class AbstractObserver(ABC):
    @abstractmethod
    def update(self, subject, *args, **kwargs):
        pass

# subject.py
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

# notify_player_observer.py
class NotifyPlayerObserver(AbstractObserver):
    def __init__(self):
        self.notify = Notification()
    
    def important_update(self, state) -> str:
        if state["game_over"]:
            return f"Game is over! {state['winner']} has won the game!"
        elif state["snake_encounter"]:
            return f"{state['current_player']} encountered a snake and moved from {state['from_position']} to {state['to_position']}"
        elif state["ladder_encounter"]:
            return f"{state['current_player']} found a ladder and moved from {state['from_position']} to {state['to_position']}"
        elif state["turn_change"]:
            return f"It's {state['current_player']}'s turn now"
        return None
    
    def update(self, subject, players=None, state=None):
        message = self.important_update(state)
        if message is not None:
            for player in players:
                self.notify.send(player.name, message)

# save_history_observer.py
class SaveHistoryObserver(AbstractObserver):
    def __init__(self, filename="game_history.txt"):
        self.filename = filename
        self.history = []
    
    def update(self, subject, players=None, state=None):
        self.history.append(state.copy())
        # Save to file
        with open(self.filename, "a") as file:
            file.write(f"{state}\n")

# notification.py
class Notification:
    def send(self, user_id, message):
        print(f"Hello {user_id}, {message}")

"""
Strategy pattern: For different dice strategies at runtime
"""

# abstract_strategy.py
class AbstractStrategy(ABC):
    @abstractmethod
    def roll(self):
        pass

# default_dice_strategy.py
class DefaultDiceStrategy(AbstractStrategy):
    def roll(self):
        return random.randint(1, 6)

# loaded_dice_strategy.py
class LoadedDiceStrategy(AbstractStrategy):
    def __init__(self, favored_player_name, favor_chance=0.7):
        self.favored_player = favored_player_name
        self.favor_chance = favor_chance
    
    def roll(self, current_player=None):
        if current_player == self.favored_player and random.random() < self.favor_chance:
            # Higher chance of rolling a 6
            return random.randint(4, 6)
        else:
            return random.randint(1, 6)

"""
Factory pattern: For creating different entities
"""

# factory_player.py
class PlayerFactory:
    @staticmethod
    def create_player(name, player_type="human"):
        if player_type.lower() == "human":
            return HumanPlayer(name)
        elif player_type.lower() == "computer":
            return ComputerPlayer(name)
        else:
            raise ValueError(f"Unknown player type: {player_type}")

# player.py
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
    
    def move(self, steps):
        self.position += steps
    
    def set_position(self, position):
        self.position = position

# human_player.py
class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.type = "human"
    
    def take_turn(self, dice_strategy):
        input(f"{self.name}, press Enter to roll the dice...")
        return dice_strategy.roll()

# computer_player.py
class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.type = "computer"
    
    def take_turn(self, dice_strategy):
        print(f"{self.name} (Computer) is rolling the dice...")
        return dice_strategy.roll()

"""
Factory pattern: For creating snakes and ladders
"""

# snake_factory.py
class SnakeFactory:
    @staticmethod
    def create_snakes(board_size, num_snakes):
        snakes = {}
        positions = set()
        
        while len(snakes) < num_snakes:
            # Snake head cannot be on the last position or first position
            head = random.randint(board_size // 4, board_size - 1)
            # Snake tail must be before the head
            tail = random.randint(1, head - 1)
            
            # Check if position is already occupied
            if head not in positions:
                snakes[head] = tail
                positions.add(head)
                positions.add(tail)
        
        return snakes

# ladder_factory.py
class LadderFactory:
    @staticmethod
    def create_ladders(board_size, num_ladders, snake_positions):
        ladders = {}
        positions = set(snake_positions)
        
        while len(ladders) < num_ladders:
            # Ladder start cannot be on the first or last position
            start = random.randint(1, board_size - board_size // 4)
            # Ladder end must be after the start
            end = random.randint(start + 1, board_size - 1)
            
            # Check if position is already occupied
            if start not in positions and end not in positions:
                ladders[start] = end
                positions.add(start)
                positions.add(end)
        
        return ladders

"""
Board: Will create and manage the game board
"""

# board.py
class Board:
    def __init__(self, size=100, num_snakes=10, num_ladders=10):
        self.size = size
        
        # Create snakes and ladders
        self.snakes = SnakeFactory.create_snakes(size, num_snakes)
        self.ladders = LadderFactory.create_ladders(size, num_ladders, list(self.snakes.keys()) + list(self.snakes.values()))
    
    def get_final_position(self, position):
        # Check if position has a snake
        if position in self.snakes:
            return self.snakes[position], "snake"
        
        # Check if position has a ladder
        if position in self.ladders:
            return self.ladders[position], "ladder"
        
        return position, None
    
    def is_winning_position(self, position):
        return position >= self.size
    
    def display_board(self):
        # Create a visual representation of the board
        width = int(self.size ** 0.5)  # Assuming a square board
        if width * width < self.size:
            width += 1
        
        print(f"\n{'=' * 40}")
        print(f"Board (Size: {self.size}, Snakes: {len(self.snakes)}, Ladders: {len(self.ladders)})")
        print(f"{'=' * 40}\n")
        
        print("Snakes:")
        for head, tail in self.snakes.items():
            print(f"  {head} -> {tail}")
        
        print("\nLadders:")
        for start, end in self.ladders.items():
            print(f"  {start} -> {end}")
        print(f"\n{'=' * 40}\n")

"""
TurnManager: Manages player turns
"""

# turn_manager.py
class TurnManager(Subject):
    def __init__(self, players):
        super().__init__()
        self.players = players
        self.current_player_index = 0
    
    def get_current_player(self):
        return self.players[self.current_player_index]
    
    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        current_player = self.get_current_player()
        
        state = {
            "turn_change": True,
            "current_player": current_player.name,
            "game_over": False,
            "snake_encounter": False,
            "ladder_encounter": False
        }
        
        self.notify(players=self.players, state=state)
        return current_player

"""
Command Pattern: Encapsulate player moves
"""

# abstract_command.py
class AbstractCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

# move_command.py
class MoveCommand(AbstractCommand):
    def __init__(self, player, dice_result, board):
        self.player = player
        self.dice_result = dice_result
        self.board = board
        self.old_position = player.position
        self.new_position = None
        self.encounter_type = None
    
    def execute(self):
        # Calculate new position
        potential_position = self.player.position + self.dice_result
        
        # Check if the move is valid
        if potential_position > self.board.size:
            # Can't go beyond the board
            return {
                "moved": False,
                "old_position": self.old_position,
                "new_position": self.old_position,
                "encounter_type": None,
                "game_over": False
            }
        
        # Move player to the potential position first
        self.player.set_position(potential_position)
        
        # Check for snakes or ladders
        final_position, encounter_type = self.board.get_final_position(potential_position)
        self.encounter_type = encounter_type
        
        # Set player to the final position
        self.player.set_position(final_position)
        self.new_position = final_position
        
        # Check if player won
        game_over = self.board.is_winning_position(final_position)
        
        return {
            "moved": True,
            "old_position": self.old_position,
            "new_position": final_position,
            "encounter_type": encounter_type,
            "game_over": game_over
        }
    
    def undo(self):
        if self.new_position is not None:
            self.player.set_position(self.old_position)
            return True
        return False

"""
Singleton + Facade Pattern: Main game controller
"""

# snake_and_ladder.py
class SnakeAndLadder:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SnakeAndLadder, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, board_size=100, num_snakes=10, num_ladders=10):
        if self._initialized:
            return
        
        self.board = Board(board_size, num_snakes, num_ladders)
        self.players = []
        self.dice_strategy = DefaultDiceStrategy()
        self.move_history = []
        self.game_over = False
        self.winner = None
        
        # Set up observers
        self.turn_manager = TurnManager([])
        self.player_notifier = NotifyPlayerObserver()
        self.history_saver = SaveHistoryObserver()
        self.turn_manager.attach(self.player_notifier)
        self.turn_manager.attach(self.history_saver)
        
        self._initialized = True
    
    def add_player(self, name, player_type="human"):
        player = PlayerFactory.create_player(name, player_type)
        self.players.append(player)
        self.turn_manager.players = self.players
        return player
    
    def set_dice_strategy(self, strategy):
        self.dice_strategy = strategy
    
    def start_game(self):
        if len(self.players) < 2:
            raise ValueError("At least 2 players are required to start the game")
        
        self.board.display_board()
        self.game_over = False
        self.winner = None
        
        print("\nGame started!")
        
        while not self.game_over:
            current_player = self.turn_manager.get_current_player()
            dice_result = current_player.take_turn(self.dice_strategy)
            print(f"{current_player.name} rolled a {dice_result}")
            
            # Create and execute move command
            move_cmd = MoveCommand(current_player, dice_result, self.board)
            move_result = move_cmd.execute()
            self.move_history.append(move_cmd)
            
            # Update game state
            if move_result["moved"]:
                print(f"{current_player.name} moved from {move_result['old_position']} to {move_result['new_position']}")
                
                # Check if player encountered a snake or ladder
                if move_result["encounter_type"] == "snake":
                    state = {
                        "snake_encounter": True,
                        "current_player": current_player.name,
                        "from_position": move_result['old_position'] + dice_result,
                        "to_position": move_result['new_position'],
                        "game_over": False,
                        "turn_change": False,
                        "ladder_encounter": False
                    }
                    self.turn_manager.notify(players=self.players, state=state)
                
                elif move_result["encounter_type"] == "ladder":
                    state = {
                        "ladder_encounter": True,
                        "current_player": current_player.name,
                        "from_position": move_result['old_position'] + dice_result,
                        "to_position": move_result['new_position'],
                        "game_over": False,
                        "turn_change": False,
                        "snake_encounter": False
                    }
                    self.turn_manager.notify(players=self.players, state=state)
                
                # Check if player won
                if move_result["game_over"]:
                    self.game_over = True
                    self.winner = current_player
                    
                    # Notify observers about game over
                    state = {
                        "game_over": True,
                        "winner": current_player.name,
                        "current_player": current_player.name,
                        "snake_encounter": False,
                        "ladder_encounter": False,
                        "turn_change": False
                    }
                    self.turn_manager.notify(players=self.players, state=state)
                    
                    print(f"\n{current_player.name} has won the game!")
                    break
            
            # Next player's turn
            self.turn_manager.next_turn()
            
            # Display current standings
            self.display_standings()
            print("\n" + "-" * 40 + "\n")
    
    def undo_last_move(self):
        if self.move_history:
            last_move = self.move_history.pop()
            if last_move.undo():
                print(f"Undid last move. {last_move.player.name} moved back to position {last_move.old_position}")
                return True
        return False
    
    def display_standings(self):
        print("\nCurrent Standings:")
        sorted_players = sorted(self.players, key=lambda p: p.position, reverse=True)
        for i, player in enumerate(sorted_players):
            print(f"{i+1}. {player.name}: Position {player.position}")

"""
Main: Entry point for the game
"""

# snake_and_ladder_demo.py
def run_game():
    # Create game instance (Singleton)
    game = SnakeAndLadder(board_size=100, num_snakes=8, num_ladders=8)
    
    # Add players
    num_players = int(input("Enter number of players: "))
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        player_type = input(f"Is {name} a human or computer player? (human/computer): ")
        game.add_player(name, player_type)
    
    # Choose dice strategy
    strategy_choice = input("Choose dice strategy (default/loaded): ")
    if strategy_choice.lower() == "loaded":
        favored_player = input("Which player should be favored? ")
        game.set_dice_strategy(LoadedDiceStrategy(favored_player))
    
    # Start the game
    game.start_game()

if __name__ == "__main__":
    run_game()