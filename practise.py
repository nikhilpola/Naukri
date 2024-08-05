import pandas as pd

df = pd.DataFrame([[1,15],[2,11],[3,11],[4,20]],columns=["A","B"])
print(df)

df1 = df.loc[df["B"]==15]

print(df1)