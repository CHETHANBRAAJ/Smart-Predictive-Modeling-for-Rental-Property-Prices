# -*- coding: utf-8 -*-
"""House_price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KYo8AqFN1T4uaJldrmU6ppW2E-2NKP04
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ddf=pd.read_csv('/content/House_Rent_Train.csv')

ddf.info()

ddf.head()

ddf.columns

ddf.drop('id',axis=1)

ddf['type'].count()

ddf['type']=ddf['type'].fillna('Unknown')

ddf['type'].isnull().sum()

ddf['type'].value_counts()

ddf['activation_date'].value_counts()

ddf.drop('activation_date',axis=1)

ddf['locality'].isnull().sum()

ddf['locality']=ddf['locality'].fillna('Unknown')

ddf['amenities'].head(2
                     )

import json

import pandas as pd

# Assuming you have a DataFrame named df with an 'amenities' column
data = {'amenities': ['INTERNET','AC','CLUB','INTERCOM','POOL','CPA','FS','SECURITY','SC','GP','PARK','RWH','STP','HK','VP']}
dff = pd.DataFrame(data)

# Extract individual amenities and create new columns
amenities_split = dff['amenities'].str.split(', ', expand=True)
amenities_dummies = pd.get_dummies(amenities_split, prefix='', prefix_sep='')

# Concatenate the new columns to the original DataFrame
dff = pd.concat([dff, amenities_dummies], axis=1)

# Drop the original 'amenities' column if needed
dff = dff.drop('amenities', axis=1)

# Display the modified DataFrame
print(dff)

dff.head()

# Concatenate the columns from dff to df
df = pd.concat([ddf, dff], axis=1)

df.head()

df.columns

df['activation_date'].isnull().sum()

df=df.drop('activation_date',axis=1)

df.columns

df=df.drop('id',axis=1)

df.head()

df['latitude'].isnull().sum()

mean_lat=df['latitude'].mean()

mean_longi=df['longitude'].mean()

df['latitude']=df['latitude'].fillna(mean_lat)
df['longitude']=df['longitude'].fillna(mean_longi)

df['latitude'].isnull().sum()

df['longitude'].isnull().sum()

df['lease_type'].isnull().sum()

df['lease_type']=df['lease_type'].fillna('UNKNOWN')

df['gym'].isnull().sum()

df['lift'].isnull().sum()

df['swimming_pool'].isnull().sum()

df['negotiable'].isnull().sum()

df['HK'].isnull().sum()

df['furnishing'].isnull().sum()

df['parking'].isnull().sum()

df['property_size'].isnull().sum()

df['property_age'].isnull().sum()

df['property_age']=df['property_age'].fillna(int(0))

df['bathroom']=df['bathroom'].fillna(int(0))

df['facing'].isnull().sum()

df['property_age']=df['property_age'].fillna('UNKNOWN')

df['cup_board'].isnull().sum()

df['cup_board']=df['cup_board'].fillna(0)

df['floor'].isnull().sum()

df['floor']=df['floor'].fillna(0)

df['total_floor'].isnull().sum()

df['total_floor']=df['total_floor'].fillna(0)

df.columns

df=df.drop('amenities',axis=1)

df['water_supply'].isnull().sum()

df['water_supply']=df['water_supply'].fillna('UNKNOWN')

df['building_type'].isnull().sum()

df['building_type']=df['building_type'].fillna('UNKNOWN')

df['building_type'].isnull().sum()

df['balconies']=df['balconies'].fillna(0)

df['rent'].isnull().sum()

df['rent']=df['rent'].fillna(0)

df['facing'].isnull().sum()

df['facing']=df['facing'].fillna('UNKNOWN')

df.isnull().sum()

# encoding
from sklearn.preprocessing import OrdinalEncoder
encode = OrdinalEncoder()

df['type']=encode.fit_transform(df[['type']])

df['locality']=encode.fit_transform(df[['locality']])

df['latitude']=encode.fit_transform(df[['latitude']])

df['longitude']=encode.fit_transform(df[['longitude']])

df['lease_type']=encode.fit_transform(df[['lease_type']])

df['furnishing']=encode.fit_transform(df[['furnishing']])

df['parking']=encode.fit_transform(df[['parking']])

df['facing']=encode.fit_transform(df[['facing']])

df['water_supply']=encode.fit_transform(df[['water_supply']])

df['building_type']=encode.fit_transform(df[['building_type']])

df.info()

df.describe()

df.corr()

# prompt: find the corelation of  only floor ,total_floor , water_supply and type with respect to rent

df.corr()['rent']

df.describe()

from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy='mean')
imp.fit(df)

# train and test split
from sklearn.model_selection import train_test_split
X=df.drop('rent',axis=1)
y=df['rent']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print(f"rows in train set:{len(y_train)}\n rows in test set:{len(y_test)}")

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.fit_transform(X_test)

X_train_scaled[2]

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train_scaled)
X_test_imputed=imputer.fit_transform(X_test_scaled)

X_train_imputed[2]

y_train.iloc[2]

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from joblib import dump,load


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

model=DecisionTreeRegressor()
model.fit(X_train_imputed,y_train)
y_pred=model.predict(X_test_imputed)
mean=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("mean score:",mean)
print("R2score:",score)

model_LR=LinearRegression()
model_LR.fit(X_train_imputed,y_train)
y_pred=model_LR.predict(X_test_imputed)
mean=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("mean score:",mean)
print("R2score:",score)

model_RR=RandomForestRegressor()
model_RR.fit(X_train_imputed,y_train)
y_pred=model_RR.predict(X_test_imputed)
mean=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("mean score:",mean)
print("R2score:",score)

from sklearn.svm import SVR
model_PR = SVR(kernel = 'rbf')
model_PR.fit(X_train_imputed,y_train)
y_pred=model_PR.predict(X_test_imputed)
mean=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("mean score:",mean)
print("R2score:",score)

from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

model2=Lasso()
model2.fit(X_train_imputed,y_train)
y_pred=model2.predict(X_test_imputed)
mean2=mean_absolute_error(y_test,y_pred)
score2=r2_score(y_test,y_pred)
print("mean:",mean2)
print("r2_score:",score2)

from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
model3=Ridge()
model3.fit(X_train_imputed,y_train)
y_pred=model3.predict(X_test_imputed)
mean3=mean_absolute_error(y_test,y_pred)
score3=r2_score(y_test,y_pred)
print("mean:",mean3)
print("score3:",score3)

from sklearn.linear_model import LassoCV
lassocv=LassoCV(cv=5)
lassocv.fit(X_train_imputed,y_train)
y_pred=lassocv.predict(X_test_imputed)

mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)

from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
elastic=ElasticNet()
elastic.fit(X_train_imputed,y_train)
y_pred=elastic.predict(X_test_imputed)
mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)

from sklearn.linear_model import RidgeCV
ridgecv=RidgeCV(cv=5)
ridgecv.fit(X_train_imputed,y_train)
y_pred=ridgecv.predict(X_test_imputed)
mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)

#to save the model
from joblib import dump,load
dump(model_RR,"housing.joblib")

model=load('housing.joblib')

X_test_imputed[2]

y_test.iloc[2]

features=np.array([[-0.19727884,  0.88374445,  1.61164629, -1.10094489, -1.03576979,
       -0.55010123, -0.75282378, -0.46404203,  0.63787547,  0.35566623,
        1.26151571, -0.66285289,  1.21400665, -1.21554239,  0.85618601,
       -0.01248836, -0.40014468, -0.24989641, -0.49993017,  0.64973361,
       -1.15946865,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.       ]])

model.predict(features)