import pickle

import pandas as pd
from sklearn import linear_model

x: int = 5000

df = pd.read_csv("examples/data/initial_homeprices.csv")
# print(df)

model = linear_model.LinearRegression()
model.fit(df[["area"]], df.price)

coefficients = model.coef_
interception = model.intercept_
cost = model.predict([[x]])

print(f"Coefficients: {coefficients}")
print(f"Interception: {interception}")
print(f"Cost for area {x}: {cost[0]}")

with open("model_pickle", "wb") as f:
    pickle.dump(model, f)

with open("model_pickle", "rb") as f:
    mp = pickle.load(f)

print(mp.predict([[x]]))
