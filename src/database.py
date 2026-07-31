import sqlite3
from pathlib import Path
def create_database(df):
    script_dir=Path(__file__).resolve().parent
    project_dir=script_dir.parent
    database=project_dir/'database'
    database_path=database/'sales.db'
    conn=sqlite3.connect(database_path)
    df.to_sql('train',conn,if_exists='replace',index=False)
    return conn
