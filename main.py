import pandas as pd


def handler():
    df = pd.read_csv("balanced-all.csv")
    print(df.head())


if __name__ == "__main__":
    handler()

