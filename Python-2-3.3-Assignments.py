import pymysql

try:
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="abcd4321",
        database="assignment_1db"   
    )

    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS STUDENT")

    create_student_table = """ CREATE TABLE STUDENT (
        STUDENT_NO INT,
        SURNAME CHAR(20),
        FORENAME CHAR(20))"""
    
    cursor.execute(create_student_table)

    cursor.execute("DROP TABLE IF EXISTS MODULE")

    create_module_table = """ CREATE TABLE MODULE (
        MODULE_CODE CHAR(20),
        MODULE_NAME CHAR(20))"""
    
    cursor.execute(create_module_table)

    cursor.execute("DROP TABLE IF EXISTS MARKS")
    
    create_marks_table = """ CREATE TABLE MARKS (
        STUDENT_NO INT,
        MODULE_CODE CHAR(20), 
        MARK INT)"""
    
    cursor.execute(create_marks_table)

    sql_insert_student = """ INSERT INTO STUDENT (STUDENT_NO, SURNAME, FORENAME)
    VALUES
        (20060101, "Dickens", "Charles"),
        (20060102, "ApGwilym", "Dafydd"),
        (20060103, "Zola", "Emile"),
        (20060104, "Mann", "Thomas"),
        (20060105, "Stevenson", "Robert")"""

    cursor.execute(sql_insert_student)

    sql_insert_module = """ INSERT INTO MODULE (MODULE_CODE, MODULE_NAME)
    VALUES
        ("CM0001", "Databases"),
        ("CM0003", "Operating Systems"),
        ("CM0004", "Graphics")"""
    
    cursor.execute(sql_insert_module)

    sql_insert_marks = """ INSERT INTO MARKS (STUDENT_NO, MODULE_CODE, MARK )
    VALUES
        (20060101, "CM0001", 80),
        (20060101, "CM0002", 65),
        (20060101, "CM0003", 50),
        (20060102, "CM0001", 75),
        (20060102, "CM0003", 45),
        (20060102, "CM0004", 70),
        (20060103, "CM0001", 60),
        (20060103, "CM0002", 75),
        (20060103, "CM0004", 60),
        (20060104, "CM0001", 55),
        (20060104, "CM0002", 40),
        (20060104, "CM0003", 45),
        (20060105, "CM0001", 55),
        (20060105, "CM0002", 50),
        (20060105, "CM0004", 65)"""

    cursor.execute(sql_insert_marks)

    sql_query = """SELECT STUDENT.FORENAME, AVG(MARKS.MARK) AS AVERAGE_MARK
                   FROM STUDENT
                   INNER JOIN MARKS ON STUDENT.STUDENT_NO = MARKS.STUDENT_NO
                   GROUP BY STUDENT.FORENAME"""

    cursor.execute(sql_query)

    result = cursor.fetchall()

    for row in result:
        forename, average_mark = row
        print(f"Forename: {forename}, Average Mark: {average_mark}")

    db.commit()
    print("Rows inserted successfully!")

except Exception as e:
    print(f"Error: {e}")
    db.rollback()

finally:
    db.close()

