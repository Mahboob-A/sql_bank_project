

"""
Conceptual Session : 4 - 1 -- Bank Project Using Python and SQL 
Moudle Date : 230323, Thursday (1st roja begin day)
Watch Date : 170423, Monday, 25th Roja, =12.00 pm 

"""

import pymysql

conn = pymysql.connect(
    
        host = "localhost", 
        user = "root",
        passwd = "learnlearn",
        database = "bankproject"

)


def create_account(f_name, l_name, balance):
        mycursor = conn.cursor()
        mycursor.execute("INSERT INTO accounts (first_name, last_name, balance) VALUES (%s, %s, %s)", (f_name, l_name, balance))
        conn.commit()
        mycursor.close()
        # %s is format specifier. put a coma after each specifier. it refers to the chronological sequence of given parameters in right hand side 


def check_balance(id):
        mycursor = conn.cursor()
        mycursor.execute("SELECT BALANCE FROM accounts WHERE id = (%s)", (id))
        mycursor.close()