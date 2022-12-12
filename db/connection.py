from mysql.connector import errorcode
from util import crypto
import config
import mysql.connector
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# Obtain connection string information from the portal
simpleEnDecrypt = crypto.SimpleEnDecrypt(config.ende_key)

config = {
    'host': 'freeworlddb.cnoo5dxelb2s.ap-northeast-2.rds.amazonaws.com',
    'user': 'freeworlduser',
    'password': simpleEnDecrypt.decrypt(config.access_key),
    'database': 'freeworldDB',
}

# Construct connection string


def dbCon():
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
