def explore_data(df):
    print(df.head())
    print(df.columns)
    print(df.info())
    print(df.describe(include='all'))
    print(df.isna().sum())
    print(df.duplicated().sum())

