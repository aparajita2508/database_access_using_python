# # INSERT Operation
#
# import MySQLdb
# db = MySQLdb.connect("localhost", "root", "root", "TESTDB")
# cursor = db.cursor()
#
# # Prepare SQL query to INSERT a record into the database.
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     # Exeute the SQL command.
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db.commit()
# except:
#     #ROllback in case there is any error
#     db.rollback()
#
# db.close()

# Above example can be written as follows to create SQL queries dynamically
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "root", "TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
      ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()

# following exapmle of where u can pass parameters directly
# user_id = "root"
# password = "root"
#
# con.execute('insert into Login values("%s", "%s")' % \
#              (user_id, password))