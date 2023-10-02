# Import frequently used libraries
# Initialize constant variables

import mysql.connector

class MySQL_connnection:
    def __init__(self, host, user, password, database) -> None:
        self.connection = mysql.connector.connect(
        user = user,
        password = password,
        host = host,
        database = database)
        self.mycursor = self.connection.cursor()

mydb = MySQL_connnection(host = 'localhost', user='root', password='pV=nRt89', database="ezdb")
