
"""
Es necesario instalar Plotly en Python :)
https://plotly.com/
"""

import plotly.graph_objects as go
import pandas as pd

url = 'https://raw.githubusercontent.com/datahackformation/Posts-Python-Tips-Tricks/main/Bubble%20Map/ciudades.csv'
df = pd.read_csv(url, sep=';')

df['text'] = df['city'] + '<br>Población ' + (round(df['population']/1e6, 2)).astype(str) + ' millones'
limits = [(0,2), (3,10),(11,20),(21,50),(50,3000)]
colors = ['royalblue', "crimson","lightseagreen","orange","lightgrey"]
cities = list()
scale = 10000

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'ISO-3',
        lon = df_sub['lng'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = {
            'size': df_sub['population']/scale,
            'color': colors[i],
            'line_color': 'rgb(40,40,40)',
            'line_width': 0.3,
            'sizemode': 'area'
        },
        hovertemplate='%{text}',
        name = ''))

fig.update_layout(
        title_text = 'Población en ciudades<br>de Sudamérica',
        showlegend = False,
        legend_title="Número por grupo",
        geo = {
            'scope': 'south america',
            'landcolor': 'rgb(217, 217, 217)'
            }
)

fig.show()
fig.write_html('southMap.html')
