import pandas as pd 

df = pd.read_csv('CO2_Emissions_Canada.csv')

#duplicated data
df_duplicated = df[df.duplicated() == True]
indexs = df_duplicated.index
for i in indexs:
   df.drop(i, axis = 0,inplace = True)
df2 = df[df.duplicated() == True]
