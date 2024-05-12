# -*- coding: utf-8 -*-
"""cdss3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G7y3-5qrqbyaZs6w4hFHTg4N0k_JAOMR
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Clone the repository containing the dataset
!git clone https://github.com/imharshitaa/Clinical-Decision-Support-System-Healthcare-EPICS-project.git

# Assuming the dataset file is in CSV format, you can use pandas to load it
di = pd.read_csv("Clinical-Decision-Support-System-Healthcare-EPICS-project/data/diabetes.csv")

# Drop the 'Index' column
di.drop(columns=['Age'], inplace=True)

# Replace NaN values with 0
di.fillna(0, inplace=True)

# Now you can work with the modified dataset
print(di.head())



di.head()
di.info()
di.describe()
di.isnull().sum()
di['Insulin'].value_counts()
di['SkinThickness'].value_counts().head()

sns.jointplot(x='Insulin',y='SkinThickness',data=di,kind='reg')

di.corr()

p=0
q=0
for i in range(len(di['Insulin'])):
    if di['Insulin'][i]==0 and di['SkinThickness'][i]!=0:
        p+=1
print(p)


p=int(di['Insulin'][di['Insulin']<400].mean())

di['SkinThickness'].replace(0,int(di['SkinThickness'].mean()),inplace=True)

di['Insulin'].replace(0,p,inplace=True)

di.head()

from sklearn.model_selection import train_test_split
xtr, xte, ytr, yte = train_test_split(di.drop('Outcome',axis=1),di['Outcome'],test_size=0.50)

ytr

from sklearn.linear_model import LogisticRegression

logmodel=LogisticRegression()
logmodel.fit(xtr,ytr)

predictions = logmodel.predict(xte)

from sklearn.metrics import confusion_matrix

accuracy = confusion_matrix(yte,predictions)
accuracy

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(yte,predictions)
accuracy

from sklearn.ensemble import RandomForestClassifier

clf=RandomForestClassifier(n_estimators=100)

clf.fit(xtr,ytr)

ypr=clf.predict(xte)

from sklearn import metrics
print('Accuracy  :',metrics.accuracy_score(yte,ypr))
sns.pairplot(hue='Outcome',kind='scatter',data=di)