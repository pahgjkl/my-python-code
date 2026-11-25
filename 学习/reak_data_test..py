import pandas as pd
import json
with open("账本.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)
pf = pd.DataFrame(raw_data)
print(pf)
print("\n")
ji = pf[pf["type"] == "incom"]
hi = ji["amount"].sum()
print(hi)
print("\n")
ki = pf[pf["type"] == "income"]
li = ki["amount"].sum()
print(li)
print("\n")
print(pf.groupby("type")["amount"].sum())