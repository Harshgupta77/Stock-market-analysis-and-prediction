# -*- coding: utf-8 -*-
"""Stock Market Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l9KsKmhDFpwYxKd038F0JRkcXhOpMzPT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
plt.style.use('bmh')

from google.colab import files
uploaded = files.upload()

df=pd.read_csv('VZ.csv')

df.head()

df.tail()

print("Checking if any null values are present\n", df.isna().sum())

plt.figure(figsize=(16,8))
plt.title('VZ')
plt.xlabel('Days')
plt.ylabel('Close Price')
plt.plot(df['Close'])
plt.show()

df=df[['Close']]
future_days=25
df['Prediction']=df[['Close']].shift(-future_days)
X=np.array(df.drop(['Prediction'],1))[:-future_days]
y=np.array(df['Prediction'])[:-future_days]

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size =0.25)

tree=DecisionTreeRegressor().fit(x_train,y_train)
lr=LinearRegression().fit(x_train,y_train)
svm=SVR(kernel='rbf',C=1e3,gamma=0.1).fit(x_train,y_train)

svm_confidence=svm.score(x_test,y_test)
tree_confidence=tree.score(x_test,y_test)
lr_confidence=lr.score(x_test,y_test)
print("The accuracy of all the models:")
print("SVM Model \t\t\t",svm_confidence)
print("Decision Model \t\t\t",tree_confidence)
print("Linear Regression Model \t",lr_confidence)

x_future=df.drop(['Prediction'],1)[:-future_days]
x_future=x_future.tail(future_days)
x_future=np.array(x_future)
x_future

tree_predict=tree.predict(x_future)
lr_predict=lr.predict(x_future)
svm_predict=svm.predict(x_future)
print(svm_predict)
print(lr_predict)
print(svm_predict)

predictions=svm_predict
valid=df[X.shape[0]:]
valid['Prediction']=predictions
plt.figure(figsize=(16,8))
plt.title('SVM Model')
plt.xlabel('Days')
plt.ylabel('Close Price in USD($)')
plt.plot(df['Close'])
plt.plot(valid[['Close','Prediction']])
plt.legend(['Orig','Val', 'Pred'])
plt.show()

predictions=lr_predict
valid=df[X.shape[0]:]
valid['Prediction']=predictions
plt.figure(figsize=(16,8))
plt.title('Linear Regression Model')
plt.xlabel('Days')
plt.ylabel('Close Price in USD($)')
plt.plot(df['Close'])
plt.plot(valid[['Close','Prediction']])
plt.legend(['Orig','Val', 'Pred'])
plt.show()

predictions=tree_predict
valid=df[X.shape[0]:]
valid['Prediction']=predictions
plt.figure(figsize=(16,8))
plt.title('Decision Tree Model')
plt.xlabel('Days')
plt.ylabel('Close Price in USD($)')
plt.plot(df['Close'])
plt.plot(valid[['Close','Prediction']])
plt.legend(['Orig','Val', 'Pred'])
plt.show()