
from game.gameRules.gameRule import GameRule
from game.gameRules.ICheckBeforeMechanicExecutedGameRule import ICheckBeforeMechanicExecutedGameRule

from Constants import ErrorCodes
from Constants import ResultCodes

class IsAgentAliveGameRule(GameRule, ICheckBeforeMechanicExecutedGameRule):
    
    def __init__(self):
        GameRule.__init__(self)
        ICheckBeforeMechanicExecutedGameRule.__init__(self)
        
        self.order = 1
        
    def checkRule(self, data):
        if data.agent.isAgentDead():
            return self.__postMethodOnSuccess(data)    
        else:
            return self.__postMethodOnFailure(data) 
            
    
        
    def __postMethodOnFailure(self, data):
        return ResultCodes.Success, None

    def __postMethodOnSuccess(self, data):
        return ResultCodes.Error, ErrorCodes.AgentNotInGame
            
            
            
        