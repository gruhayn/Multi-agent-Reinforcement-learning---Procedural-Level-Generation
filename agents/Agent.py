# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:27:56 2022

@author: agana
"""
import uuid

from Constants import ErrorCodes
from Constants import ResultCodes

class Agent(object):
    
    def __init__(self, teamId = 0, mechanics = None, xPosition = None, yPosition = None, zPosition = None, name = None):
        #set mechanics of agent 
        print(mechanics)
        
        self.agentUUID = uuid.uuid4().hex
        
        self.teamId = teamId
        self.mechanics = mechanics if mechanics is not None else []
        self.xPosition = xPosition if xPosition is not None else 0
        self.yPosition = yPosition if yPosition is not None else 0
        self.zPosition = zPosition if zPosition is not None else 0
        self.name = name
        
    def overrideMechanics(self, mechanics):
        self.mechanics = mechanics
        
    def addMechanic(self, mechanic):
        self.mechanics.append(mechanic)
        
    def doMechanic(self, index = None, mechanic = None):
        if index is not None:
            self.mechanics[index].do(self)
            return ResultCodes.Success, None, None
        elif mechanic is not None:
            try:
                index = self.mechanics().index(mechanic)
                self.mechanics[index].do(self)
                return ResultCodes.Success, None, None
            except:
                return ResultCodes.Error, ErrorCodes.AgentDoesntHaveThisMechanic, None
        

