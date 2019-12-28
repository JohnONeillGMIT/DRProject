import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password= "root",
    database="datarepresentation"
)

cursor = db.cursor()
sql="delete from empldirectory where id = %s"
values = (10001,) #be sure to leave in the comma as tuple!

cursor.execute(sql,values)
db.commit()
print("delete done")




