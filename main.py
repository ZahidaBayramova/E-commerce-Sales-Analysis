from src.load_data import load_data
from src.database import create_database
from src.analysis import explore_data
from src.sql_queries import sql_queries
from src.sql_queries import business_queries
df=load_data()
conn=create_database(df)
explore_data(df)
sql_queries(conn)
business_queries(conn)