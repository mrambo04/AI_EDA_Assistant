import pandas as pd

def missing_analysis(df):

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    missing_df = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    missing_df["Percentage"] = (
        missing_df["Missing Values"] / len(df) * 100
    ).round(2)

    missing_df = missing_df.sort_values(
        by="Missing Values",
        ascending=False
    )

    return missing_df