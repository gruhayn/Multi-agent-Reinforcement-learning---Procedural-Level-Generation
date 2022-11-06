from enum import IntEnum

class MechanicTypes(IntEnum):
    GoRight = 1
    GoUp = 2
    
class CellTypes(IntEnum):
    Empty = 1
    Bomb = 2
    Coin = 3
    Agent = 4

    
class ErrorCodes(IntEnum):
    AgentDoesntHaveThisMechanic = 1
    
class ResultCodes(IntEnum):
    Success = 1
    Error = 2