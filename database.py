import mysql.connector
from mysql.connector import Error
import Constants


def B2C_execute_query(query, env='SIT'):
    try:
        if env == 'SIT':
            connection = mysql.connector.connect(host=Constants.SITDBHOST,
                                                 database=Constants.SITDBNAME,
                                                 user=Constants.SITDBUSERNAME,
                                                 password=Constants.SITDBPASSWORD)
        elif env == 'PROD':
            connection = mysql.connector.connect(host=Constants.PRODDBHOST,
                                                 database=Constants.PRODDBNAME,
                                                 user=Constants.PRODDBUSERNAME,
                                                 password=Constants.PRODDBPASSWORD)
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
