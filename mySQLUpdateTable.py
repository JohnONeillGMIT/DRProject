import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password= "root",
    database="datarepresentation"
)

cursor = db.cursor()
sql="update empldirectory set first_name= %s, surname=%s where id = %s"
values = ("BONO","VOX",10001)

cursor.execute(sql,values)
db.commit()
print("update done")




