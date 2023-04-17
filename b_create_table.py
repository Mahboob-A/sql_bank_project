



"""
Conceptual Session : 4 - 1 -- Bank Project Using Python and SQL 
Moudle Date : 230323, Thursday (1st roja begin day)
Watch Date : 170423, Monday, 25th Roja, 10.30 am 

"""


import pymysql

conn = pymysql.connect(
    
        host = "localhost", 
        user = "root",
        passwd = "learnlearn",
        database = "bankproject"

)


mycursor = conn.cursor()

sql_command =                           """

                                                     CREATE TABLE accounts (
                                                
                                                     id INT AUTO_INCREMENT PRIMARY KEY, 
                                                     first_name VARCHAR(20) NOT NULL, 
                                                     last_name VARCHAR(30) NOT NULL, 
                                                     balance DECIMAL(12, 4) DEFAULT(1000.00)
                                                     
                                                     );

                                                     """


mycursor = conn.cursor()

mycursor.execute(sql_command)
