import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    man = employee['managerId'].value_counts()
    man_id = man[man>=5].index
    df2 = employee.loc[employee['id'].isin(man_id), 'name']
    df = pd.DataFrame(df2)
    return df