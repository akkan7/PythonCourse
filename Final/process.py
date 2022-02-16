import pandas as pd
import numpy as np

a = np.array(pd.read_csv("fshib.csv"))
ag = np.array(pd.read_csv("googleshiba.csv"))
ap = np.array(pd.read_csv("priceshib.csv"))
ab = np.array(pd.read_csv("pricebtc.csv"))

kl = pd.DataFrame(a, columns=['a', 'Date', 'Tweets'])
klg = pd.DataFrame(ag, columns=['Date', 'Google','?'])
klp = pd.DataFrame(ap, columns=['Date', 'low','high','open','close','vfrom','vto'])
klb = pd.DataFrame(ab, columns=['Date', 'low','high','BTCopen','close','vfrom','vto'])

kl=kl[::-1]
kl.drop('a', axis=1, inplace=True)
klg=klg.drop_duplicates(subset=['Date'])
klg.drop('?', axis=1, inplace=True)
klp.drop(['low','high','close','vfrom','vto'], axis=1, inplace=True)
klb.drop(['low','high','close','vfrom','vto'], axis=1, inplace=True)

kl=kl.set_index('Date')
klg=klg.set_index('Date')
klp=klp.set_index('Date')
klb=klb.set_index('Date')

kl=kl.join(klg)
kl=kl.join(klp)
kl=kl.join(klb)
kl = kl.reset_index()

print(kl)
print(kl.isnull().sum())

#kl.Date= kl.Date.apply(lambda x: datetime.timestamp(datetime.strptime(x, "%Y-%m-%d %H:%M:%S") ))



kl.to_csv('datashiba.csv')


###BUSD

a = np.array(pd.read_csv("fbusd.csv"))
ag = np.array(pd.read_csv("googlebusd.csv"))
ap= np.array(pd.read_csv("pricebusd.csv"))

kl = pd.DataFrame(a, columns=['a', 'Date', 'Tweets'])
klg = pd.DataFrame(ag, columns=['Date', 'Google','?'])
klp = pd.DataFrame(ap, columns=['Date', 'low','high','open','close','vfrom','vto'])

kl=kl[::-1]
kl.drop('a', axis=1, inplace=True)
klg=klg.drop_duplicates(subset=['Date'])
klg.drop('?', axis=1, inplace=True)
klp.drop(['low','high','close','vfrom','vto'], axis=1, inplace=True)

kl=kl.set_index('Date')
klg=klg.set_index('Date')
klp=klp.set_index('Date')

kl=kl.join(klg)
kl=kl.join(klp)
kl=kl.join(klb)
kl = kl.reset_index()

print(kl)
print(kl.isnull().sum())
#kl.Date= kl.Date.apply(lambda x: datetime.timestamp(datetime.strptime(x, "%Y-%m-%d %H:%M:%S") ))
kl.to_csv('databusd.csv')

###NEAR

a = np.array(pd.read_csv("fnear.csv"))
ag = np.array(pd.read_csv("googlenear.csv"))
ap= np.array(pd.read_csv("pricenear.csv"))

kl = pd.DataFrame(a, columns=['a', 'Date', 'Tweets'])
klg = pd.DataFrame(ag, columns=['Date', 'Google','?'])
klp = pd.DataFrame(ap, columns=['Date', 'low','high','open','close','vfrom','vto'])

kl=kl[::-1]
kl.drop('a', axis=1, inplace=True)
klg=klg.drop_duplicates(subset=['Date'])
klg.drop('?', axis=1, inplace=True)
klp.drop(['low','high','close','vfrom','vto'], axis=1, inplace=True)

kl=kl.set_index('Date')
klg=klg.set_index('Date')
klp=klp.set_index('Date')

kl=kl.join(klg)
kl=kl.join(klp)
kl=kl.join(klb)
kl = kl.reset_index()

print(kl)
print(kl.isna().sum())

#kl.Date= kl.Date.apply(lambda x: datetime.timestamp(datetime.strptime(x, "%Y-%m-%d %H:%M:%S") ))


kl.to_csv('datanear.csv')
