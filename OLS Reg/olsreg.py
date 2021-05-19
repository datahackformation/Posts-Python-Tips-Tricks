

import statsmodels.api as sm
import numpy as np
import pandas as pd

df = pd.read_csv('data.csv', delimiter=';')
df.drop('marca', axis=1, inplace=True)

Y = df['precio']
X = df[[col for col in df.columns if col != 'precio']]
X = sm.add_constant(X)

model = sm.OLS(Y, X)
results = model.fit()

print(results.summary())

