
from game.cells.agentCell import AgentCell
from game.cells.coinCell import CoinCell
from game.cells.bombCell import BombCell
from game.cells.emptyCell import EmptyCell


class CellMaker(object):
    def __init__(self):
        pass
    
    def createAgentCell(self, agent, cellPosition = [None, None]):
        return AgentCell(agent, cellPosition)
    
    def createCoinCell(self, cellPosition):
        return CoinCell(cellPosition)
    
    def createBombCell(self, cellPosition):
        return BombCell(cellPosition)
    
    def createEmptyCell(self, cellPosition):
        return EmptyCell(cellPosition)
    
    
    