import pandas as pd

global_gdp = pd.read_csv('global_gdp_wb.csv', sep=',"')

# PROBLEM : This dataset requires cleaning. I first need to study that more. Will be back later

print(global_gdp.head())
