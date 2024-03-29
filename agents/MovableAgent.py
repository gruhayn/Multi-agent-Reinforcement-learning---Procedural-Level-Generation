# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:21:43 2022

@author: agana
"""

from agents.Agent import Agent
from agents.IMovableAgent import IMovableAgent

class MovableAgent(Agent, IMovableAgent):
    
    def __init__(self, teamId, mechanics = None, position = [None, None, None], name = None):
        Agent.__init__(self, teamId, mechanics, position, name)
        IMovableAgent.__init__(self)

