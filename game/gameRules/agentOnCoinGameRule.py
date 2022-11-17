
from game.gameRules.gameRule import GameRule
from game.gameRules.ICheckAfterMechanicExecutedGameRule import ICheckAfterMechanicExecutedGameRule

from Constants import ErrorCodes
from Constants import ResultCodes

class AgentOnCoinGameRule(GameRule, ICheckAfterMechanicExecutedGameRule):
    
    def __init__(self):
        GameRule.__init__(self)
        ICheckAfterMechanicExecutedGameRule.__init__(self)
        
        self.order = 2
       
    def checkRule(self, data):
        if data.destCell.isCoinCell():
            return self.__postMethodOnSuccess(data)
        else:
            return self.__postMethodOnFailure(data)
            
    def __postMethodOnSuccess(self, data):
        data.game.addCoinValueToAgentDict(data.agent, 
                                          data.destCell.getCellValue())
        
        data.game.setCellAsEmptyCell(data.destCell.xPosition, data.destCell.yPosition)
        
        self.applyAfterMechanicEffects(data)
        return ResultCodes.Success, None

    def __postMethodOnFailure(self, data):
        return self.applyAfterMechanicEffects(data)