import pandas as pd

df = pd.DataFrame() 
df["Col1"] = [0,2,4,6,2] 
df["Col2"] = [5,1,3,4,0]
df["Col3"] = [8,0,5,1,7]
df["Col4"] = [1,4,6,0,8]
df_new = df.iloc[:, 1:3]

print(df_new)