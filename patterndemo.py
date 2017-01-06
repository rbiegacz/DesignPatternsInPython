from abc import ABCMeta,abstractmethod

class PatternDemo:
    __metaclass__ = ABCMeta
    
    @staticmethod
    def PatternInfo():
        print "\n--------------------------------------------"
    
    @abstractmethod
    def PatternRun(self):
        pass
    