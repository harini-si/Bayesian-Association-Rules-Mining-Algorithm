import pandas as pd
df=pd.read_csv("data/breast-cancer.csv",header=None)
df.columns=["Class","age","menopause","tumor-size","inv-nodes","node-caps","deg-malig","breast","breast-quad","irradiat"]
#remove the rows with missing values
df.drop(df[df["node-caps"]=="?"].index,inplace=True)
df.drop(df[df["breast-quad"]=="?"].index,inplace=True)

df['node-caps'] = df['node-caps'].replace(['no'], 'no_node_caps')
df['node-caps'] = df['node-caps'].replace(['yes'], 'node_caps')
df['irradiat'] = df['irradiat'].replace(['no'], 'no_irradiat')
df['irradiat'] = df['irradiat'].replace(['no'], 'no_node_caps')
df.to_csv("data/bc.csv",index=False)
