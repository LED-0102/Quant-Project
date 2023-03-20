import pandas
import numpy

led = pandas.read_csv('stocks_data.csv')

led = led.loc[(led['p/e']<40) &(led['cagr']>=10.0) & (led['eps_2022']-led['eps_2021']>0) & (led['eps_2021']-led['eps_2020']>0)]
led['criteria'] = led['cagr']/led['p/e']
led = led.sort_values(by='criteria', ascending=False)
led.index = numpy.arange(1, len(led)+1)

led.drop('criteria', axis=1, inplace=True)

led.to_csv('preferred_stocks.csv')




