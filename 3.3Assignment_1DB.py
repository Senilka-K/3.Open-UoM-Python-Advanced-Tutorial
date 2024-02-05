import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="abcd4321",
    database="assignment_1db"   
)

cursor = db.cursor()

sql = """ CREATE TABLE STUDENT (
    STUDENT_NO INT,
    SURNAME CHAR(20),
    FORENAME CHAR(20)) """

cursor.execute(sql)

db.close()

# sql_insert = """ INSERT INTO STUDENT (STUDENT_NO, SURNAME, FORENAME)
# VALUES
#     (20060101, "Dickens", "Charles"),
#     (20060102, "ApGwilym", "Dafydd"),
#     (20060103, "Zola", "Emile"),
#     (20060104, "Mann", "Thomas"),
#     (20060105, "Stevenson", "Robert")
# """

# try:
#     cursor.execute(sql_insert)
#     db.commit()
#     print("Rows inserted successfully!")
# except Exception as e:
#     print(f"Error: {e}")
#     db.rollback()
# finally:
#     db.close()
