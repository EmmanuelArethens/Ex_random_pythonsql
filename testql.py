import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test_db',
                                         user='',
                                         password='')
    sql_insert_query = """ INSERT INTO `users`
                          (`id`, `name`, `birth_date`, `age`) VALUES (1,'Manu','1995-04-10', 24)"""
    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query)
    connection.commit()
    print ("Record inserted successfully into users table")
except mysql.connector.Error as error:
    connection.rollback()
    print("Failed inserting record into users table {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")