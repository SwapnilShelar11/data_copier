import os

import pandas as pd


def load_db_table(df,conn,table_name, key):
    min_key = df[key].min()
    max_key = df[key].max()
    df.to_sql(table_name, conn, if_exists='append', index=False)
    print(f'Loaded data for {table_name} with in the range of {min_key} and {max_key}')

if __name__=="__main__":
    data = [
        {'user_id': 1, 'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
        {'user_id': 2, 'user_first_name': 'Donald', 'user_last_name': 'Duck'}
    ]
    df=pd.DataFrame(data)
    config=dict(os.environ.items())
    conn=f'postgresql://{config["USER"]}:{config["PASSWORD"]}@{config["HOST"]}:{config["PORT"]}/{config["DATABASE"]}'
    load_db_table(df,conn,'user',"user_id")