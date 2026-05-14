import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    X = df.drop("MedHouseVal", axis = 1)
    y = df["MedHouseVal"]

    return X, y

    