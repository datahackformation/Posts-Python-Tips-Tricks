

import csv

values = [(1,'a', True), (2,'b', False), (3,'c', True)]
values.insert(0, ('id', 'area', 'status'))

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(values)


import pandas as pd 
df = pd.read_csv('data.csv', sep=';')

df.head()
df.info()