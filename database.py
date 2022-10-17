import mysql.connector
from mysql.connector import Error



def B2C_execute_query(query):
    try:
        connection = mysql.connector.connect(host='172.17.2.93',
                                             database='db_grab_sit',
                                             user='debashishkha',
                                             password='Deb@shih#321')
        record = ""
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            result = cursor.execute(query)
            record = cursor.fetchall()
            # a_string = record.replace(',)', '')
            # b_string = record.replace('(', '')
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return record
