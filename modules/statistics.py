import pandas as pd


def statistics_analysis(df):
    """Return descriptive statistics for the dataset's numeric columns."""
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return pd.DataFrame()

    statistics_df = numeric_df.describe().T
    statistics_df["median"] = numeric_df.median()
    statistics_df["skewness"] = numeric_df.skew()
    statistics_df["kurtosis"] = numeric_df.kurtosis()

    return statistics_df.round(2)
