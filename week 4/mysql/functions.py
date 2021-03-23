import mysql.connector as msc

mydb = msc.connect(
    host = 'localhost' ,
    user = 'root' ,
    passwd = 'admin',
    database = 'employeedb'
    )


mycursor = mydb.cursor()

# mycursor.execute("""CREATE TABLE people (first_name VARCHAR(50) NOT NULL,
#  last_name VARCHAR(50) NOT NULL, personID int PRIMARY KEY AUTO_INCREMENT)""")

def addRecord():
    try:
        fName = input("Enter the First name : ").upper()
        lName = input("Enter the Last name : ").upper()
        mycursor.execute("INSERT INTO people (first_name,last_name) VALUES (%s,%s)",(fName , lName ))
        mydb.commit()
    except ValueError as ve:
        print("Enter proper value : ",ve)
    except Exception as e:
        print("Oops something went wrong !!", e)
    except:  
        # rollback used for if any error   
        mydb.rollback()  
        mydb.close()
    
def showDb():
    mycursor.execute("SELECT * from people")
    for items in mycursor:
        fName = items[0],
        lName = items[1],
        id = items[2]
        print('First_Name = ', fName , 'Last_Name = ', lName , 'I.D = ', id )
def createFun():
    mycursor.execute("""
        CREATE FUNCTION full_name(first_name CHAR(30),last_name CHAR(30))
        RETURNS CHAR(65) DETERMINISTIC
        RETURN CONCAT(first_name,' ',last_name)
    """)

def useCreateFun():

    mycursor.execute("""
        SELECT full_name(first_name,last_name) AS name
        FROM people
    """)

    for x in mycursor:
        print(x)

def describeTable():

    mycursor.execute("""
        DESC people
    """)
    for items in mycursor:
        print(items)

def revFun():
    mycursor.execute("""
        CREATE FUNCTION rev_name(first_name CHAR(30))
        RETURNS CHAR(30) DETERMINISTIC
        RETURN REVERSE(first_name)
    """)
    # mycursor.execute("""
    # DROP FUNCTION rev_name
    # """)

def useRevFun():
    mycursor.execute("""
        SELECT rev_name(first_name) AS RF_name
        FROM people
    """)
    for x in mycursor:
        print(x)



def main():
    # addRecord()
    # showDb()
    # createFun()
    # useCreateFun()
    # describeTable()
    # revFun()
    useRevFun()

if __name__ == "__main__":
    main()