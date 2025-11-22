import pandas as pd
df = pd.read_csv("~/Desktop/docs/names.csv")
df.head()
df = df.str.replace("min","max",regex=True)
