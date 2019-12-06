from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy.orm import mapper

meta = MetaData()

tb_user = Table( 'tb_user', meta, 
                    Column('id', Integer),
                    Column('name', String),
                    Column('age', Integer),
                    PrimaryKeyConstraint('id', name = 'tb_user_pk')
                    )

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

mapper(User, tb_user)

if __name__ == '__main__' :
    dburl = 'postgresql://supriadi:190277@localhost:5432/test123'
    engine = create_engine(dburl)
    
    try:
        meta.create_all(engine)
    except:
        print("terjadi kesalahan")
