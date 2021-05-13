

import pandas as pd
import requests, json 

# --> Desde un archivo .json
with open('cryptodata.json') as f:
    file = json.load(f)

df1 = pd.json_normalize(file, record_path='data')

# --> Desde respuesta de API
url = 'https://api.coinlore.net/api/tickers/?start=100&limit=100'
req = requests.get(url).json()

df2 = pd.DataFrame(req['data'])

df1.head()
df2.head()
