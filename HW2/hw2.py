import wbdata
import pandas
import numpy as np
import MyReg
import matplotlib.pyplot as plt
import seaborn
from sklearn import linear_model


#print(wbdata.get_indicator(source=24))

countries = [i['id'] for i in wbdata.get_country(country_id=("TUR"))]

vars = {"NY.GDP.PCAP.PP.KD": "GDP per capita", "SI.POV.GINI":"Gini inequality index"}

datas = wbdata.get_dataframe(vars, country=countries)

# Get rid of na values
datas.dropna(inplace=True)
#The data is incontinous at 1994 and starts again later, which create a discrepancy since Turkey's economy was transformed inbetween
datas.drop("1994", inplace=True)


#get a 1's column somewhere to capture b0

#  I make GDPCC in thousand $ so the regression coefficient and s.dev is easier for us to evaluate and understand
datas["GDP per capita"]=datas["GDP per capita"].div(1000)
print(datas)

datas.to_csv('HW2RegressionData.csv')
#locate x and y
y = np.array(datas.iloc[:,1]).reshape(-1,1)
x = np.vstack((np.ones((y.shape[0])), np.array(datas.iloc[:,0])))
x=x.T


results= MyReg.myreg(x,y)
print(results)
print("The regression fitted as gini = ", results[0][0], "+", results[0][1], " * gdp")
print("The standard errors are, respectively, ", results[1])
print("My reg coefficient is not statistically significant as the conf interval contains 0: ",results[2][0][1],"-", results[2][1][1])

#now we can visualize the results by using seaborn

graph= seaborn.lmplot(x= "GDP per capita", y="Gini inequality index", data=datas)
plt.title("GDP per capita against the income inequality")
plt.savefig("GDPCC-Gini-Regression")
plt.show()
plt.close()


#bonus
print("For the bonus, I have imported linear_model from sklearn library, to check my results")
lm = linear_model.LinearRegression()
model = lm.fit(x,y)
print("B1 is ", lm.coef_, "and B0 is ", lm.intercept_)






