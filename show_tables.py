from sqlalchemy import create_engine

dburl = "postgresql://supriadi:190277@localhost:5432/test123"
engine = create_engine(dburl)

print( engine.table_names())