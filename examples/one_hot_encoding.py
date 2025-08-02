import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv("examples/data/one_hot_encoding.csv")

dummies = pd.get_dummies(df.town)
merged = pd.concat([df, dummies], axis="columns")
final = merged.drop(["town", "west windsor"], axis="columns")

model = LinearRegression()
X = final.drop("price", axis="columns")
y = final.price
model.fit(X, y)
cost = model.predict([[2800, 0, 1]])

model.score(X, y)  # how accurate the model is

le = LabelEncoder()
dfle = df
dfle.town = le.fit_transform(dfle.town)
# print(dfle)

X = dfle[["town", "area"]].values
y = dfle.price.values

# print(f"\nX values: \n{X} \nPrice values(y): \n{y}")

ct = ColumnTransformer([("town", OneHotEncoder(), [0])], remainder="passthrough")

X = ct.fit_transform(X)

X = X[:, 1:]
print(X)

model.fit(X, y)
cost = model.predict([[1, 0, 2800]])
print(cost)
