
from game.gameRules.gameRule import GameRule
from game.gameRules.ICheckAfterMechanicExecutedGameRule import ICheckAfterMechanicExecutedGameRule

from Constants import ErrorCodes
from Constants import ResultCodes

class AgentOnBombGameRule(GameRule, ICheckAfterMechanicExecutedGameRule):
    
    def __init__(self):
        GameRule.__init__(self)
        ICheckAfterMechanicExecutedGameRule.__init__(self)
        
        self.order = 2
        
        
    def checkRule(self, data):
        if data.destCell.isBombCell():
            return self.__postMethodOnSuccess(data)
        else:
            return self.__postMethodOnFailure(data)
            
    def __postMethodOnSuccess(self, data):
        data.agent.die()
        data.game.removeAgentFromAgentList(data.agent)
        data.game.setCellAsEmptyCell(data.agent.prevAgent.xPosition, 
                                     data.agent.prevAgent.yPosition)
        data.game.setCellAsEmptyCell(data.destCell.xPosition, 
                                     data.destCell.yPosition)
        
        return ResultCodes.Error, ErrorCodes.AgentOnBomb

    def __postMethodOnFailure(self, data):
        return self.applyAfterMechanicEffects(data)
        