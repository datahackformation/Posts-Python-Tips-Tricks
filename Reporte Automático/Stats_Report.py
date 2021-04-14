'''
Pandas Profiling
https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/index.html
'''

import pandas as pd
import pandas_profiling

csv = 'https://raw.githubusercontent.com/matplotlib/sample_data/master/aapl.csv'

df = pd.read_csv(csv, sep=',')
report = df.profile_report(title='My report')
report.to_file('final_report.html')

