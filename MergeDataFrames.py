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
print(gdp_pop.isna().any())

# Iterate over rows of gdp-pop and calculate GDP per capita
for lab, row in gdp_pop.iterrows():
    print(str(lab) + row['Country Name'] + str(row['Year']) + ": " + str(row['GDP']/row['Pop']))


