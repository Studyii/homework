import pandas as pd
df = pd.read_csv("d:\Desktop\completebaw.csv")
x = df.query("price >= 100 and price <= 150")
print(x)

