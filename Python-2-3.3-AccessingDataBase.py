# creating a table and inserting new records 

import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="abcd4321",
    database="testdb"
)

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

sql_insert = """INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
VALUES
    ('Mac', 'Mohan', 20, 'M', 20000),
    ('Percy', 'Jackson', 18, 'M', 25000),
    ("Harry", "Potter", 20, "M", 60000),
    ("Hermion", "Granger", 20, "F", 50000),
    ("Ron", "Weasly", 20, "M", 50000),
    ("Ginny", "Weasly", 16, "F", 40000)"""

try:
    cursor.execute(sql_insert)
    db.commit()
    print("Rows inserted successfully!")
except Exception as e:
    print(f"Error: {e}")
    db.rollback()
finally:
    db.close()


# # quering all the records from EMPLOYEE table having salary more than 25000

# import pymysql

# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="abcd4321",
#     database="testdb"
# )

# cursor = db.cursor()

# sql = "SELECT * FROM EMPLOYEE \
#       WHERE INCOME > '%d'" % (25000)
# try:
#    cursor.execute(sql)
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#       print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
#          (fname, lname, age, sex, income ))
# except:
#    print ("Error: unable to fetch data")

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
    