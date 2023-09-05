import mysql.connector

database  = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Tata@786786'

)

#prepare a cursor object
cursorObject = database.cursor()

#create a db

cursorObject.execute("CREATE DATABASE dtuco")

print("Done!")