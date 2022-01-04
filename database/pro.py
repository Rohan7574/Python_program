import sqlite3 
def connection():
    a=sqlite3.connect('data.db')
    return a

def table(a):
    a.execute('''CREATE TABLE IF NOT EXISTS NEW(NAME TEXT,AGE INT)''')

def insert(a):
    i=int(input("how many data:"))
    for j in range(i):
        x=input("enter name:")
        y=int(input("enter age:"))
        a.execute("insert into NEW(NAME,AGE) values(?,?)",(x,y))

obj=connection()
table(obj)
insert(obj)
obj.commit()
obj.close()
