import pandas as pd
from pathlib import Path
def load_data():
    
    script_dir=Path(__file__).resolve().parent
    project_dir=script_dir.parent
    data_f=project_dir/'data'
    data=data_f/'train.csv'
    df=pd.read_csv(data)
    return df
