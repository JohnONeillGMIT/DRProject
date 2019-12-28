import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost?",
    user = "root",
    password = "root",
    database = "???"
)

mycursor = mydb.cursor()
sql="insert int student (name, address) values (%s,%s)"
values = ("Mary", "Galway")
mycursor.execute(sql,values)

#all update functions have to be committed
db.commit()



