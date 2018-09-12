# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
# Take all columns except last one
X = dataset.iloc[:, :-1].values
# Take only column3
y = dataset.iloc[:, 3].values


# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
# 1:3 means 1<=columns<3, not 2
imputer= imputer.fit(X[:, 1:3])
# X replace by means of column
X[:, 1:3] =imputer.transform( X[:, 1:3] ) 


# Encoding categorial data
# Replace string by categories number
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
# Create columns with dummy variables to replace number after label encoder
onehotencoder = OneHotEncoder(categorical_features= [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
# Replace Yes, No by numbers
y = labelencoder_Y.fit_transform(y)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
# Standardization and Normalization 
# Fit calculate parameter about mean and standard
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
