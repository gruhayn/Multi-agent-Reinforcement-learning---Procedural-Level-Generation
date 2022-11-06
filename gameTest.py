# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 00:30:34 2022

@author: agana
"""

from game.game import Game    
from game.cellMaker import CellMaker
from agents.MovableAgent import MovableAgent
from mechanics.GoRightMechanic import GoRightMechanic
from mechanics.GoUpMechanic import GoUpMechanic 


goR = GoRightMechanic()
goU = GoUpMechanic()

mechArray = [goU,goR]

agent1 = MovableAgent(1, [goU], 2,3 ,None, "A" )
agent2 = MovableAgent(2, [goU, goR], 4,4,None, "B" )
agent3 = MovableAgent(1, [goU], 5,2 ,None, "K" )

a = Game([agent1, agent2, agent3], 6,7, 3,5, CellMaker())    

a.printBoardWithAgents()
