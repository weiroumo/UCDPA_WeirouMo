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