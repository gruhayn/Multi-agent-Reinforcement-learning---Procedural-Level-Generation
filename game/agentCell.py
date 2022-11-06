from game.cell import Cell
from Constants import CellTypes

class AgentCell(Cell):
    
    def __init__(self, agent, name=None):
        if name is None:
            name = str(agent.teamId) + str(agent.name)
        Cell.__init__(self, CellTypes.Agent, name)
        