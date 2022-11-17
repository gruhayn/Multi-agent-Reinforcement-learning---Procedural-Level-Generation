from game.cells.cell import Cell
from Constants import CellTypes

class EmptyCell(Cell):
    
    def __init__(self, cellPosition, name="E"):
        Cell.__init__(self, CellTypes.Empty, cellPosition, name)