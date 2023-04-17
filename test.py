


"""
Conceptual Session : 4 - 1 -- Bank Project Using Python and SQL 
Moudle Date : 230323, Thursday (1st roja begin day)
Watch Date : 170423, Monday, 25th Roja, 10.30 am 

"""


import pymysql

conn = pymysql.connect(
    
        host = "localhost", 
        user = "root",
        passwd = "learnlearn"

)

print(conn)