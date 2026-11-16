import sqlalchemy 


def get_engine():
    engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:Sanskar%240724@localhost:5432/etl')
    return engine
get_engine() 