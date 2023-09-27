# Import frequently used libraries
# Initialize constant variables

import mysql.connector

class MySQL_connnection:
    def __init__(self, host, user, password, database) -> None:
        self.connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database)
        self.mycursor = self.connection.cursor()

