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
""" this is an example of template design pattern """

from abc import ABCMeta, abstractmethod
from patterndemo import PatternDemo
import datetime
from locale import currency
from random import randint

class InvestmentTemplate:
    """ this class is a template class and implements
    the core of Template design pattern """
    __metaclass__ = ABCMeta
    purchaseDate = None
    sellDate = None
    purchasePrice = 0
    currentPrice = 0
    sellPrice = 0
    securityName = None
    @abstractmethod
    def investment_info(self):
        pass
    @abstractmethod
    def investment_buy(self):
        pass
    @abstractmethod
    def InvestmentSell(self):
        pass
    @abstractmethod
    def InvestmentShowValue(self):
        pass
    @abstractmethod
    def InvestmentGetValue(self):
        pass
    def InvestmentCreate(self):
        self.InvestmentGetValue()
        self.investment_buy()
    def InvestmentDelete(self):
        self.investment_info()
        self.InvestmentShowValue()
        self.InvestmentSell()

class StockExchange(InvestmentTemplate):
    Amount = 0
    def __init__(self, name, amount):
        self.securityName = name
        self.purchaseDate = datetime.date.today()
        self.Amount = amount
    def investment_info(self):
        print"StockEx Company {} purchased on {}".format(self.securityName, self.purchaseDate)
    def investment_buy(self):
        print "StockEx Buying: {}".format(self.securityName)
    def InvestmentSell(self):
        print "StockEx Selling: {}".format(self.securityName)
    def InvestmentShowValue(self):
        print "StockEx Gain is: {}".format(self.Amount*(self.purchasePrice - self.currentPrice))
    def InvestmentGetValue(self):
        print "\nStockEx Price is: {}".format(self.currentPrice)

class GiltEdgedSecurities(InvestmentTemplate):
    Amount = 0
    def __init__(self, name, amount):
        self.securityName = name
        self.purchaseDate = datetime.date.today()
        self.Amount = amount
    def investment_info(self):
        print"Bond: {} purchased on {}".format(self.securityName, self.purchaseDate)
    def investment_buy(self):
        print"Bond Buying {}".format(self.securityName)
    def InvestmentSell(self):
        print"Bond Selling {}".format(self.securityName)
    def InvestmentShowValue(self):
        print "Bond Gain is: {}".format(self.Amount*(self.purchasePrice - self.currentPrice))
    def InvestmentGetValue(self):
        print"\nBond Price is: {}".format(self.currentPrice)

class TermDeposit(InvestmentTemplate):
    currency = currency
    interestRate = 0.01
    Amount = 0
    def __init__(self, name, amount):
        self.securityName = name
        self.purchaseDate = datetime.date.today()
        self.Amount = amount
    def investment_info(self):
        print "Term Deposit in a Bank, interest {} for {}".format(self.interestRate, self.Amount)
    def investment_buy(self):
        print "Term Deposit Buying {}".format(self.securityName)
    def InvestmentSell(self):
        print "Term Deposit Selling {}".format(self.securityName)
    def InvestmentShowValue(self):
        print "Term Deposit Gain is: {}".format(self.Amount*(self.purchasePrice \
                                                             - self.currentPrice))
    def InvestmentGetValue(self):
        print "\nTerm Deposit Price is: {}".format(self.currentPrice)

class InvestmentFactory():
    def createInvestment(self, invest, name, amount):
        if invest in investmentType:
            return investmentType[invest](name, amount)
        return None

investmentType = {
    "termdeposit" : TermDeposit,
    "stockexchange" : StockExchange,
    "giltedgedsecurity": GiltEdgedSecurities,
}

class TemplatePatternDemo(PatternDemo):
    """ This class inherits after PatternDemo and runs the demo """
    @staticmethod
    def pattern_info():
        PatternDemo.pattern_info()
        print "This is an example of Template Design Pattern"
    def pattern_run(self):
        factory = InvestmentFactory()
        investments = ["termdeposit", "stockexchange", \
                       "stockexchange", "giltedgedsecurity", "termdeposit", "none"]
        for a in investments:
            temp = factory.createInvestment(a, "AA", str(randint(0, 100)))
            if temp != None:
                temp.InvestmentCreate()
                temp.InvestmentDelete()
