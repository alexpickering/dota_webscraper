import pandas as pd

df = pd.DataFrame({"Hero": ["Abaddon", "Alchemist", "Axe"],
                   "Str": [23, 25, 19]})

df["C"] = [1,2,3]
df.loc[:, "D"] = [1,2,3]
df = df.assign(E=[1,2,3])
print(df)
