import pandas as pd

# Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv("Train.csv")
hue_colors = {0: "m",
              1: "c"}
sns.countplot(x="Warehouse_block", data=df1, hue="Reached.on.Time_Y.N", palette=hue_colors)

plt.show()

# Box plot
df2 = pd.read_csv("WorldBank_GDP.csv")
gdp = sns.catplot(x="Year", y="GDP", data=df2, kind="box")
plt.show()