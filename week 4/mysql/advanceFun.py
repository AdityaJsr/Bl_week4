import mysql.connector as msc

mydb = msc.connect(
    host = 'localhost' ,
    user = 'root' ,
    passwd = 'admin',
    database = 'employeedb'
    )


mycursor = mydb.cursor()


# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)",("BHOOMI " , 11 ))
# mydb.commit()

def viewAllData():
    mycursor.execute("SELECT * from Person")
    for items in mycursor:
        name = items[0],
        age = items[1],
        id = items[2]
        print('name = ', name , 'age = ', age , 'id = ', id )

# viewAllData()

# mycursor.execute("DELETE FROM Person WHERE name = 'Rahul'")
# mydb.commit()
# viewAllData()
# mycursor.execute("DROP TABLE find_age")
def showTable():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        table = x[0]
        print("Table ",table)

def viewMain():
    # inputAge = int(input("Enter the age for view : ")) 
    # view1 = """CREATE VIEW find_rahul AS
    #         SELECT * FROM Person WHERE name = 'RAHUL'
    #     """
    # mycursor.execute(view1)
    # mydb.commit()
    mycursor.execute("SELECT * FROM find_rahul")
    for item in mycursor:
        print(item)

# viewMain()
# showTable()
viewAllData()

def storeProcedure():

   mycursor.execute("""

    DELIMITER $$

    CREATE PROCEDURE find_age()
    BEGIN
        SELECT * FROM person
    END$$
    
    DELIMITER

    """) 

# mycursor.execute("")

    
# mycursor.execute("SHOW PROCEDURE STATUS")
# storeProcedure()

# mycursor.callproc("find_age")

# # print out the result
# for result in mycursor.stored_results():
#     print(result.fetchall())

# mycursor.execute("CREATE INDEX name ON person(name)")
# mycursor.execute("DESCRIBE person")
# for d in mycursor:
#     print(d)


def storeProcedure2():

    createsProcedure = """
    CREATE PROCEDURE find_by_id AS
    SELECT * FROM person WHERE id = 1
    """
    mycursor.execute(createsProcedure)
    # mydb.commit()

storeProcedure2()
# showTable()