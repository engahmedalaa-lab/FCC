from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
   
    def make_move(self):
        move = random.choice(self.moves)
        n_pos = ((self.position[0] + move[0]), (self.position[1] + move[1]))
        self.position = n_pos
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
   
    def __init__(self) -> None:
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
   
    def level_up(self):
        n_mov = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves += n_mov