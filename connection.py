from sqlalchemy import create_engine

dburl = 'postgresql://scott:tiger@localhost:5432/test123'
engine = create_engine(dburl) 

connection = engine.connect()
