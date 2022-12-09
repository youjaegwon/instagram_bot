import mysql.connector
import util.crypto
import config

from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host': 'freeworlddb.cnoo5dxelb2s.ap-northeast-2.rds.amazonaws.com',
  'user': 'freeworlduser',
  'password': util.crypto.SimpleEnDecrypt(config.access_key),
  'database': 'freeworldDB',
}

# Construct connection string
def dbCon() :
    try:
        conn = mysql.connector.connect(**config)
        print("Connection established")
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)