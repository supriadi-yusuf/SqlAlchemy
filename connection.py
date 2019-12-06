from sqlalchemy import create_engine

db_url = "postgresql://supriadi:190277@localhost:5432/test123"
engine = create_engine(db_url) 

connection = engine.connect()