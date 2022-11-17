
from Constants import CellTypes

class Cell(object):
    
    def __init__(self, cellTypeId, cellPosition, name):
        self.cellTypeId = cellTypeId
        self.name = name
        if cellPosition is not None:
            self.xPosition = cellPosition[0]
            self.yPosition = cellPosition[1]
        
        
    def isEmptyCell(self):
        return self.cellTypeId == CellTypes.Empty
    
    def isBombCell(self):
        return self.cellTypeId == CellTypes.Bomb
    
    def isCoinCell(self):
        return self.cellTypeId == CellTypes.Coin
    
    def isAgentCell(self):
        return self.cellTypeId == CellTypes.Agent
        
    
    def getCellName(self, includePosition = False):
        if includePosition:
            return  self.name + ":"+ str(self.xPosition)+":"+str(self.yPosition)
        else:
            return self.name
    
        