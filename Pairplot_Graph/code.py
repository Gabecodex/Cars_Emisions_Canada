import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import plotly.express as px
import plotly.graph_objects as go
import sklearn.tree as tree

df = pd.read_csv('CO2_Emissions_Canada.csv')

#duplicated data
df_duplicated = df[df.duplicated() == True]
indexs = df_duplicated.index
for i in indexs:
   df.drop(i, axis = 0,inplace = True)

cdf = df[['Engine Size(L)','Cylinders','Transmission','Fuel Type','Fuel Consumption City (L/100 km)','Fuel Consumption Hwy (L/100 km)','Fuel Consumption Comb (L/100 km)','Fuel Consumption Comb (mpg)','CO2 Emissions(g/km)']]

Transmissionn = pd.get_dummies(cdf['Transmission'])
Fuel_Type = pd.get_dummies(cdf['Fuel Type'])

# Concat
df2 = pd.concat((cdf, Transmissionn), axis = 1)
df2 = pd.concat((df2, Fuel_Type), axis = 1)

# Drop
df2 = df2.drop(['Transmission'], axis = 1)
df2 = df2.drop(['Fuel Type'], axis = 1)

# Float Convert
df2['Z'] = df2['Z'].astype(float)
df2['X'] = df2['X'].astype(float)
df2['N'] = df2['N'].astype(float)
df2['E'] = df2['E'].astype(float)
df2['D'] = df2['D'].astype(float)
df2['M7'] = df2['M7'].astype(float)
df2['M6'] = df2['M6'].astype(float)
df2['M5'] = df2['M5'].astype(float)
df2['AV8'] = df2['AV8'].astype(float)
df2['AV7'] = df2['AV7'].astype(float)
df2['AV6'] = df2['AV6'].astype(float)
df2['AV10'] = df2['AV10'].astype(float)
df2['AV'] = df2['AV'].astype(float)
df2['AS9'] = df2['AS9'].astype(float)
df2['AS8'] = df2['AS8'].astype(float)
df2['AS7'] = df2['AS7'].astype(float)
df2['AS6'] = df2['AS6'].astype(float)
df2['AS5'] = df2['AS5'].astype(float)
df2['AS4'] = df2['AS4'].astype(float)
df2['AS10'] = df2['AS10'].astype(float)
df2['AM9'] = df2['AM9'].astype(float)
df2['AM8'] = df2['AM8'].astype(float)
df2['AM7'] = df2['AM7'].astype(float)
df2['AM6'] = df2['AM6'].astype(float)
df2['AM5'] = df2['AM5'].astype(float)
df2['A9'] = df2['A9'].astype(float)
df2['A8'] = df2['A8'].astype(float)
df2['A7'] = df2['A7'].astype(float)
df2['A6'] = df2['A6'].astype(float)
df2['A5'] = df2['A5'].astype(float)
df2['A4'] = df2['A4'].astype(float)
df2['A10'] = df2['A10'].astype(float)

df2['Cylinders'] = df2['Cylinders'].astype(float)
df2['Fuel Consumption Comb (mpg)'] = df2['Fuel Consumption Comb (mpg)'].astype(float)
df2['CO2 Emissions(g/km)'] = df2['CO2 Emissions(g/km)'].astype(float)


#plot
fig = sns.pairplot(df2, hue= 'CO2 Emissions(g/km)')
fig.savefig("out.png") 
