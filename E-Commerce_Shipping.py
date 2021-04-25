
# importing data
import pandas as pd
file = "Train.csv"
commerce = pd.read_csv(file)

# dataframe info
print(commerce.shape)
print(commerce.info())
print(commerce.columns)

# check missing values
print(commerce.isna().any())

# Drop duplicate ID/Warehouse_block combinations
ID_Warehouse_block = commerce.drop_duplicates(subset=["ID", "Warehouse_block"])
print(ID_Warehouse_block.head())

# sorting data by Cost_of_the_Product and Weight_in_gms
commerce_cost_weight = commerce.sort_values(["Cost_of_the_Product", "Weight_in_gms"], ascending = [False, True])
print(commerce_cost_weight)

# filter rows where Mode_of_Shipment is Ship and Weight is > 4000
commerce_ship_time = commerce[(commerce["Mode_of_Shipment"] == "Ship") & (commerce["Weight_in_gms"] > 4000)]
print(commerce_ship_time)

# index commerce by Product_importance
commerce_ind = commerce.set_index("Product_importance")
print(commerce_ind)

# Make a list of importance to subset on
importance = ["high", "medium"]

# Subset commerce_ind on using .loc[]
print(commerce_ind.loc[importance])

# Sort commerce_ind by index values
commerce_srt = commerce_ind.sort_index()

# Slicing columns from Cost_of_the_Product to Weight_in_gms
print(commerce_srt.loc[:, "Cost_of_the_Product": "Weight_in_gms"])