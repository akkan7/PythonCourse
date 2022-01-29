import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


d = pd.read_csv("cses4_cut.csv")
y=np.array(d['voted'])
y=y.astype('int')

### I use ordered and categorical values- D2020 Household income,  d2003 education, d2023 religiosity, d2029 residence
#clean data from unwanted values, the missing answers to the question.
from sklearn import preprocessing

#ordered ones
x = np.array(d[['D2003', 'D2020', 'D2023', 'D2029']])
x=x.astype('float')
x[x>=6]=np.nan

from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
x = imp.fit_transform(x)

#scaling ordered ones
sc = preprocessing.StandardScaler()
x = sc.fit_transform(x)



#categorical ones,  D2005 union membership D2013 employment type d2004 marital status
x2 = np.array(d[['D2004', 'D2005', 'D2013']])
x2=x2.astype('float')
x2[x2>=6]=np.nan

### using scikit to manage missing data  https://scikit-learn.org/stable/modules/impute.html
#I think using mean in a not ordered variable is confusing, using the most frequent may better randomize it.
imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
x2 = imp.fit_transform(x2)

#one-hot encoding to deal with categorical variables, which creates new variables for each category
enc = preprocessing.OneHotEncoder()
enc.fit(x2)
x2onehot = enc.transform(x2).toarray()


#merging explanatory variables
X = np.concatenate((x, x2onehot), axis=1)

#feature selection
#https://scikit-learn.org/stable/modules/feature_selection.html, chi was giving a value error, I used f_classif

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif


X = SelectKBest(f_classif, k=7).fit_transform(X, y)

#splitting into train and test
from sklearn import model_selection as ms

xtrain, xtest, ytrain, ytest = ms.train_test_split(X,y, test_size=0.33, random_state=42)


from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

kneigh = KNeighborsClassifier()
dtree = DecisionTreeClassifier()
sv = svm.SVC()
gn = GaussianNB()
lr = LogisticRegression()

# Cross Validation check for possible models

KCV = ms.cross_val_score(kneigh, xtrain, ytrain, cv=5).mean()
DCV = ms.cross_val_score(dtree, xtrain, ytrain, cv=5).mean()
SCV= ms.cross_val_score(sv, xtrain, ytrain, cv=5).mean()
GCV= ms.cross_val_score(gn, xtrain, ytrain, cv=5).mean()
LCV= ms.cross_val_score(lr, xtrain, ytrain, cv=5).mean()

print("Cross Validation Scores (5-fold) Follow as:  \nKNeigbors : ", KCV, "\nDecision Tree: ", DCV,
      "\nSupport Vector Machine:", SCV, "\nGaussian Naive Bayes:", GCV,"\nLogistic Regression:", LCV )




#Best Scores came from Support Vector Machine and Logistic Regression
#Now use these two while optimizing the models. Using GridSearch
from sklearn.model_selection import GridSearchCV


#Support Vector Machine

sv.fit(xtrain, ytrain)
SVpredict = sv.predict(xtest)
print("Accuracy score for Support vector machine with default settings is ->", accuracy_score(ytest, SVpredict))


sv = svm.SVC()
param = {'C': [1, 10],
              'gamma': [0.001, 0.01, 1]}
grid1 = GridSearchCV(estimator=sv, param_grid=param)
grid1.fit(xtrain, ytrain)
# summarize the results of the grid search
print("Best optimized score for Support Vector Machine: ",grid1.best_score_)
print("Best parameters for Support vector machine: ", grid1.best_params_)

sv = svm.SVC(C= 1, gamma= 0.001)
sv.fit(xtrain, ytrain)
SVpredict = sv.predict(xtest)
print("Accuracy score for Support vector machine with best settings is ->", accuracy_score(ytest, SVpredict))

#confusion matrix
from sklearn.metrics import confusion_matrix
m = confusion_matrix(ytest, SVpredict)
sns.heatmap(m, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()


# Logistic Regression


lr.fit(xtrain, ytrain)
LRpredict = lr.predict(xtest)
print("Accuracy score for Logistic Regression with default settings is ->", accuracy_score(ytest, LRpredict))


#Found parameter set that will be checked, from the internet.
param = {'C' :np.logspace(-4, 4, 20)}

#I was getting an error, I found this new lr definition which solves it and deleting penalty option from grid

lr= LogisticRegression(max_iter=1000)
grid2 = GridSearchCV(estimator=lr, param_grid=param, error_score='raise')
grid2.fit(xtrain, ytrain)
# summarize the results of the grid search
print("Best optimized score for Logistic Regression: ", grid2.best_score_)
print("Best parameters for Logistic Regression: ", grid2.best_params_)

lr= LogisticRegression(C= 0.0001, max_iter=1000)
lr.fit(xtrain, ytrain)
LRpredict = lr.predict(xtest)
print("Accuracy score for Logistic Regression with best settings is ->", accuracy_score(ytest, LRpredict))
# Weirdly, optimized logistic regression has less accuracy score, I do not understand it.

#confusion matrix
m2 = confusion_matrix(ytest, LRpredict)
sns.heatmap(m2, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()




