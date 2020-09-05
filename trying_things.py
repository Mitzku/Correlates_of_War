import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re


cow_nmc = pd.read_csv('NMC_5_0.csv')

# aap = absolute aggregate power

cow_nmc['aap'] = cow_nmc['milex'] + cow_nmc['milper'] + cow_nmc['irst'] + cow_nmc['pec'] + cow_nmc['tpop'] + cow_nmc['upop']
aap_by_state_and_year = cow_nmc.groupby(['stateabb', 'year'])['aap'].sum().reset_index()

# making boolean series for a state
filter = aap_by_state_and_year['stateabb'] == "USA"

# filtering data
filtered_for_state = aap_by_state_and_year.where(filter, inplace=True)


#but.... does this one really just have 5 entries?
print(cow_nmc.head())
print(filtered_for_state)
