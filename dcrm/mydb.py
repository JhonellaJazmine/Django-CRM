import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)

#prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE testing")

print("All Done!")