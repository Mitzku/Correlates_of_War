import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



cow_nmc = pd.read_csv('NMC_5_0.csv')

print(cow_nmc.columns)

# aap = absolute aggregate power

cow_nmc['aap'] = cow_nmc['milex'] + cow_nmc['milper'] + cow_nmc['irst'] + cow_nmc['pec'] + cow_nmc['tpop'] + cow_nmc['upop']

print(cow_nmc.head())

# First we need to calculate the aggregate power of every country by adding up the six individual power components and dividing them by six.
# The thesis made use of a relative power index for a group of countries. While this does not allow to adapt the model for other countries, it is first reproduced in step 1


# General Inquiries
# How did the overall absolute power evolve in the international system over time?
aap_by_year = cow_nmc.groupby('year')['aap'].sum().reset_index()

print(aap_by_year.head())

plt.plot(aap_by_year['year'], aap_by_year['aap'])
plt.show()



# How does this compare to Global GDP (1960-2017)?
