from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from classic_mapping import User 

db_url = 'postgresql://scott:tiger@localhost:5432/test123'
engine = create_engine(db_url)

session = sessionmaker(engine)
my_session = session()

# get one record
user = my_session.query(User).first()
print("id : %d, name : %s, age : %d" % ( user.id, user.name, user.age))

# get all records
users = my_session.query(User).all()
for user in users : 
    print("id : %5d, name : %-20s, age : %5d" % ( user.id, user.name, user.age))