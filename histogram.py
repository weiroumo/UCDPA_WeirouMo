import pandas as pd
file = "Train.csv"
commerce = pd.read_csv(file)

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# check any missing data
print(commerce.isna().any())

# Get total number of Weight_in_gms shipped by each mode
weight_shipped_by_mode = commerce.groupby("Mode_of_Shipment")["Weight_in_gms"].sum()

# Create a bar plot of the number of Weight shipped by each mode
weight_shipped_by_mode.plot(kind="bar")

# Show the plot
plt.show()


# Layering histogram plots
commerce[commerce["Mode_of_Shipment"] == "Flight"]["Cost_of_the_Product"].hist(alpha=1,bins=20)
commerce[commerce["Mode_of_Shipment"] == "Ship"]["Cost_of_the_Product"].hist(alpha=0.8,bins=20)
commerce[commerce["Mode_of_Shipment"] == "Road"]["Cost_of_the_Product"].hist(alpha=0.5,bins=20)
plt.legend(["Flight", "Ship", "Road"])
plt.show()