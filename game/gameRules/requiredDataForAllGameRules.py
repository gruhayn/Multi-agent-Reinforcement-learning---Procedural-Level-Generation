
class RequiredDataForAllGameRules(object):
    
    def __init__(self, keys, values):
        for (key, value) in zip(keys, values):
            self.__dict__[key] = value
    
    def __setattr__(self, name, value):
        raise Exception("It is read only!")