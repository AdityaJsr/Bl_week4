import mysql.connector as msc

mydb = msc.connect(host = 'localhost' , user = 'root' , passwd = 'admin')
mycursor = mydb.cursor()
mycursor.execute("show databases")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)