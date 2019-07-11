import pandas as pd
df = pd.read_csv('sales100.csv', index_col="Region")
print(df)