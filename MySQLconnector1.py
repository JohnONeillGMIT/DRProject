import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost?",
    user = "root",
    password = "root",
    database = "???"
)

mycursor = mydb.cursor()
sql="some sql"
mycursor.execute(sql)



