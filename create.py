from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from classing_mapping import User
from declarative_mapping import Student

if __name__ == "__main__" :

    try :
        db_url = "postgresql://supriadi:190277@localhost:5432/test123"
        engine = create_engine(db_url)
        
        session = sessionmaker(bind=engine)
        my_session = session()
    except :
        print("terjadi kesalahan")