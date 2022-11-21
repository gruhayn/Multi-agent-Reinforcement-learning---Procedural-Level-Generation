# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:36:51 2022

@author: agana
"""

from mechanics.Mechanic import Mechanic 
from Constants import MechanicTypes

class GoRightMechanic(Mechanic):
    def __init__(self, stepCount = None):
        name = f'{GoRightMechanic=}'.split('=')[0] + str(stepCount)
        Mechanic.__init__(self, MechanicTypes.GoRight, name)
        self.stepCount = stepCount if stepCount is not None else 1 
        
    def do(self, agent):
        if agent.IsMovable:
            agent.xPosition += self.stepCount
        