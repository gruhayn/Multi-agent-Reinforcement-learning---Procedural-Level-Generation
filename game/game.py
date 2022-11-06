
import numpy as np
import random


class Game():
     
    def __init__(self, agents, width, height, bombCount, coinCount, cellMaker):
        self.agents = agents
        self.width = width
        self.height = height
        self.bombCount = bombCount
        self.coinCount = coinCount
        self.cellMaker = cellMaker
        
        self.__createBoard()     
        
        
    def __setAgentsCells(self):
        for agent in self.agents:
            aRow , aColumn = self.__agentPosToBoardPos(agent)
            self.putCellOnGridIfValid(aRow, aColumn, self.cellMaker.createAgentCell(agent))
        
    def __createBoard(self):
        
        self.board = np.full( shape=(self.height, self.width ), fill_value=self.cellMaker.createEmptyCell() )
        
        self.__setAgentsCells()
        
        self.__putRandomBombs()
        self.__putRandomCoins()
               
    
    def putCellOnGridIfValid(self, row, column, cell):
        isLegalCellToPlace = self.__isLegalCellToPlace(row, column)
        
        
        if(isLegalCellToPlace):
            self.__putCellOnGrid(row, column, cell)
            
        return isLegalCellToPlace
    
    def __putCellOnGrid(self, row, column, cell):
        self.board[row, column] = cell
        
        
    def __isInGrid(self, row, column):
        isInGrid = True
        
        if(row<0 or row>=self.height):
            isInGrid = False
        
        if(column<0 or column>=self.width):
            isInGrid = False
        
        return isInGrid
    
    
    
    def __getRandomRowAndColumn(self):
        row = random.randrange(self.height)
        column = random.randrange(self.width)
        return row, column
    
    def __putRandomBombs(self):
        
        for i in range(self.bombCount):
            row, column = self.__getRandomRowAndColumn()
            
            while not self.__isLegalCellToPlace(row, column):
                row, column = self.__getRandomRowAndColumn()
                
            self.__putCellOnGrid(row, column, self.cellMaker.createBombCell())
    
    def __putRandomCoins(self):
        
        for i in range(self.coinCount):
            row, column = self.__getRandomRowAndColumn()
            
            while not self.__isLegalCellToPlace(row, column):
                row, column = self.__getRandomRowAndColumn()
                  
            self.__putCellOnGrid(row, column, self.cellMaker.createCoinCell())
    
    
    def printBoardWithAgents(self):
        
        for row in range(self.height-1 , -1, -1):
            
            for column in range(self.width):
                    print("{0: >4}".format(self.board[row,column].getCellName()), end=" ")
                    
            print("\n")
                        
    def __agentPosToBoardPos(self, agent):
        row = agent.yPosition 
        column = agent.xPosition
        return row , column
    
    def __isLegalCellToPlace(self, row, column):
        if(self.__isInGrid(row, column)) :
            
            isEmptyCell = self.board[row,column].isEmptyCell()                   
            return isEmptyCell
        else:
            return False
        
    
    
        
    
        