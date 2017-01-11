""" this is a demo template; each demo needs to inherit after this class """

from abc import ABCMeta, abstractmethod

class PatternDemo:
    """ this is a demo template; each demo needs to inherit after this class """
    __metaclass__ = ABCMeta
    pattern_name = ""
    def __init__(self, name):
        """ constructor in Pattern Demo class, the second argument is a name for a demo """
        self.pattern_name = name
    @staticmethod
    def pattern_info():
        """ common info formating for all demos"""
        print "\n--------------------------------------------"
    @abstractmethod
    def pattern_run(self):
        """ each demo needs to implement PatternRun function"""
        pass
    