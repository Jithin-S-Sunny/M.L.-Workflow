# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:51:19 2021

@author: J. Sunny
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
f=open('out.txt','w')
features=pd.read_csv('4glm.csv')
x=features.head(5)
print(x)
#y=features.describe()
#print(y, file=f)
#f.close()
labels=np.array(features['target'])
features=features.drop('target', axis=1)
feature_list = list(features.columns)
features = np.array(features)
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)
baseline_preds = test_features[:, feature_list.index('ip')]
baseline_errors = abs(baseline_preds - test_labels)
print('Average baseline error: ', round(np.mean(baseline_errors), 2))
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(train_features, train_labels);
predictions = rf.predict(test_features)
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
mape = 100 * (errors / test_labels)
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')