
# Es necesario instalar pyarrow, si pyarrow < 3.0.0, requiere versión numpy < 1.20.0.
# Si pyarrow >= 3.0.0, numpy >= 1.20.0 es compatible.

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
