import pandas as pd

df = pd.read_csv("data/output.csv")
df = df.sort_values(by=["bayesian confidence"], ascending=False)
print("Top 10 rules with highest bayesian confidence")
print(df[:10])
print("Class association rules")
dfrl = df[df["B"].str.contains("no-recurrence-events")]
dfrl = dfrl.sort_values(by=["bayesian confidence"], ascending=False)
print(dfrl[:10])
