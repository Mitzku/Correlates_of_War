import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re


#change
cow_nmc = pd.read_csv('NMC_5_0.csv')

# aap = absolute aggregate power

cow_nmc['aap'] = cow_nmc['milex'] + cow_nmc['milper'] + cow_nmc['irst'] + cow_nmc['pec'] + cow_nmc['tpop'] + cow_nmc['upop']

# First we need to calculate the aggregate power of every country by adding up the six individual
# power components and dividing them by six.

# The thesis made use of a relative power index for a group of countries.
# While this does not allow to adapt the model for other countries, it is first reproduced in step 1


# General Inquiries
# How did the overall absolute power evolve in the international system over time?
aap_by_year = cow_nmc.groupby('year')['aap'].sum().reset_index()

plt.plot(aap_by_year['year'], aap_by_year['aap'])


# How does this compare to Global GDP (1960-2017)?
# The WorldBank dataset requires cleaning.

global_gdp = pd.read_csv('global_gdp_wb.csv', sep=',"',engine='python')
global_gdp = global_gdp.replace('"', '', regex=True)
global_gdp = global_gdp.rename(columns=lambda x: re.sub('"','',x))
global_gdd = global_gdp.rename(columns={'ï»¿Country Name':'Year'}, inplace=True)
global_gdp = global_gdp.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1)
global_gdp_transposed = global_gdp.set_index('Year').T
global_gdp_transposed = global_gdp_transposed.reset_index()
cols = global_gdp_transposed.columns.tolist()
global_gdp_transposed[cols] = global_gdp_transposed[cols].apply(pd.to_numeric, errors='coerce', axis=1)
global_gdp_transposed['aggregate_gdp'] = global_gdp_transposed.sum(axis=1)

# We need to create the relevant format (i.e. global GDP by year in this case) to make it comparable

###### !!!! Could be better to do this using .melt ? TRY!!!!!
###### ALSO df.reps = pd.to_numeric(split_df[1]) might be a good tool to do the to_numeric transformation
#

# Now we need to merge the data frames.

aap_gdp_merged = pd.merge(
    aap_by_year,
    global_gdp_transposed,
    left_on='year',
    right_on='index'
)

print(aap_gdp_merged.head())

plt.subplot(1,2,1)
plt.plot(aap_gdp_merged['year'], aap_gdp_merged['aap'], label="aap")
plt.title("aap")

plt.subplot(1,2,2)
plt.plot(aap_gdp_merged['year'], aap_gdp_merged['aggregate_gdp'], label="aggregate gdp")
plt.title("gdp")



# Now that we merged the gdp and aap data, we want to look at an individual's country share of the total aap over time


