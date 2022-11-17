
from game.cells.cell import Cell
from Constants import CellTypes

class CoinCell(Cell):
    
    def __init__(self, cellPosition, name="C", value=1):
        Cell.__init__(self, CellTypes.Coin, cellPosition, name)
        self.value = value
        
    def getCellValue(self):
        return self.value
    