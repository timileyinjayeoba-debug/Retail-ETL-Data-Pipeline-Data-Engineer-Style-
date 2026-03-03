def transform_data(df):
    df["total_sales"] = df["quantity"] * df["price"]
    return df