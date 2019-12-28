import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password= "root",
    database="datarepresentation"
)

cursor = db.cursor()
sql="CREATE TABLE EmplDirectory (id INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(20),surname VARCHAR(25),Ext INT)"

cursor.execute(sql)




