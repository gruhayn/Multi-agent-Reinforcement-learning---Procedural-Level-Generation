from game.cell import Cell
from Constants import CellTypes

class EmptyCell(Cell):
    
    def __init__(self, name="E"):
        Cell.__init__(self, CellTypes.Empty, name)