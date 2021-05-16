
import mysql.connector as msc
mydb = msc.connect(host = 'localhost' , user = 'root' , passwd = 'admin', database = 'employeedb' )
mycursor = mydb.cursor()

def showDb():
  mycursor.execute("SHOW DATABASES")
  for x in mycursor:
    print(x)

def showTable():
  mycursor.execute("SHOW TABLES")
  for x in mycursor:
    print(x)

def showData():
  
  mycursor.execute("select * from  employee")
  myresult = mycursor.fetchall()
  
  for values in myresult:    
    id=values[0]  
    name=values[1]  
    salary=values[2]  
    print('id = ',id,'name = ',name,'salary = ',salary) 

def addRecord():

  # mycursor = mydb.cursor()

  try:
    id = int(input("Enter the id of the employee : "))
    name = input("Enter the name of the employee : ").upper()
    salary = input("Enter the salary of the employee : ")
    mycursor.execute("""
    INSERT INTO employee(id,name, salary)
    VALUES (%s,%s,%s)
    """, (id,name, salary))
    mydb.commit()
    print('Record inserted successfully...')

  except ValueError as ve:  
    print("Value error ", ve)
  
  except Exception as e:
    print("Oops something went wrong !!", e)

  except:  
    # rollback used for if any error   
    mydb.rollback()  
    mydb.close()#Connection Close

def delData():
  try:
    showData()
    name = input("Enter the name : ").upper()
    mycursor.execute("""
    DELETE FROM employee WHERE name = '%s'""" % (name))
    
    mydb.commit()
    print('Record deleted successfully...',mycursor.rowcount)

  except ValueError as ve:
    print("Enter a proper value", ve)

  except Exception as e:
    print("Oops something went wrong!!", e)

  except:
    mydb.rollback()  
    mydb.close()#Connection Close
  
  finally:
    showData()
  

def updateData():
  
  mycursor.execute("select * from  employee")
  myresult = mycursor.fetchall()

  showData() 
  id = int(input("Enter the id of the person you want to update : "))
  mycursor.execute("""
  SELECT * from employee WHERE id = %d """%(id))
  for x in mycursor:
    print(x)
  ch = int(input("Press 1 to update name\nPress 2 to update salary : "))
  if ch == 1:
    change = 'name'
  elif ch ==2 :
    change = 'salary'
  

def main():
  try:
    ch = int(input("Press 1 to show-all the Databases \
    \nPress 2 to perform show-all the Tables Database \
    \nPress 3 to perform show-all Data from the Database \
    \nPress 4 to perform add-record to the Database \
    \nPress 5 to perform delete-record opertation on the Database \
    \nPress 6 to perform update record operation on the Database \
    \nEnter your choice : "))
  except ValueError:
    print("Enter a proper value to excecute ")
  except Exception as e:
    print("Oops something went wrong ")

  if (ch == 1):
    showDb()
  elif (ch == 2):
    showTable()
  elif (ch == 3):
    showData()
  elif (ch == 4):
    addRecord()
  elif (ch == 5):
    delData()
  elif (ch == 6):
    updateData()
    
  else:
    print("Try again : ")
    main()


if __name__ == '__main__':
  main()
