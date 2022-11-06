from game.cell import Cell
from Constants import CellTypes

class BombCell(Cell):
    
    def __init__(self, name="B"):
        Cell.__init__(self, CellTypes.Bomb, name)