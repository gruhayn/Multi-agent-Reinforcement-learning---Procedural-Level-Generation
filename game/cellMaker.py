
from game.agentCell import AgentCell
from game.coinCell import CoinCell
from game.bombCell import BombCell
from game.emptyCell import EmptyCell


class CellMaker(object):
    def __init__(self):
        pass
    
    def createAgentCell(self, agent):
        return AgentCell(agent)
    
    def createCoinCell(self):
        return CoinCell()
    
    def createBombCell(self):
        return BombCell()
    
    def createEmptyCell(self):
        return EmptyCell()
    
    
    