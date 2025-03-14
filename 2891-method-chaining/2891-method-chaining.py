import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals.loc[animals['weight']>100,:]
    df = df.sort_values(by='weight', ascending=False)
    return df[['name']]