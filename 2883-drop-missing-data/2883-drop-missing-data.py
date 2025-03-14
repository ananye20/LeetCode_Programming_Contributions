import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    s = students.dropna(subset=['name'])
    return s
    