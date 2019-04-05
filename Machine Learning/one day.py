import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
dataset = pd.read_csv('/home/wlb/Desktop/100-Days-Of-ML-Code/datasets/Data.csv')
X = dataset.iloc[:,:].values
Y = dataset.iloc[:,:-1].values
imputer = Imputer(missing_values="NaN",strategy='mean',axis=0)
imputer = imputer.fit(X[:,1:3])

X[:,1:3] = imputer.transform(X[:,1:3])
print(X[:,1:3])