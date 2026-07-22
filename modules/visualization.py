import plotly.express as px


def histogram(df, column):
    return px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"Histogram of {column}"
    )


def boxplot(df, column):
    return px.box(
        df,
        y=column,
        title=f"Box Plot of {column}"
    )


def scatter(df, x, y):
    return px.scatter(
        df,
        x=x,
        y=y,
        title=f"{x} vs {y}"
    )


def bar_chart(df, column):
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, "Count"]

    return px.bar(
        counts,
        x=column,
        y="Count",
        title=f"{column} Distribution"
    )


def pie_chart(df, column):
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, "Count"]

    return px.pie(
        counts,
        names=column,
        values="Count",
        title=f"{column} Distribution"
    )