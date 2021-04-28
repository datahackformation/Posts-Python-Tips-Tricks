

import pandas as pd, numpy as np
import matplotlib.pyplot as plt, seaborn as sns

url = 'https://raw.githubusercontent.com/datahackformation/Posts-Python-Tips-Tricks/main/Heatmap/titanic.csv'
df = pd.read_csv(url, sep=';').set_index('PassengerId')

df = pd.get_dummies(df, columns=['Pclass'])
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# --> Heatmap
plt.figure(figsize=(16, 6))
mask = np.triu(np.ones_like(df.corr(), dtype=np.bool))

sns.heatmap(
    df.corr(), 
    mask=mask, 
    vmin=-1, 
    vmax=1, 
    annot=True, 
    cmap='rocket'
)
