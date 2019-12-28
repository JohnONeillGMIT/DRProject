import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password= "root",
    database="datarepresentation"
)

cursor = db.cursor()
sql="insert EmplDirectory (id,first_name,surname,Ext) values (%s,%s,%s,%s)"
# deliberately setting first ID value
values = (10001,"Paul","Hewson",1001)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, id=:",cursor.lastrowid)




