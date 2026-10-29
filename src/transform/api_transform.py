import pandas as pd

def transformer(products):
    df = pd.DataFrame(products)
    cleaned_df = df.drop(columns = ['image','rating'])
    updated_col = cleaned_df.rename(columns = {'id':'product_id','title':'product_tittle'})
    added_col = updated_col.assign(load_timestamp = pd.Timestamp.now())
    return added_col
