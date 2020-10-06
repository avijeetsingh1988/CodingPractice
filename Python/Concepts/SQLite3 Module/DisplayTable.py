import sqlite3

conn=sqlite3.connect('employee.db')
c=conn.cursor()

c.execute('SELECT * FROM Employees')

#The above statement tells us what output we want 
#In order to see the output in python we need to use the print statement along with the fetch arguments.

print(c.fetchall())

conn.commit()
conn.close()
