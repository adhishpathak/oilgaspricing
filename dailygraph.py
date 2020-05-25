from datetime import datetime 
import matplotlib.pyplot as plt
import csv
import numpy as np

dates=[]
prices=[]
with open('gaspricemonthly.csv', 'r') as f:
	data = csv.reader(f)
	next(data)
	for row in data:
		dates.append(row[0])
		prices.append(float(row[1]))
date_list = [datetime.strptime(date, "%d/%m/%Y").date() for date in dates]
plt.plot(date_list,prices)
plt.title('Henry Hub Natural Gas Spot Price')
plt.xlabel('Year')
plt.ylabel('Dollars per Million Btu')
plt.show()
