"""
reflection reads database and builds SQL alchemy table object
"""

from sqlalchemy import create_engine

dburl = "postgresql://supriadi:190277@localhost:5432/test123"

engine = create_engine( dburl)

from sqlalchemy import MetaData, Table

metadata = MetaData()
tb_user = Table("tb_user", metadata, autoload=True, autoload_with=engine)

print(repr(tb_user))

