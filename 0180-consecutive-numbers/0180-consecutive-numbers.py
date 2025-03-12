import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    l=[]
    l1=[]
    for i in logs['num']:
        l.append(i)
    for i in range(0,len(l)-2):
        if(l[i]==l[i+1] and l[i+1]==l[i+2]):
            l1.append(l[i])
    l2 = list(set(l1))
    df = pd.DataFrame(l2, columns=['ConsecutiveNums'])
    return df


    