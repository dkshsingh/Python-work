# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:14:53 2022

@author: singh
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

#loading the diabetes dataset to a pandas Dataframe
diabetes_dataset = pd.read_csv("C:\\Users\singh\OneDrive\Desktop\Shape-my-skills\diabetes.csv")
diabetes_dataset.head()

#number of rows and columns in this dataset
diabetes_dataset.shape

#getting the statical measures of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()


# 0 --> Non-diabetic 1 --> diabetic
diabetes_dataset.groupby('Outcome').mean()

#seperating data and labels
X = diabetes_dataset.drop(columns='Outcome',axis=1)
Y = diabetes_dataset['Outcome']

print(X)

print(Y)

#train test split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

#training the model
classifier = svm.SVC(kernel='linear')
                     
#training the support vector machine classifier
classifier.fit(X_train,Y_train)


#model evaluation
#accuracy score

#accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print('accuracy score of the training data:',training_data_accuracy)

#making a predictive system
input_data = (1,85,66,29,0,26.6,0.351,31)

#changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
    print('The person is not diabetic')
else:
    print('The person is diabetic')


input_data=(6,148,72,35,0,33.6,0.627,50)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
    print('The person is not diabetic')
else:
    print('The person is diabetic')





