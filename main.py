from src.load_data import load_data
from src.database import create_database
from src.analysis import explore_data
from src.sql_queries import sql_queries
from src.sql_queries import business_queries
from src.cleaning import missing_values
from src.cleaning import changing_date
from src.eda import (
    sales_by_region,
    sales_by_category,
    sales_by_state,
    sales_by_subcategory,
    top_products,
    ship_mode,
    shipping_time,
    monthly_trend,
    yearly_trend,
)
df=load_data()
explore_data(df)
df_new=missing_values(df)
df_new=changing_date(df_new)
conn=create_database(df_new)
sql_queries(conn)
business_queries(conn)
sales_region=sales_by_region(df_new)
sales_category=sales_by_category(df_new)
sales_state_10=sales_by_state(df_new)
sales_subcategory=sales_by_subcategory(df_new)
top_products_10=top_products(df_new)
most_ship=ship_mode(df_new)
orders_month=monthly_trend(df_new)
orders_years=yearly_trend(df_new)
shipping_time(df_new)
