import sqlalchemy 
import pandas

def get_engine():
    engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:Sanskar%400724@localhost:5432/etl')
    return engine

engine = get_engine()

'''with engine.connect() as connection:
    result = connection.execute(
           sqlalchemy.text("SELECT product_id FROM api_load_data")   
    )
print(result.fetchone())'''


def load_data(Dataframe):
    Dataframe.to_sql(name = 'api_load_data', con = engine, if_exists = 'append', index = False)