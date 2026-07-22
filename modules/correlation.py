import pandas as pd


def correlation_matrix(df):

    numeric_df = df.select_dtypes(include="number")

    corr = numeric_df.corr()

    return corr


def high_correlation(df, threshold=0.8):

    corr = df.select_dtypes(include="number").corr()

    pairs = []

    columns = corr.columns

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):

            value = corr.iloc[i, j]

            if abs(value) >= threshold:

                pairs.append({
                    "Feature 1": columns[i],
                    "Feature 2": columns[j],
                    "Correlation": round(value, 3)
                })

    return pd.DataFrame(pairs)