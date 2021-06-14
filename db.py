import pandas as pd
def get_db():
    db = pd.read_csv("vgsales.csv")
    db = pd.DataFrame(db)
    db['Year'] = db['Year'].fillna(-1)
    db['Year'] = db['Year'].astype(int)
    return db