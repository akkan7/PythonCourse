import random

#I use random library to pick an uniform number from the ranges specified in the instructions for stock and mutual funds


class Portfolio:
    def __init__(self):
        self.c = 0
        self.s = {}
        self.mf = {}
        self.b = {}
        self.h = []

    def __str__(self):
        result = ""
        dict = self.s
        for st in self.s:
            result += str(dict.get(st)) + " " + st + " shares \n"
        result2 = ""
        dict = self.mf
        for mf in dict:
            result2 += str(dict.get(mf)) + " " + mf + " funds shares \n"
        result3 = ""
        dict = self.b
        for b in dict:
            result3 += str(dict.get(b)) +" " + b +" bonds\n"
        return "cash: " + str(self.c ) + " \nStocks: " + result + "Mutualfunds: " + result2 + "Bonds: " + result3

    def __repr__(self):
        return self.__str__()

    def addcash(self, cash):
        self.c += cash
    def withdrawCash(self,cash):
        self.c += -cash

    def buyStock(self, amount, stockname):

        stocks = self.s
        if self.c >= amount * stockname.p and amount % 1==0:
            if stockname.t not in stocks:
                stocks[stockname.t] = 0
            self.h.append(["Stock", "Buy", amount, stockname.t])
            self.c += -(amount*stockname.p)
            amount += stocks[stockname.t]
            stocks.update({stockname.t: amount})
        self.s = stocks

    def sellStock(self, amount, stockname):
        stocks = self.s
        self.h.append(["Stock", "Sell", amount,stockname.t])
        self.c += (amount * stockname.p * (random.uniform(0.5,1.5)))
        amount = stocks[stockname.t] - amount
        stocks.update({stockname.t: amount})
        self.s = stocks

    def history(self):
        print("History of Transactions follows, ordered chronologically")
        for item in self.h:
            print(item)

    def buyMutualFund(self, amount, mutualfund):
        funds = self.mf
        if amount*mutualfund.p <= self.c:
            if mutualfund.t not in funds:
                funds[mutualfund.t] = 0
            self.h.append(["Mutual Fund","Buy",amount, mutualfund.t])
            self.c += -(amount*mutualfund.p)
            amount = funds[mutualfund.t]+amount
            funds.update({mutualfund.t: amount})
            self.mf = funds

    def sellMutualFund(self, amount, mutualfund):
        funds = self.mf
        self.h.append(["Mutual Fund", "Sell", amount, mutualfund.t])
        self.c += (amount*mutualfund.p * (random.uniform(0.9,1.2)))
        amount = funds[mutualfund.t] - amount
        funds.update({mutualfund.t: amount})
        self.mf = funds

    def sellBonds(self,bond, amount):
        bonds=self.b
        self.h.append(["Bond",-amount,bonds.t])
        self.c += +(amount * bond.p * (random.uniform(0.9,1.2)))
        amount = bonds[bond.t] - amount
        bonds.update({bond.t: amount})
        self.b = bonds


class stock:
    def __init__(self, price, name):
        self.p = price
        self.t = name
class MutualFund:
    def __init__(self, name):
        self.p = 1
        self.t = name

class Bonds(stock):
    pass



portfolio = Portfolio() #Creates a new portfolio
portfolio.addcash(300.50) #Adds cash to the portfolio
s = stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
sami= stock(20, "abc")
portfolio.buyStock(5, s) #Buys 5 shares of stock s
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2= MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.history()
portfolio.sellMutualFund(3,mf1) #Sells 3 shares of BRT
portfolio.sellStock(1, s) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50
portfolio.history() #Prints a list of all transactions