import sqlite3

#always first connect to the Database and create the cursor
conn=sqlite3.connect('employee.db')
c=conn.cursor()

#use SQL SYNTAX  alter the table or perform any operation to the table
c.execute("""ALTER TABLE Employees ADD Occupation TEXT""")

conn.commit()
conn.close()
