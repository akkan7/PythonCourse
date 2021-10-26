import random

#I use random library to pick an uniform number from the ranges specified in the instructions for stock and mutual funds


class Portfolio:
    def __init__(self):
        self.c = 0
        self.s = {}
        self.mf = {}
        self.b = {}
        self.h = []
### c for cash, s for stock, mf for mutual fund, b for bonds and h for history.

    def __str__(self):
        result = ""
        for st in self.s:
            result += str(self.s.get(st)) + " " + st + " shares \n"
        result2 = ""
        for mf in self.mf:
            result2 += str(self.mf.get(mf)) + " " + mf + " funds shares \n"
        result3 = ""
        for b in self.b:
            result3 += str(self.b.get(b)) +" " + b +" bonds\n"
        return "Portfolio has:\ncash: " + str(self.c ) + " \nStocks: " + result + "Mutualfunds: " + result2 + "Bonds: " + result3

    def __repr__(self):
        return self.__str__()

    def addcash(self, cash):
        self.c += cash
        self.h.append(["Cash", "Add", cash])

    def withdrawCash(self,cash):
        if cash< self.c:
            self.c += -cash
            self.h.append(["Cash", "Withdraw", cash])
        else:
            print("Portfolio only has "+ str(self.c) +"dollars.")

    def buyStock(self, amount, stockname):
### I assign self.s to stocks to reduce the complex representation, then reassign it to the portfolio attribute.
###same logic applies in other functions
        stocks = self.s
        if self.c >= amount * stockname.p and amount % 1==0:
            if stockname.t not in stocks:
                stocks[stockname.t] = 0
            self.h.append(["Stock", "Buy", amount, stockname.t, amount*stockname.p])
            self.c += -(amount*stockname.p)
            amount += stocks[stockname.t]
            stocks.update({stockname.t: amount})
        self.s = stocks

    def sellStock(self, amount, stockname):
        stocks = self.s
        if stocks.get(stockname.t)>= amount:
            money = (amount * stockname.p * (random.uniform(0.5,1.5)))
            self.c+= money
            self.h.append(["Stock", "Sell", amount, stockname.t, money])
            amount = stocks[stockname.t] - amount
            stocks.update({stockname.t: amount})
        else: print("The Portfolio does not have such stocks")
        self.s = stocks

    def history(self):
        print("\nHistory of Transactions follows, ordered chronologically")
        print("Type: Action: Amount: Symbol: Cash equivalent")
        a=1
        for item in self.h:
            print(str(a), end="- ")
            for i in item:
                print(i, end="  ")
            print("\n")
            a+=1
#for loop to make history of transactions more esthetic

    def buyMutualFund(self, amount, mfund):
        funds = self.mf
        if amount*mfund.p <= self.c:
            if mfund.t not in funds:
                funds[mfund.t] = 0
            self.h.append(["Mutual Fund","Buy",amount, mfund.t, amount*mfund.p ])
            self.c += -(amount*mfund.p)
            amount = funds[mfund.t]+amount
            funds.update({mfund.t: amount})
            self.mf = funds

    def sellMutualFund(self, amount, mfund):
        funds = self.mf
        if funds.get(mfund.t)>=amount:
            money = (amount * mfund.p * (random.uniform(0.9,1.2)))
            self.c += money
            amount = funds[mfund.t] - amount
            self.h.append(["Mutual Fund", "Sell", amount, mfund.t, money])
            funds.update({mfund.t: amount})
        else: print("The Portfolio does not have such mutual fund shares")
        self.mf = funds

    def sellBonds(self,bond, amount):
        bonds=self.b
        if bonds.get(bond.t)>=amount:
            self.h.append(["Bond",-amount,bonds.t])
            self.c += +(amount * bond.p * (random.uniform(0.9,1.2)))
            amount = bonds[bond.t] - amount
            bonds.update({bond.t: amount})
        else: print("The Portfolio does not have such bonds")
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
portfolio.sellMutualFund(12,mf1)
portfolio.sellStock(1, s) #Sells 1 share of HFH
portfolio.withdrawCash(250)
portfolio.withdrawCash(50)#Removes $50
portfolio.history() #Prints a list of all transactions

print(portfolio)
