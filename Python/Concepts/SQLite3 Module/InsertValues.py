import sqlite3

conn=sqlite3.connect('employee.db')
c=conn.cursor()

# c.execute("""INSERT INTO Employees VALUES ('Avijeet','Singh',31,'Programmer')""")
# c.execute("""INSERT INTO Employees VALUES ('Parampreet','Caur',28,'Sales')""")
# c.execute("""INSERT INTO Employees VALUES ('Nikhil','Jain',31,'Production Support')""")
# c.execute("""INSERT INTO Employees VALUES ('Tejinder','Aujla',31,'Production Support')""")


c.execute('SELECT * FROM Employees')
print(c.fetchall())
conn.commit()
conn.close()
