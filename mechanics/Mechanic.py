# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:22:29 2022

@author: agana
"""

import uuid

class Mechanic(object):
    
    def __init__(self, mechanicTypeId):
        self.mechanicTypeId = mechanicTypeId
        self.mechanicUUID = uuid.uuid4().hex
        
    def do(self, agent):
        raise NotImplementedError()
    
    def __eq__(self, other): 
        if not isinstance(other, Mechanic):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.mechanicUUID == other.mechanicUUID
    
        
        
        
        
        
        
        