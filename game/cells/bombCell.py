from game.cells.cell import Cell
from Constants import CellTypes

class BombCell(Cell):
    
    def __init__(self, cellPosition, name="B"):
        Cell.__init__(self, CellTypes.Bomb, cellPosition, name)