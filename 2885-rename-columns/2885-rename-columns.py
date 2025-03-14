import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students['student_id'], students['first_name'], students['last_name'], students['age_in_years']= students['id'], students['first'], students['last'], students['age']
    return students.drop(['id','first', 'last','age'], axis = 1)
    