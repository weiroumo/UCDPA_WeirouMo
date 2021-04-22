# Real world dataset:  The aviation accident database throughout the world, from 1908-2019.

# import data

# Import package
from urllib.request import urlretrieve

# Assign url of file: url
url = "https://www.kaggle.com/cgurkan/airplane-crash-data-since-1908"

# Save file locally
urlretrieve(url, 'airplane-crash-data-since-1908.csv')

# Import pandas
import pandas as pd

# import airplane crash CSV file into a Pandas DataFrame and print its head
df = pd.read_csv('Airplane_Crashes_and_Fatalities_Since_1908_20190820105639.csv')
print(df.head())

# importing data
import pandas as pd
file = "Train.csv"
commerce = pd.read_csv(file)

#
print(commerce.shape)
print(commerce.info())
print(commerce.columns)

# sorting data by Cost_of_the_Product and Weight_in_gms
commerce_cost_weight = commerce.sort_values(["Cost_of_the_Product", "Weight_in_gms"], ascending = [False, True])
print(commerce_cost_weight)

# filter rows where Mode_of_Shipment is Ship and Weight is > 4000
commerce_ship_time = commerce[(commerce["Mode_of_Shipment"] == "Ship") & (commerce["Weight_in_gms"] > 4000)]
print(commerce_ship_time)
