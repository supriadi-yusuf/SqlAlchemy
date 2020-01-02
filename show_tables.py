from sqlalchemy import create_engine

dburl = 'postgresql://scott:tiger@localhost:5432/test123'
engine = create_engine(dburl)

print( engine.table_names())