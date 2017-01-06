from abc import ABCMeta,abstractmethod

class PatternDemo:
    __metaclass__ = ABCMeta
    
    patternName = ""
 
    def __init__(self, name):
        self.patternName = name
        
    @staticmethod
    def PatternInfo():
        print "\n--------------------------------------------"
    
    @abstractmethod
    def PatternRun(self):
        pass
    