from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import sys
import os

def predict_house_price(m2, position):
    model = LinearRegression()
    scaler = StandardScaler()

    pd.options.display.float_format = '{:.2f}'.format

    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'larv_testdata.csv')
    df = pd.read_csv(data_path, header=0)

    df["lage_boosted"] = df["lage"] * 3.5

    X = df[["m2", "lage_boosted"]]
    y = df["pris"]

    scaled_data = scaler.fit_transform(X)
    df[["m2 stand", "lage_boosted stand"]] = scaled_data

    X = df[["m2 stand", "lage_boosted stand"]]
    y = df["pris"]
    model.fit(X, y)

    lage_boosted = position * 3.5
    input_data = scaler.transform([[m2, lage_boosted]])

    predicted_price = model.predict(input_data)
    return predicted_price

    