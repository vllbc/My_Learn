import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
import warnings
warnings.simplefilter("ignore")

data = pd.read_excel("./a1d1.xlsx")
a1 = data["a1"].values
d1 = data["d1"].values

day = 1
X_a1 = a1[:-day]
y_a1 = a1[day:]

X_d1 = d1[:-day]
y_d1 = d1[day:]
## a1预测
model1 = Sequential()
model1.add(Dense(12, input_dim=1, activation='relu'))
model1.add(Dense(1))
model1.compile(loss='mean_squared_error', optimizer='adam')
early_stop = EarlyStopping(monitor='loss', patience=2, verbose=1)
model1.fit(X_a1, y_a1, epochs=100, batch_size=1, verbose=1, callbacks=[early_stop], shuffle=False)

for i in range(6):
    a1 = np.append(a1, model1.predict(np.array([[a1[-1]]]))[0][0])

## d1预测
model2 = Sequential()
model2.add(Dense(12, input_dim=1, activation='relu'))
model2.add(Dense(1))
model2.compile(loss='mean_squared_error', optimizer='adam')
early_stop = EarlyStopping(monitor='loss', patience=2, verbose=1)
model2.fit(X_d1, y_d1, epochs=100, batch_size=1, verbose=1, callbacks=[early_stop], shuffle=False)

for i in range(6):
    d1 = np.append(d1, model2.predict(np.array([[d1[-1]]]))[0][0])
res = pd.DataFrame({"a1": a1, "d1": d1}).round(15)
res.to_excel("res.xlsx", index=False)