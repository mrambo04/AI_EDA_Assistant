import pandas as pd


def dataset_overview(df):

    overview = {}

    overview["Rows"] = df.shape[0]
    overview["Columns"] = df.shape[1]

    overview["Missing Values"] = df.isnull().sum().sum()

    overview["Duplicate Rows"] = df.duplicated().sum()

    overview["Memory Usage (KB)"] = round(
        df.memory_usage(deep=True).sum() / 1024, 2
    )

    overview["Numeric Columns"] = len(
        df.select_dtypes(include="number").columns
    )

    overview["Categorical Columns"] = len(
        df.select_dtypes(include="object").columns
    )

    overview["Boolean Columns"] = len(
        df.select_dtypes(include="bool").columns
    )

    overview["Datetime Columns"] = len(
        df.select_dtypes(include="datetime").columns
    )

    return overview