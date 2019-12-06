from sqlalchemy import create_engine

dburl = 'postgresql://supriadi:190277@localhost:5432/test123'
engine = create_engine(dburl)

try:
    cursor  = engine.connect()
    sql = "select * from customer"
    results = cursor.execute(sql)
    for result in results:
        print( "id : %d, name : %s, age : %d" % ( result[0], result[1], result[2]))

except:
    print("terjadi kesalahan")