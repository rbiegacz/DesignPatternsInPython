#
# Copyright (c) 2016 Rafal Biegacz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

""" this is an example for Factory design pattern"""

from abc import ABCMeta, abstractmethod
from patterndemo import PatternDemo

class Investment:
    """ abstract base class for an investment"""
    __metaclass__ = ABCMeta
    def __init__(self):
        pass
    @abstractmethod
    def investment_info(self):
        """virtual function that is to give info about investment"""
        pass

class StockExchange(Investment):
    """class for an Stock Exchange investment"""
    Name = ""
    Amount = ""
    PurchaseDate = None
    def investment_info(self):
        print "Company on Stock Exchange"

class TermDeposit(Investment):
    """class for Term Deposit investment"""
    interestRate = 0.01
    def investment_info(self):
        print "Term Deposit in a Bank"

class Bond(Investment):
    """class for Bond investment"""
    interestRate = 0.01
    def investment_info(self):
        print "Bonds are usually emitted by governments"

INVESTMENT_TYPE = {
    "termdeposit" : TermDeposit,
    "stockexchange" : StockExchange,
    "bond" : Bond,
}

class InvestmentFactory(object):
    """class implementing factory for various types of investments"""
    def __init__(self):
        pass
    def create_investment(self, invest):
        """factory method"""
        if invest in INVESTMENT_TYPE:
            return INVESTMENT_TYPE[invest]()
        return None

class FactoryPatternDemo(PatternDemo):
    """class running Factory design pattern example"""
    @staticmethod
    def pattern_info():
        PatternDemo.pattern_info()
        print "This is an example of Factory Design Pattern"
    def pattern_run(self):
        factory = InvestmentFactory()
        investment_type = ["termdeposit", "stockexchange", "stockexchange",
                           "termdeposit", "none", "bond"]
        for investment_example in investment_type:
            temp = factory.create_investment(investment_example)
            if temp != None:
                temp.investment_info()
