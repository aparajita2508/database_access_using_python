#Update Operation

import traceback
import MySQLdb
db = MySQLdb.connect("localhost", "root", "root", "TESTDB")
cursor = db.cursor()
sql = "SELECT * FROM EMPLOYEE  \
      WHERE INCOME > '%d' " % (1000)

# Prepare SQL query to UPDATE required records

sql1 = "UPDATE EMPLOYEE SET AGE = AGE+1 \
        WHERE SEX = '%c'" %('M')
try:
    #Execute the SQL command
    cursor.execute(sql1)
    db.commit()
    cursor.execute(sql)

    #Fetch all the rows in a list of list.
    results = cursor.fetchall()
    for row in results:
        FIRST_NAME = row[0]
        LAST_NAME = row[1]
        AGE = row[2]
        SEX = row[3]
        INCOME = row[4]
        # Now print fetched result
        print "fname = %s, lname = %s, age = %d, sex = %c, income = %d" % \
              (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
except Exception as e:
    db.rollback()
    print "Error: unable to fetch data"+ str(e)
    print traceback.print_exc(50)

db.close