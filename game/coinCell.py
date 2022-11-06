
from game.cell import Cell
from Constants import CellTypes

class CoinCell(Cell):
    
    def __init__(self, name="C"):
        Cell.__init__(self, CellTypes.Coin, name)
    