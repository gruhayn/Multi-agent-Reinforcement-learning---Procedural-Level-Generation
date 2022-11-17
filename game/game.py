

import numpy as np
import random
import copy

from Constants import ErrorCodes,ResultCodes

from game.gameRules.requiredDataForAllGameRules import RequiredDataForAllGameRules

class Game():
     
    def __init__(self, 
                 agents, 
                 width, 
                 height, 
                 bombCount, 
                 coinCount, 
                 cellMaker, 
                 gameRules=None, 
                 predefinedCoinCells = None, 
                 predefinedBombCells = None):
        
        self.agents = agents
        self.width = width
        self.height = height
        self.bombCount = bombCount
        self.coinCount = coinCount
        self.cellMaker = cellMaker
        self.agentUUIDToGatheredCoinValueDict = {agent.UUID:0 for agent in agents}
        
        self.teamIdToGatheredCoinValueDict = {}
        for agent in agents:
            val = self.teamIdToGatheredCoinValueDict.get(agent.teamId)
            if val is None:
                self.teamIdToGatheredCoinValueDict[agent.teamId] = 0
                
        
        self.teamToAgents = {}
        for agent in agents:
            val = self.teamToAgents.get(agent.teamId)
            
            if val is None:
                self.teamToAgents[agent.teamId] = [agent.UUID]
            else:
                self.teamToAgents[agent.teamId] = val + [agent.UUID]
        
        
        
        if gameRules is not None:
            self.postGameRules = sorted( 
                [x for x in gameRules if x.isPostRule ],
                key=lambda d: d.order
                )
            
            self.preGameRules = sorted( 
                [x for x in gameRules if x.isPreRule ],
                key=lambda d: d.order
                )
        else:
            self.postGameRules = []
        
        self.__isOver = False
        
        self.__createBoard(predefinedCoinCells, predefinedBombCells)   
        
    def isOver(self):
        if not self.__isOver:
            
            coinCellsCount = self.__getActiveCoinCountInGame()        
            
            teamId = self.whichTeamWon()
            if teamId is not None or coinCellsCount==0:
                self.__isOver = True
                return True
        else:
            return True
    
    def __getActiveCoinCountInGame(self):
        coinCellsCount = 0
        for row in range(self.height):
            for column in range(self.width):
                if self.board[row, column].isCoinCell():
                    coinCellsCount = coinCellsCount + 1    
        return coinCellsCount
    
    
    def whichTeamWon(self):
        
        wonTeamId = None
        notWon = False
        
        for key, value in self.teamToAgents.items():
            if value:
                if wonTeamId is None:
                    wonTeamId = key
                else:
                    notWon = True
                    
        if not notWon:
            if wonTeamId is not None:
                return wonTeamId 
        else:
            coinCellsCount = self.__getActiveCoinCountInGame()
            wonTeamId = None
            
            if coinCellsCount == 0:
                coinCount = -1
                
                for key, value in self.teamIdToGatheredCoinValueDict.items():
                    if value > coinCount:
                        coinCount = value
                        wonTeamId = key
                
                return wonTeamId
                
                    
            else:
                return None
        
        
        
    def __setAgentsCells(self):
        for agent in self.agents:
            self.createAgentCell(agent)
            
    def createAgentCell(self, agent):
        aRow , aColumn = self.__agentPosToBoardPos(agent)
        self.putCellOnGridIfValid(aRow, aColumn, self.cellMaker.createAgentCell(agent,[agent.xPosition, agent.yPosition]))
    
        
    def __createBoard(self, predefinedCoinCells, predefinedBombCells):
        
        self.board = np.full( shape=(self.height, self.width ), fill_value=object)
        
        for row in range(self.height):
            for column in range(self.width):
                #set empty cells locations
                x, y = self.__boardPosToAgentPos(row, column)
                self.setCellAsEmptyCell(x, y)
        
        self.__setAgentsCells()
        
        if predefinedBombCells is None:
            self.__putRandomBombs()
        else:
            self.__addBombCellsToBoard(predefinedBombCells)
        
        if predefinedCoinCells is None:
            self.__putRandomCoins()
        else:
            self.__addCoinCellsToBoard(predefinedCoinCells)
           
    def __addBombCellsToBoard(self, predefinedBombCells):
        for bomb in predefinedBombCells:
            row, column = self.__agentPosToBoardPosWithXY(bomb.xPosition, bomb.yPosition)
            self.__putCellOnGrid(row, column, bomb)
        
            
    def __addCoinCellsToBoard(self, predefinedCoinCells):
        
        for cell in predefinedCoinCells:
            row, column = self.__agentPosToBoardPosWithXY(cell.xPosition, cell.yPosition)
            self.__putCellOnGrid(row, column, cell)
        
        
    def setCellAsEmptyCell(self, x, y):
        emptyCell = self.cellMaker.createEmptyCell([x,y])
        row, column = self.__agentPosToBoardPosWithXY(x, y)
        self.board[row, column] = emptyCell
    
    def putCellOnGridIfValid(self, row, column, cell):
        isLegalCellToPlace = self.__isLegalCellToPlace(row, column)
        
        
        if(isLegalCellToPlace):
            self.__putCellOnGrid(row, column, cell)
            
        return isLegalCellToPlace
    
    def __putCellOnGrid(self, row, column, cell):
        self.board[row, column] = cell
        
    def isAgentInBoard(self, agent):
        row, column = self.__agentPosToBoardPos(agent)
        return self.__isInBoard(row, column)
        
    def __isInBoard(self, row, column):
        isInBoard = True
        
        if(row<0 or row>=self.height):
            isInBoard = False
        
        if(column<0 or column>=self.width):
            isInBoard = False
        
        return isInBoard
    
    
    
    def __getRandomRowAndColumn(self):
        row = random.randrange(self.height)
        column = random.randrange(self.width)
        return row, column
    
    def __putRandomBombs(self):
        
        for i in range(self.bombCount):
            row, column = self.__getRandomRowAndColumn()
            
            while not self.__isLegalCellToPlace(row, column):
                row, column = self.__getRandomRowAndColumn()
               
            x, y = self.__boardPosToAgentPos(row, column)    
            self.__putCellOnGrid(row, column, self.cellMaker.createBombCell([x, y]))
    
    def __putRandomCoins(self):
        
        for i in range(self.coinCount):
            row, column = self.__getRandomRowAndColumn()
            
            while not self.__isLegalCellToPlace(row, column):
                row, column = self.__getRandomRowAndColumn()
            
            x, y = self.__boardPosToAgentPos(row, column)
            self.__putCellOnGrid(row, column, self.cellMaker.createCoinCell([x, y]))
    
    
    def printBoardWithAgents(self, includePosition = False):
        
        for row in range(self.height-1 , -1, -1):
            
            for column in range(self.width):
                    print("{0: >6}".format(self.board[row,column].getCellName(includePosition)), end=" ")
                    
            print("\n")
                        
    def __agentPosToBoardPos(self, agent):
        return self.__agentPosToBoardPosWithXY(agent.xPosition, agent.yPosition)
        
    def agentPosToBoardPosWithXY(self, x, y):
        return self.__agentPosToBoardPosWithXY(x, y)
    
    def __agentPosToBoardPosWithXY(self, x, y):
        row = y 
        column = x
        return row , column
    
    def __boardPosToAgentPos(self, row, column):
        y = row
        x = column
        return x, y
    
    def __isLegalCellToPlace(self, row, column):
        if(self.__isInBoard(row, column)) :
            
            isEmptyCell = self.board[row,column].isEmptyCell()                   
            return isEmptyCell
        else:
            return False
        
    
    def playForAgent(self, agent, mechanic):
        resultCode, errorCode = self.__playForAgentWithoutAgentExistenceCheck(agent, mechanic)
        return resultCode, errorCode
      
    def __playForAgentWithoutAgentExistenceCheck(self, agent, mechanic):
        resultCode = ResultCodes.Success
        
        self.__createRequiredDataForAllGameRules(agent)
        
        for preGameRule in self.preGameRules:
            if resultCode is ResultCodes.Success:
                resultCode, errorCode = preGameRule.checkRule(self.requiredDataForAllGameRules)
        
        if resultCode == ResultCodes.Success:    
            resultCode, errorCode = agent.doMechanic(None, mechanic)
    
        if resultCode == ResultCodes.Success:
            self.__createRequiredDataForAllGameRules(agent)
            resultCode = ResultCodes.Success
            for postGameRule in self.postGameRules:
                if resultCode is ResultCodes.Success:
                    resultCode, errorCode = postGameRule.checkRule(self.requiredDataForAllGameRules)
                
        return resultCode, errorCode
      
    def removeAgentFromAgentList(self, agent):
        self.agents = [x for x in self.agents if x.UUID is not agent.UUID ]
        self.teamToAgents[agent.teamId].remove(agent.UUID)
    
    def addCoinValueToAgentDict(self, agent, value):
        newValue = self.agentUUIDToGatheredCoinValueDict[agent.UUID] + value
        self.agentUUIDToGatheredCoinValueDict[agent.UUID] = newValue
        
        newValue = self.teamIdToGatheredCoinValueDict[agent.teamId] + value
        self.teamIdToGatheredCoinValueDict[agent.teamId] = newValue
    
    def __createRequiredDataForAllGameRules(self, agent):
        row, column = self.__agentPosToBoardPos(agent)
        
        if(self.__isInBoard(row, column)):
            destCell = copy.deepcopy(self.board[row,column])
        else:
            destCell = None
            
        game = self
        
        keys = [
            f'{agent=}'.split('=')[0],
            f'{destCell=}'.split('=')[0],
            f'{game=}'.split('=')[0]
            ]
        
        values = [
           agent,
           destCell,
           game
            ]
        self.requiredDataForAllGameRules = RequiredDataForAllGameRules(keys, values)
        
        
        
        
        
        
        
        
        
        
        
        