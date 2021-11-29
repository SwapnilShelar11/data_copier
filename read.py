import os
import pandas as pd

def get_json_reader(base_dir,table_name,chunksize=1000):
    file_name=os.listdir(f'{base_dir}//{table_name}')[0]
    fd=f'{base_dir}//{table_name}//{file_name}'
    return pd.read_json(fd,lines=True,chunksize=chunksize)

if __name__=="__main__":
    base_dir=os.environ.get("base_dir")
    table_name=os.environ.get("table_name")
    data=get_json_reader(base_dir,table_name)
    for d in data:
        print(d)