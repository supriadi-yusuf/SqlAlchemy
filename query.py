from sqlalchemy import create_engine

dburl = 'postgresql://scott:tiger@localhost:5432/test123'
engine = create_engine(dburl)

try:
    connection  = engine.connect()
    stmt = "select * from tb_customer"
    result_proxy = connection.execute(stmt)
    result_set = result_proxy.fetchall()
    for result in result_set:
        print( "id : %d, name : %s, age : %d" % ( result[0], result[1], result[2]))

        # result is dictionary
        for key, val in result.items():
            print( "%s : %s" % (key,val))

    # result_proxy has been empty
    result_set = result_proxy.fetchall()
    for result in result_set:
        print( "id : %d, name : %s, age : %d" % ( result[0], result[1], result[2])) 
        
except:
    print("terjadi kesalahan")