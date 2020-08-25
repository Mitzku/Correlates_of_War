import pandas as pd
import re


# The WorldBank dataset requires cleaning.

global_gdp = pd.read_csv('global_gdp_wb.csv', sep=',"',engine='python')
global_gdp = global_gdp.replace('"', '', regex=True)
global_gdp = global_gdp.rename(columns=lambda x: re.sub('"','',x))
global_gdd = global_gdp.rename(columns={'ï»¿Country Name':'Year'}, inplace=True)
global_gdp = global_gdp.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1)
global_gdp_transposed= global_gdp.set_index('Year').T
cols = global_gdp_transposed.columns.tolist()
global_gdp_transposed[cols] = global_gdp_transposed[cols].apply(pd.to_numeric, errors='coerce', axis=1)




# We need to create the relevant format (i.e. global GDP by year in this case) to make it comparable

global_gdp_transposed['aggregate_gdp'] = global_gdp_transposed.sum(axis=1)


print(global_gdp_transposed.head())
print(global_gdp_transposed.dtypes)