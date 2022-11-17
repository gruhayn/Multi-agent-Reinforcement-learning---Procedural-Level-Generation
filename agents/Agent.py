# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:27:56 2022

@author: agana
"""
import uuid

from Constants import ErrorCodes
from Constants import ResultCodes

import copy

class Agent(object):
    
    def __init__(self, teamId = 0, mechanics = None, position = [None, None, None], name = None):
        
        self.UUID = uuid.uuid4().hex
        
        self.teamId = teamId
        self.mechanics = mechanics if mechanics is not None else []
        self.xPosition = position[0] if position[0] is not None else 0
        self.yPosition = position[1] if position[1] is not None else 0
        self.zPosition = position[2] if position[2] is not None else 0
        self.name = name

        self.isDead = False
        self.willDieOnBomb = True        

    def die(self):
        self.isDead = True

    def isAgentDead(self):
        return self.isDead
        
    def overrideMechanics(self, mechanics):
        self.mechanics = mechanics
        
    def addMechanic(self, mechanic):
        self.mechanics.append(mechanic)
        
    def doMechanic(self, index = None, mechanic = None, isCheckMechanicExistence = True):
        if index is not None:
            self.__saveAgentBeforeDoingMechanic()
            self.mechanics[index].do(self)
            return ResultCodes.Success, None
        
        elif mechanic is not None:
            try:
                if isCheckMechanicExistence:
                    if mechanic not in self.mechanics:
                        return ResultCodes.Error, ErrorCodes.AgentDoesntHaveThisMechanic
                
                self.__saveAgentBeforeDoingMechanic()
                
                index = self.mechanics.index(mechanic)
                self.mechanics[index].do(self)
                return ResultCodes.Success, None
                
                    
            except:
                return ResultCodes.Error, ErrorCodes.AgentDoesntHaveThisMechanic
        
    def __saveAgentBeforeDoingMechanic(self):
        self.prevAgent = copy.deepcopy(self)
       
    def goBackPreviousState(self):
        #do not save from self.prevAgent because you will 
        #lose pointer to agent
        self.xPosition = self.prevAgent.xPosition
        self.yPosition = self.prevAgent.yPosition
        self.zPosition = self.prevAgent.zPosition