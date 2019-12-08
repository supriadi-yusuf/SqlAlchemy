from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from classic_mapping import User
from declarative_mapping import Student

susanto = Student( name='susanto', age=15)
suharto = User(name='suharto', age=20)
mulyono = Student( name='mulyono', age=10)
heri = User( name='heri', age=15)

db_url = "postgresql://supriadi:190277@localhost:5432/test123"
engine = create_engine(db_url)
    
session = sessionmaker(bind=engine)
my_session = session()

my_session.add( suharto) # add one object
my_session.add( susanto) # add one object

my_session.add_all( [mulyono, heri]) # add many objects at once

my_session.commit()