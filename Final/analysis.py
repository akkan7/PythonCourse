
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler



#--------------------
#SHIBA operations

shiba = pd.read_csv("datashiba.csv")


#We form x and y
ys=np.array(shiba['open'])
ys=ys.astype('float')
ys=ys.reshape(-1,1)
xs = np.array(shiba[['Tweets', 'Google', 'BTCopen']])
xs=xs.astype('float')

#We use MinMaxScaler

sc = MinMaxScaler()
xs = sc.fit_transform(xs)
ys = sc.fit_transform(ys)

ys=np.ravel(ys)

##We are checking for stationary data by utilizing Augmented Dickey-Fuller
import statsmodels.api as sm

d = sm.tsa.stattools.adfuller(ys)
print('\n')
print('\033[1m' + 'Results 1 Shiba' + '\033[0m')
print('ADF Statistic : %f' % d[0])
print('p-value: %f' % d[1])
print('Critical Values:')
for key, value in d[4].items():
    print('\t%s: %.3f' % (key, value))

    # create a differenced series, model from machinelearningmastery.com, to make data stationary
def difference(dataset, interval=1):
    diff = list()
    diff.append(0)
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return diff

ys=difference(ys)

#Checking again for stationarity after differencing
d = sm.tsa.stattools.adfuller(ys)
print('\n')
print('\033[1m' + 'Results 2 Shiba' + '\033[0m')
print('ADF Statistic : %f' % d[0])
print('p-value: %f' % d[1])
print('Critical Values:')
for key, value in d[4].items():
    print('\t%s: %.3f' % (key, value))



 ##Train Test Split, customized for time series cut point 5 days=120 hours vs 25 days of training

trainx = xs[0:600,:]
testx = xs[600:,:]

trainy = ys[0:600]
testy = ys[600:]

#MLP Regressor to incorporate exogenous variables and time series in a neural network
#We also used GridSearch to optimize model as much as we can


mlp=MLPRegressor(max_iter=5000, solver= 'lbfgs')
param_list = {"hidden_layer_sizes": [(1,),(50,)], "activation": ["identity", "logistic", "tanh", "relu"], "alpha": [0.00005,0.0005,0.0001]}
gridCV = GridSearchCV(estimator=mlp, param_grid=param_list)
gridCV.fit(trainx, trainy)
predicted = gridCV.predict(testx)
parameters = mlp.get_params()
print("Grid Best Parameters: ", parameters)

#Train and predict
regr = MLPRegressor(random_state=1, max_iter=10000, activation= 'relu').fit(trainx, trainy)
predshib = regr.predict(testx)


#Plot the resulting predictions against actual data
plt.clf()
plt.plot(predshib)
plt.plot(testy, color='red')
plt.xlabel('Next hours')
plt.ylabel('Price of SHIB')
plt.title("Prediction of $SHIB- MLP")

plt.savefig('shibpredMLP-ST.png')

#Statistical checks

print("RMSE for MLP SHIB: ", mean_squared_error(testy, predshib,squared=False))

print("R2 for MLP SHIB: ", r2_score(testy, predshib))

###SARIMAX model. We used SARIMAX to both use a statistical model with lags and moving average, along with exogenous variables

from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
model = SARIMAX(trainy, exog=trainx, order=(1, 1, 1), seasonal_order=(0, 0, 0, 0))
model_fit = model.fit(disp=False)
ypred=[]
for i in range(0,120):
    a= model_fit.predict(len(trainy), len(trainy), exog=(testx[i].reshape(1,-1)))
    ypred.append(a)

plt.clf()
plt.plot(ypred)
plt.plot(testy, color='red')

plt.xlabel('Next hours')
plt.ylabel('Price of SHIB')
plt.title("Prediction of $SHIB- SARIMAX")

plt.savefig('shibpredSARIMAX-ST.png')
print("RMSE for SARIMAX SHIB: ", mean_squared_error(testy, ypred,squared=False))
print("R2 for SARIMAX SHIB: ", r2_score(testy, ypred))


#--------------------
#NEAR operations

near = pd.read_csv("datanear.csv")


sc = preprocessing.MinMaxScaler()


yn=np.array(near['open'])
yn=yn.reshape(-1,1)
yn=yn.astype('float')
xn = np.array(near[['Tweets', 'Google', 'BTCopen']])
xn=xn.astype('float')


xn = sc.fit_transform(xn)
yn = sc.fit_transform(yn)


yn=np.ravel(yn)

##We are checking for stationary data by utilizing Augmented Dickey-Fuller


d2 = sm.tsa.stattools.adfuller(yn)
print('\n')
print('\033[1m' + 'Result 1 Near' + '\033[0m')
print('ADF Statistic : %f' % d2[0])
print('p-value: %f' % d2[1])
print('Critical Values:')
for key, value in d2[4].items():
    print('\t%s: %.3f' % (key, value))

##Differencing
yn=difference(yn)

d2 = sm.tsa.stattools.adfuller(yn)
print('\n')
print('\033[1m' + ' Result 2 Near' + '\033[0m')
print('ADF Statistic : %f' % d2[0])
print('p-value: %f' % d2[1])
print('Critical Values:')
for key, value in d2[4].items():
    print('\t%s: %.3f' % (key, value))


##Train Test Split, customized for time series cut point 5 days=120 hours vs 25 days of training
trainxn = xn[0:600,:]
testxn = xn[600:,:]

trainyn = yn[0:600]
testyn = yn[600:]

##MLP REGressor
mlp=MLPRegressor(max_iter=5000, solver= 'lbfgs')
param_list = {"hidden_layer_sizes": [(1,),(50,)], "activation": ["identity", "logistic", "tanh", "relu"], "alpha": [0.00005,0.0005,0.0001]}
gridCV = GridSearchCV(estimator=mlp, param_grid=param_list)
gridCV.fit(trainxn, trainyn)
predicted = gridCV.predict(testxn)
parameters = mlp.get_params()
print("Grid Best Parameters: ", parameters)

regr = MLPRegressor(random_state=1, max_iter=10000, activation= 'relu').fit(trainx, trainy)
prednear = regr.predict(testxn)

plt.clf()
plt.plot(prednear)
plt.plot(testyn, color='red')
plt.xlabel('Next hours')
plt.ylabel('Price of $NEAR')
plt.title("Prediction of $NEAR- MLP")

plt.savefig('nearpredMLP-ST.png')
print("RMSE for MLP NEAR: ", mean_squared_error(testyn, prednear,squared=False))
print("R2 for MLP NEAR: ", r2_score(testyn, prednear))
###SARIMAX

model2 = SARIMAX(trainyn, exog=trainxn, order=(1, 1, 1), seasonal_order=(0, 0, 0, 0))
model2_fit = model2.fit(disp=False)
ypred2=[]
for i in range(0,120):
    a= model2_fit.predict(len(trainyn), len(trainyn), exog=(testxn[i].reshape(1,-1)))
    ypred2.append(a)


plt.clf()
plt.plot(ypred2)
plt.plot(testyn, color='red')

plt.xlabel('Next hours')
plt.ylabel('Price of Near')
plt.title("Prediction of $NEAR- SARIMAX")
plt.savefig('nearpredSARIMAX-ST.png')

print("RMSE for SARIMAX NEAR: ", mean_squared_error(testyn, ypred2,squared=False))
print("R2 for SARIMAX NEAR: ", r2_score(testyn , ypred2))
