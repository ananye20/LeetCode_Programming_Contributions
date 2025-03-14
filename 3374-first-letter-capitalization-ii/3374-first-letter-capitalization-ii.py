import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    l=[]
    user_content['original_text']=user_content['content_text']
    user_content['converted_text'] = user_content['content_text'].str.title()
    user_content.drop(columns=["content_text"], inplace=True)
    return user_content
    