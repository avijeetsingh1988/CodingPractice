class Emp:
    def __init__(self,first,last,age,occ):
        self.first = first
        self.last = last
        self.age = age
        self.occ = occ

import sqlite3

## making the connection and initiating the cursor

conn=sqlite3.connect('employee.db')
c=conn.cursor()

## creating an object of class employee

emp1 = Emp('Bhagat','Singh',50,'Freedom Fighter')

##inserting this into the db using the :key method (preferred method)
## commenting out the below section because otherwise it will keep adding the values to the list

# c.execute("INSERT INTO Employees VALUES (:first,:last,:age,:occ)",{'first':emp1.first,'last':emp1.last,'age':emp1.age,'occ':emp1.occ})
# conn.commit()

c.execute("SELECT * FROM Employees WHERE Lastname = 'Singh'")
print(c.fetchall())

conn.commit()
conn.close()