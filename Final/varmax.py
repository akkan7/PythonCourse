#modelfit lineında hata veriyor VARMAX - arifin sarimaxtan drive edildi
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
shiba = pd.read_csv("datashiba.csv")
ys=np.array(shiba['open'])
ys=ys.astype('float')
ys=ys.reshape(-1,1)
xs = np.array(shiba[['Tweets', 'Google', 'BTCopen']])
xs=xs.astype('float')

sc = MinMaxScaler()
xs = sc.fit_transform(xs)
ys = sc.fit_transform(ys)

ys=np.ravel(ys)

trainx = xs[0:600,:]
testx = xs[600:,:]

trainy = ys[0:600]
testy = ys[600:]

from statsmodels.tsa.statespace.varmax import VARMAX
import matplotlib.pyplot as plt
model = VARMAX(trainy, exog=trainx, order=(1, 1))
model_fit = model.fit(disp = False)
ypred=[]
for i in range(0,119):
    a= model_fit.predict(len(trainy), len(trainy), exog=(testx[i].reshape(1,-1)))
ypred.append(a)

plt.plot(ypred)
plt.plot(testy, color='red')

plt.xlabel('Next hours')
plt.ylabel('Price of SHIB')
plt.title("Prediction of $SHIB")

plt.savefig('shibpred.png')
plt.show()
plt.close()
