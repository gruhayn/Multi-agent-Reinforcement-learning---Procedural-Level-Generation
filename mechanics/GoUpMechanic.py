# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 21:52:14 2022

@author: agana
"""

from mechanics.Mechanic import Mechanic 
from Constants import MechanicTypes

class GoUpMechanic(Mechanic):
    def __init__(self, stepCount = None):
        Mechanic.__init__(self, MechanicTypes.GoUp)
        self.stepCount = stepCount if stepCount is not None else 1 
        
    def do(self, agent):
        if agent.IsMovable:
            agent.yPosition += self.stepCount
        