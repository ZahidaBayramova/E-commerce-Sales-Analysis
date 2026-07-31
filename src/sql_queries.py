import pandas as pd
def sql_queries(conn):
    count_orders = """
    select count(*) as total
    from train;
    """
    print("\n----Number of Orders----")
    print(pd.read_sql(count_orders, conn))
    categories = """
    select distinct Category
    from train;
    """
    print("\n----Categories----")
    print(pd.read_sql(categories, conn))
    regions = """
    select distinct Region
    FROM train;
    """
    print("\n----Regions----")
    print(pd.read_sql(regions, conn))
    top_sales = """
    select *
    FROM train
    order by Sales desc
    limit 10;
    """
    print("\n----Top 10 Highest Sales----")
    print(pd.read_sql(top_sales, conn))
    technology = """
    select *
    from train
    where Category = 'Technology';
    """
    print("\n----Technology Category----")
    print(pd.read_sql(technology, conn))
def business_queries(conn):
    sales_by_category = """
    select
        Category,
        sum(Sales) as totalsale
    from train
    group by  Category
    order by totalsale desc;
    """
    print("\n----Total Sales by Category----")
    print(pd.read_sql(sales_by_category, conn))
    sales_by_region = """
    select
        Region,
        sum(Sales) as totalsales
    from train
    group by Region
    order by totalsales desc;
    """
    print("\n----Total Sales by Region----")
    print(pd.read_sql(sales_by_region, conn))
    avg_sales_region = """
    select
        Region,
        avg(Sales) as averagesales
    from train
    group by Region
    order by averagesales desc;
    """
    print("\n----Average Sales by Region----")
    print(pd.read_sql(avg_sales_region, conn))