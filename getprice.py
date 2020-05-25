import pandas as pd


dfg = pd.read_csv('Henry_Hub_Natural_Gas_Spot_Price.csv', skiprows=4)
dfg.index = pd.to_datetime(dfg["Day"],format='%m/%d/%Y')
dfg.to_csv('gaspricedaily.csv', index=False ,header=["Day","Price"])

dfg_month = dfg['Henry Hub Natural Gas Spot Price Dollars per Million Btu'].resample('M').sum()
df = pd.DataFrame(dfg_month, index=dfg_month.index.strftime("%d/%m/%Y"))
df.to_csv('gaspricemonthly.csv', index=True,header=["Price"])  
