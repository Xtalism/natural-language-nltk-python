import math

import pandas as pd
import sklearn.linear_model as liner_model

df = pd.read_csv("examples/data/homeprices.csv")
median_bedrooms = math.floor(df.bedrooms.median())
print(f"Median number of bedrooms: {median_bedrooms}")

df.bedrooms = df.bedrooms.fillna(median_bedrooms)
print(df)

reg = liner_model.LinearRegression()
reg.fit(df[["area", "bedrooms", "age"]], df.price)  # [indedependent], dependent

# m1 * area + m2 * bedrooms + m3 * age = price
coeficients = reg.coef_
b = reg.intercept_
prediction = reg.predict([[3000, 3, 40]])
second_prediction = reg.predict([[2500, 4, 5]])
calculation = coeficients[0] * 3000 + coeficients[1] * 3 + coeficients[2] * 40 + b

print(f"Coefficients: {coeficients}")
print(f"Intercept: {b}")
print(f"Prediction for 3000 sqft, 3 bedrooms, 40 years old house: {prediction}")
print(f"Prediction for 2500 sqft, 4 bedrooms, 5 years old house: {second_prediction}")
# print(calculation)
