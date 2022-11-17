
from Constants import ErrorCodes
from Constants import ResultCodes

class GameRule(object):
    
    def __init__(self):
        self.isPostRule = False
        self.isPreRule = False
        pass
    
    
    
    def checkRule(self, data):
        raise NotImplementedError()
      
    def postMethodOnSuccess(self, data):
        raise NotImplementedError()

    def __postMethodOnFailure(self, data):
        raise NotImplementedError()

    def __postMethodOnSuccess(self, data):
        raise NotImplementedError()
        
    def applyAfterMechanicEffects(self, data):
        return self.__updateAgentNextCellAndPrevCellOnBoard(data)
        
    def __updateAgentNextCellAndPrevCellOnBoard(self, data):
        
        #do not create new pre rule for this
        #it should be check every time before trying to update 
        #board and agent
        #if cell is already updated with agent position then do not update
        if data.destCell.isAgentCell():
            return ResultCodes.Success, None
    
        row, column = data.game.agentPosToBoardPosWithXY(data.agent.xPosition, 
                                             data.agent.yPosition)
        cell = data.game.board[row, column]
        
        if cell.isAgentCell():
            if cell.agent.UUID == data.agent.UUID:
                return ResultCodes.Success, None
        
        data.game.createAgentCell(data.agent)
        data.game.setCellAsEmptyCell(data.agent.prevAgent.xPosition, 
                                     data.agent.prevAgent.yPosition)
        return ResultCodes.Success, None