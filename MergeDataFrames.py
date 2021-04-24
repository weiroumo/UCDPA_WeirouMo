import pandas as pd

# Import data

gdp = pd.read_csv('WorldBank_GDP.csv')
print(gdp.head())
print(gdp.shape)

pop = pd.read_csv('WorldBank_POP.csv')
print(pop.head())
print(pop.shape)

# Merge
gdp_pop = gdp.merge(pop, on=['Country Name', 'Country Code', 'Year'], suffixes=('_gdp', '_pop'))
print(gdp_pop.columns)
print(gdp_pop.shape)