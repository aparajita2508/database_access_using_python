# DELETE Operation

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "root", "TESTDB")

#prepare a cursor object using cursor() method
cursor = db.cursor()

#Prepare SQL querry to DELETE required records

sql = "DELETE from employee where age > '%d'" %(20)
try:
    # Execute the SQL command
    cursor.execute(sql)
    db.commit()

except:
    db.rollback()

db.close()
