import pandas as pd
def sales_by_region(df_new):
    sales_region=df_new.groupby('Region')['Sales'].sum()
    return sales_region
def sales_by_category(df_new):
    sales_category=df_new.groupby('Category')['Sales'].sum()
    return sales_category
def sales_by_state(df_new):
    sales_state=df_new.groupby('State')['Sales'].sum()
    sales_state=sales_state.sort_values(ascending=False)
    sales_state_10=sales_state.head(10)
    return sales_state_10
def sales_by_subcategory(df_new):
    sales_subcategory=df_new.groupby('Sub-Category')['Sales'].sum()
    return sales_subcategory
def top_products(df_new):
    counts=df_new['Product Name'].value_counts()
    top_products_10=counts.head(10)
    return top_products_10
def ship_mode(df_new):
    most_ship=df_new['Ship Mode'].value_counts()
    return most_ship
def shipping_time(df_new):
    shipping=df_new['Ship Date']-df_new['Order Date']
    print(shipping.mean())
    print(shipping.max())
    print(shipping.min())
def monthly_trend(df_new):
    df_new['order_month']=df_new['Order Date'].dt.month_name()
    orders_month=df_new.groupby('order_month')['Sales'].sum()
    
    return orders_month
def yearly_trend(df_new):
    df_new['order_years']=df_new['Order Date'].dt.year
    orders_years=df_new.groupby('order_years')['Sales'].sum()
    
    return orders_years


