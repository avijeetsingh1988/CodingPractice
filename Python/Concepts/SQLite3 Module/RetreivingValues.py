import sqlite3

conn=sqlite3.connect('employee.db')
c=conn.cursor()

# We use fetch commands to retreive values in python after the SELECT statement : fetchall(),fetchone(),fetchmany(x)
# E.g if we need to get all records with last name singh

c.execute("SELECT * FROM Employees WHERE Lastname ='Singh'")
print(c.fetchall())
conn.commit()
conn.close()

