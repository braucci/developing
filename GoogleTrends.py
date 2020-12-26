import pandas as pd
import matplotlib
from pytrends.request import TrendReq

pytrends = TrendReq(hl='it-IT', tz=360)
pytrend = TrendReq(hl='it-IT', tz=360)


keywords=['Pompei']
pytrend.build_payload(
    kw_list=keywords,
    cat=0,
    timeframe='today 12-m',
    geo='IT',
    gprop='')
data = pytrend.interest_over_time()
data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')

image = data.plot(title = 'Pompei in last 12 months on Google Trends')
fig = image.get_figure()
fig.savefig('figure.png')
