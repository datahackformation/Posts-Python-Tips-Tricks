
# Es necesario una versión de numpy < 1.20.0 e instalar pyarrow.

import pandas as pd 
import os

df = pd.read_csv('original.csv', sep=',')
df.reset_index(drop=True).to_feather('new.feather')

csv = round(os.stat('original.csv').st_size/1e+9,3)
feather = round(os.stat('new.feather').st_size/1e+9,3)

print(
    f'''
    Comparación del tamaño de archivos: \n
    Size CSV: {csv} GB
    Size Feather: {feather} GB
    '''
)
