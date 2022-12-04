import pandas as pd

df = pd.read_csv("data/output.csv")
df = df.sort_values(by=["bayesian confidence"], ascending=False)
print("Top 10 rules with highest bayesian confidence")
print(df[:10])
print("Class association rules")
dfrl = df[df["B"].str.contains("no-recurrence-events" or "recurrence-events")]
dfrl = dfrl.sort_values(by=["bayesian confidence"], ascending=False)
print(dfrl[:10])
df.to_csv("data/rules.csv", index=False)
dfrl.to_csv("data/rules_class.csv", index=False)
