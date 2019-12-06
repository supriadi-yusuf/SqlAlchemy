from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

dburl = 'postgresql://supriadi:190277@localhost:5432/test123'
engine = create_engine(dburl)

my_base = declarative_base()

# create table
class Student(my_base):
    __tablename__ = 'tb_student'

    id = Column( Integer)
    name = Column(String(50))
    age = Column( Integer)

    def __str__(self):
        return self.name

    __table_args__ = (
        PrimaryKeyConstraint('id'),
    )

try:
    my_base.metadata.create_all(engine)
except:
    print("terjadi kesalahan")
