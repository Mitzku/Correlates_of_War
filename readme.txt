# The Correlates of War Datasets can be downloaded from https://correlatesofwar.org/data-sets/national-material-capabilities
# This Project makes use of the most recent COW Dataset National Material Capabilities (v5.0) https://correlatesofwar.org/data-sets/national-material-capabilities
# It aims to reproduce what I did in my MA thesis, which can be found here: http://othes.univie.ac.at/32272/1/2014-03-19_1127018.pdf
# The first tasks are to reproduce the visualizations on page 24 and 27 and 29.
# The graphics on page 24 and 29 capture the overall share of power (as defined by the COW approach) of a set of countries. The reproduction should make it possible to do this for n countries instead of only having the fixed countries as in the graphics.
# The graphic on page 27 captures the overall share of power of two groups of countries. This means it aggregates several countries. The reproduction should make this possible for n number of country groupings.
# Any other interesting things that come across will be investigated in this project.


# We look at other datasets as frame of reference and to get additional insights

# 1) Data on global GDP
# It is difficult to get adequate data prior to 1960.
# The Maddison Project provides fragmented historical data but is not adequate because of the many gaps, see https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2018?lang=en
# The WorldBank provides data from 1960 to 2019, see https://data.worldbank.org/indicator/NY.GDP.MKTP.CD
