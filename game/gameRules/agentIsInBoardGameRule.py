
from game.gameRules.gameRule import GameRule
from game.gameRules.ICheckAfterMechanicExecutedGameRule import ICheckAfterMechanicExecutedGameRule

from Constants import ErrorCodes
from Constants import ResultCodes

class AgentIsInBoardGameRule(GameRule, ICheckAfterMechanicExecutedGameRule):
    
    def __init__(self):
        GameRule.__init__(self)
        ICheckAfterMechanicExecutedGameRule.__init__(self)
        
        self.order = 1
        
    def checkRule(self, data):
        if data.game.isAgentInBoard(data.agent):
            return self.__postMethodOnSuccess(data)    
        else:
            return self.__postMethodOnFailure(data) 
            
    
        
    def __postMethodOnFailure(self, data):
        data.game.removeAgentFromAgentList(data.agent)
        data.agent.die()
        data.game.setCellAsEmptyCell(data.agent.prevAgent.xPosition, 
                                     data.agent.prevAgent.yPosition)
        return ResultCodes.Error, ErrorCodes.AgentNotInGame

    def __postMethodOnSuccess(self, data):
        return self.applyAfterMechanicEffects(data)
            
            
            
        