# Import frequently used libraries
# Initialize constant variables

import mysql.connector
import inspect

"""
## Setup instructions for MySQL server
Create new database noting vairables used in documentation below
Run: CREATE DATABASE (database name)

## Input variables
host = address of sql server, "localhost" for most servers
user = username for sql server, "root" for most servers
password = password for the user account on that host
database = name of the data base created above

## Example usage:
mydb = MySQL_connnection(host = 'localhost', user='root', password='pV=nRt89', database="ezdb")
print(mydb())
"""
class MySQL_connnection:
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        self.connection = mysql.connector.connect(
        user = user,
        password = password,
        host = host,
        database = database)
        self.mycursor = self.connection.cursor()
    
    def __call__(self):
        return self.mycursor
    
    def class_to_table(self, user_class):
        pass
        
        # Determine sql varaible type
        # Create columns based on name and type 
    
    def add_class_to_table(self, user_class):
        pass


class input_class:
    def __init__(self, user_class: object) -> None:
        self.user_class = user_class

    def __call__(self):
        self.parse_class()
        return self.class_dict

    def parse_class(self):
        self.class_dict = self.user_class.__dict__
        return self.class_dict



# Working env

class test_class:
    def __init__(self, variable1, variable2):
        self.variable1 = variable1
        self.variable2 = variable2
    
    def add_var(self, variable3):
        self.variable3 = variable3

t = test_class(1,2)
t.add_var(5)

user_input_class = input_class(t)
print(user_input_class())
