# EZdb for python

## William Ramsey 2023

A MySQL integration to easily save classes to MySQL tables

Every time I build a backend for a website using Python, I write custom methods to save the attributes of a class to a SQL database. For example, if we have the class user, we need to save their ID, username, password, and whatever other information may be associated with them to a database so it can be preserved without a continuous script running. Saving this information requires a lot of obnoxious code. 

To streamline this process, I am writing a Python library that can take any class, save its attributes to an SQL table, and automatically populate an empty Python class with information from an SQL database. This works by reading the attributes of a class as a dictionary, generating an SQL table with the same name as the class, determining the SQL datatypes from actual data within the class, and finally saving the class to the newly generated SQL table. 
