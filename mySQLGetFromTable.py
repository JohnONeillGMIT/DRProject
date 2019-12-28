import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password= "root",
    database="datarepresentation"
)

cursor = db.cursor()
sql="select * from empldirectory where id = %s"
values = (10001,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)



