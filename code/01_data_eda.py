# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:00:33 2020

@author: yg
"""

import pandas as pd
import numpy as np
dir_ = r'D:\data_compete\dacon\data\jeju-credit-card\\'
df = pd.read_csv(dir_ + "201901-202003.csv", dtype=str)
sub_df = pd.read_csv(dir_ + "submission.csv")
sub_df[["REG_YYMM","CARD_SIDO_NM","STD_CLSS_NM"]].duplicated().sum()


#%%

df

import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score

X_train = df[df["REG_YYMM"]]

def rmsle(real, predicted):
    sum=0.0
    for x in range(len(predicted)):
        p = np.log(predicted[x]+1)
        r = np.log(real[x]+1)
        sum = sum + (p - r)**2
    return (sum/len(predicted))**0.5

rmsle_score = make_scorer(rmsle, greater_is_better=False)

rf = RandomForestRegressor(random_state=1839, n_jobs=-1, verbose=2)
rf_scores = cross_val_score(rf, X_train, y_train, cv=3, scoring=rmsle_score)
print(np.mean(rf_scores))





df.info()

df["REG_YYMM"].str.len().min()
