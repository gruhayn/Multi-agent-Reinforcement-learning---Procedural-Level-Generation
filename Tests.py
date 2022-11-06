# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:41:44 2022

@author: agana
"""

import unittest

from mechanics.GoRightMechanic import GoRightMechanic 
from agents.MovableAgent import MovableAgent

class TestGoRightMechanic(unittest.TestCase):

    def test_goRight1(self):
        mec = GoRightMechanic(1)
        agent = MovableAgent(1, [mec])
        prevX = agent.xPosition
        agent.doMechanic(0)
        laterX =  agent.xPosition
        self.assertEqual(prevX+1, laterX, "prev+1 = laterX")
        
        
    def test_goRight2(self):
        mec = GoRightMechanic(2)
        agent = MovableAgent(1, [mec])
        prevX = agent.xPosition
        agent.doMechanic(0)
        laterX =  agent.xPosition
        self.assertEqual(prevX+2, laterX, "prev+1 = laterX")
        
    def test_goRightMinus1(self):
        mec = GoRightMechanic(-1)
        agent = MovableAgent(1, [mec])
        prevX = agent.xPosition
        agent.doMechanic(0)
        laterX =  agent.xPosition
        self.assertEqual(prevX-1, laterX, "prev+1 = laterX")
    
    def test_goRightMinus2(self):
        mec = GoRightMechanic(-2)
        agent = MovableAgent(1, [mec])
        prevX = agent.xPosition
        agent.doMechanic(0)
        laterX =  agent.xPosition
        self.assertEqual(prevX-2, laterX, "prev+1 = laterX")


from agents.MovableAgent import MovableAgent  
from mechanics.GoUpMechanic import GoUpMechanic
        
class TestGoUpMechanic(unittest.TestCase):

    def test_goUp1(self):
        mec = GoUpMechanic(1)
        agent = MovableAgent(1, [mec])
        prev = agent.yPosition
        agent.doMechanic(0)
        later =  agent.yPosition
        self.assertEqual(prev+1, later, "prev+1 = laterX")
        
        
    def test_goUp2(self):
        mec = GoUpMechanic(2)
        agent = MovableAgent(1, [mec])
        prev = agent.yPosition
        agent.doMechanic(0)
        later =  agent.yPosition
        self.assertEqual(prev+2, later, "prev+1 = laterX")
        
    def test_goUpMinus1(self):
        mec = GoUpMechanic(-1)
        agent = MovableAgent(1, [mec])
        prev = agent.yPosition
        agent.doMechanic(0)
        later =  agent.yPosition
        self.assertEqual(prev-1, later, "prev+1 = laterX")
        
    def test_goUpMinus2(self):
        mec = GoUpMechanic(-2)
        agent = MovableAgent(1, [mec])
        prev = agent.yPosition
        agent.doMechanic(0)
        later =  agent.yPosition
        self.assertEqual(prev-2, later, "prev+1 = laterX")
    

if __name__ == '__main__':
    unittest.main()
    

