
from game.gameRules.gameRule import GameRule
from game.gameRules.ICheckAfterMechanicExecutedGameRule import ICheckAfterMechanicExecutedGameRule 

from Constants import ErrorCodes
from Constants import ResultCodes

class AgentOnAnotherAgentGameRule(GameRule, ICheckAfterMechanicExecutedGameRule ):
    
    def __init__(self):
        GameRule.__init__(self)
        ICheckAfterMechanicExecutedGameRule .__init__(self)
        
        self.order = 2
        
    def checkRule(self, data):
        if data.destCell.isAgentCell() and (data.destCell.agent.UUID is not data.agent.UUID):
            return self.__postMethodOnSuccess(data)
        else:
            return self.__postMethodOnFailure(data)
            
    def __postMethodOnSuccess(self, data):
        data.agent.goBackPreviousState()
        return ResultCodes.Success, None

    def __postMethodOnFailure(self, data):
        return ResultCodes.Success, None
            
