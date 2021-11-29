import os
from read import get_json_reader
from write import load_db_table


def process_table(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])


def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    table_names = os.environ.get('TABLE_NAMES').split(',')

    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["USER"]}:{configs["PASSWORD"]}@{configs["HOST"]}:{configs["PORT"]}/{configs["DATABASE"]}'
    for table_name in table_names:
        process_table(BASE_DIR, conn, table_name)


if __name__ == '__main__':
    main()