import pandas as pd
def missing_values(df):
    df_new=df.dropna(subset=['Postal Code']).copy()
    return df_new
def changing_date(df_new):
    df_new['Order Date']=df_new['Order Date'].str.strip()
    df_new['Order Date']=pd.to_datetime(df_new['Order Date'],format='%d/%m/%Y')
    df_new['Ship Date']=df_new['Ship Date'].str.strip()
    df_new['Ship Date']=pd.to_datetime(df_new['Ship Date'],format='%d/%m/%Y')
    return df_new
