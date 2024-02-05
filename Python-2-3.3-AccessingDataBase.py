# # creating a table in testdb

# import pymysql

# # Open database connection
# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="abcd4321",
#     database="testdb"
# )
# # prepare a cursor object using cursor() method
# cursor = db.cursor()

# # Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# # Create table as per requirement
# sql = """CREATE TABLE EMPLOYEE (
#    FIRST_NAME  CHAR(20) NOT NULL,
#    LAST_NAME  CHAR(20),
#    AGE INT,  
#    SEX CHAR(1),
#    INCOME FLOAT )"""

# cursor.execute(sql)

# # disconnect from server
# db.close()


# # inserting new records to a table

# import pymysql

# # Open database connection
# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="abcd4321",
#     database="testdb"
# )

# # prepare a cursor object using cursor() method
# cursor = db.cursor()

# # # Prepare SQL query to INSERT a record into the database.
# # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
# #    LAST_NAME, AGE, SEX, INCOME)
# #    VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

# # # creating SQL queries dynamically
# # sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
# #    LAST_NAME, AGE, SEX, INCOME) \
# #    VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
# #    ('Percy', 'Jackson', 18, 'M', 20000)
# # Create a cursor object

# # SQL statement for insertion
# sql_insert = """
# INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
# VALUES
#     ("Harry", "Potter", 20, "M", 60000),
#     ("Hermion", "Granger", 20, "F", 50000),
#     ("Ron", "Weasly", 20, "M", 50000),
#     ("Ginny", "Weasly", 16, "F", 40000)
# """

# try:
#     # Execute the SQL statement
#     cursor.execute(sql_insert)

#     # Commit your changes in the database
#     db.commit()
#     print("Rows inserted successfully!")
# except Exception as e:
#     # Rollback in case there is any error
#     print(f"Error: {e}")
#     db.rollback()
# finally:
#     # Disconnect from the server
#     db.close()


# # quering all the records from EMPLOYEE table having salary more than 25000

# import pymysql

# # Open database connection
# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="abcd4321",
#     database="testdb"
# )

# # prepare a cursor object using cursor() method
# cursor = db.cursor()

# # Prepare SQL query to INSERT a record into the database.
# sql = "SELECT * FROM EMPLOYEE \
#       WHERE INCOME > '%d'" % (25000)
# try:
#    # Execute the SQL command
#    cursor.execute(sql)
#    # Fetch all the rows in a list of lists.
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#       # Now print fetched result
#       print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
#          (fname, lname, age, sex, income ))
# except:
#    print ("Error: unable to fetch data")

# # disconnect from server
# db.close()


# # update operation

# import pymysql

# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="abcd4321",
#     database="testdb"   
# )

# cursor = db.cursor()

# sql = """ UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = "M" """
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()


# # delete operation

# import pymysql

# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="abcd4321",
#     database="testdb"    
# )

# cursor = db.cursor()

# sql = """ DELETE FROM EMPLOYEE WHERE AGE < 20 """

# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

# db.close()



