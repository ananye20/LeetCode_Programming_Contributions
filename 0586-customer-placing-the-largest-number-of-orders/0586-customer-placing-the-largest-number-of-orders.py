import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    a = orders['customer_number'].value_counts()
    b = a.head(1)
    c=b.index
    df = orders.loc[orders['customer_number'].isin(c), 'customer_number']
    df = df.drop_duplicates()
    df2 = pd.DataFrame(df)
    return df2

    