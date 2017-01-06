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

from abc import ABCMeta,abstractmethod
from patterndemo import PatternDemo

class Investment:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def InvestmentInfo(self):
        pass

class StockExchange(Investment):
    Name = ""
    Amount = ""
    PurchaseDate = None
    def InvestmentInfo(self):
        print("Company on Stock Exchange")

class TermDeposit(Investment):
    
    interestRate = 0.01
    def InvestmentInfo(self):
        print("Term Deposit in a Bank")

class InvestmentFactory():
    
    def createInvestment(self, invest):
        if (invest in investmentType):
            return investmentType[invest]()
        return None

investmentType = {
    "termdeposit" : TermDeposit,
    "stockexchange" : StockExchange,
}

class FactoryPatternDemo(PatternDemo):
    @staticmethod
    def PatternInfo():
        PatternDemo.PatternInfo()
        print "This is an example of Factory Design Pattern"
    
    def PatternRun(self):
        factory = InvestmentFactory();
        investments = ["termdeposit", "stockexchange", "stockexchange", "termdeposit", "none"]
        
        for a in investments:
            temp = factory.createInvestment(a)
            if (temp != None):
                temp.InvestmentInfo()
