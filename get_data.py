# make a csv file that contains some stock data

import tushare as ts

angang = ts.get_h_data('000898', start='2016-01-01')
angang.to_csv('data/000898.csv')
