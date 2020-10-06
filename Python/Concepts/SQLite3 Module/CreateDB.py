
import sqlite3

#following creates or connects to a database in the current directory
conn=sqlite3.connect('employee.db')

#following creates a cursor for the above database. We need this to execute commands in sql
c=conn.cursor()

c.execute("""CREATE TABLE Employees (
    Firstname TEXT, 
    Lastname TEXT, 
    Age INTEGER)""")

#To push changes into the table we need to commit
conn.commit() 
conn.close()