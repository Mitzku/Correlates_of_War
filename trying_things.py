import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re



global_gdp = pd.read_csv('global_gdp_wb.csv', sep=',"',engine='python')
global_gdp = global_gdp.replace('"', '', regex=True)
global_gdp = global_gdp.rename(columns=lambda x: re.sub('"','',x))
global_gdd = global_gdp.rename(columns={'ï»¿Country Name':'Year'}, inplace=True)
global_gdp = global_gdp.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1)

trans = global_gdp.set_index('Year').T


trans = trans.reset_index()

cols = trans.columns.tolist()
trans[cols] = trans[cols].apply(pd.to_numeric, errors='coerce', axis=1)
trans['aggregate_gdp'] = trans.sum(axis=1)




cow_nmc = pd.read_csv('NMC_5_0.csv')
cow_nmc['aap'] = cow_nmc['milex'] + cow_nmc['milper'] + cow_nmc['irst'] + cow_nmc['pec'] + cow_nmc['tpop'] + cow_nmc['upop']
aap_by_year = cow_nmc.groupby('year')['aap'].sum().reset_index()


merged_table = pd.merge(
    aap_by_year,
    trans,
    left_on='year',
    right_on='index'
)

print(merged_table.head())

plt.subplot
plt.plot(merged_table['year'], merged_table['aap'], label="aap")
plt.plot(merged_table['year'], merged_table['aggregate_gdp'], label="aggregate gdp")
plt.legend()
plt.show()
