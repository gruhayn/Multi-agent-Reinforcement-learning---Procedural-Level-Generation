# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 00:30:34 2022

@author: agana
"""

from game.game import Game    
from game.cells.cellMaker import CellMaker
from agents.MovableAgent import MovableAgent
from mechanics.GoRightMechanic import GoRightMechanic
from mechanics.GoUpMechanic import GoUpMechanic 

from game.gameRules.agentIsInBoardGameRule import AgentIsInBoardGameRule
from game.gameRules.agentOnAnotherAgentGameRule import AgentOnAnotherAgentGameRule
from game.gameRules.agentOnBombGameRule import AgentOnBombGameRule
from game.gameRules.agentOnCoinGameRule import AgentOnCoinGameRule
from game.gameRules.isGameOverGameRule import IsGameOverGameRule
from game.gameRules.isAgentAliveGameRule import IsAgentAliveGameRule

from game.gameRules.requiredDataForAllGameRules import RequiredDataForAllGameRules

goR = GoRightMechanic(1)
goU = GoUpMechanic(1)
goL = GoRightMechanic(-1)
goD = GoUpMechanic(-1)


agent1 = MovableAgent(1, [goU, goR, goL, goD], [1,1 ,None], "A" )
agent2 = MovableAgent(2, [goU, goR], [2,2,None], "I" )
agent3 = MovableAgent(1, [goU], [2,1 ,None], "K" )

agentIsInBoardGameRule = AgentIsInBoardGameRule()
agentOnAnotherAgentGameRule = AgentOnAnotherAgentGameRule()
agentOnBombGameRule = AgentOnBombGameRule()
agentOnCoinGameRule = AgentOnCoinGameRule()
isGameOverGameRule = IsGameOverGameRule()
isAgentAliveGameRule = IsAgentAliveGameRule()

gameRulesNotTested = [agentOnBombGameRule, agentIsInBoardGameRule]

gameRulesTest = [agentOnBombGameRule, agentIsInBoardGameRule, 
                 agentOnCoinGameRule, agentOnAnotherAgentGameRule, isGameOverGameRule, isAgentAliveGameRule]

cellMaker = CellMaker()

predefinedCoinCells = [
    cellMaker.createCoinCell([1,2]),
    cellMaker.createCoinCell([2,4])
    ]


predefinedBombCells=[
 cellMaker.createBombCell([1,4]),
 cellMaker.createBombCell([0,2])
 ]

a = Game([agent1, agent2, agent3], 
         3,
         5, 
         
         3,
         5, 
         
         cellMaker, 

         gameRulesTest, 
         
         predefinedCoinCells,
         
         predefinedBombCells
         )    

result, message = None, None

while True:
    print("--------------------------------")
    
    a.printBoardWithAgents(True)
    print(result, message)
    print(a.agentUUIDToGatheredCoinValueDict)
    print("won",a.whichTeamWon())
    where = input("where?")

    if where == "w":
        result, message = a.playForAgent(agent1, goU)
    elif where == "s":
        result, message = a.playForAgent(agent1, goD)
    elif where == "a":
        result, message = a.playForAgent(agent1, goL)
    elif where == "d":
        result, message = a.playForAgent(agent1, goR)
        
