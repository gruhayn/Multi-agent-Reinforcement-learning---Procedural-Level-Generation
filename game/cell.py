
from Constants import CellTypes

class Cell(object):
    
    def __init__(self, cellTypeId, name):
        self.cellTypeId = cellTypeId
        self.name = name
        
    def isEmptyCell(self):
        return self.cellTypeId == CellTypes.Empty
    
    
    def getCellName(self):
        return  self.name
    
    
        