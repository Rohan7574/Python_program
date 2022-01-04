import sqlite3 

def connection():
    a=sqlite3.connect('new.db')
    return a

def create_t(a):
    a.execute('''CREATE TABLE STUDENT(NAME TEXT,AGE INT,ROLL_NUM INT,MATHS INT,SCIENCE INT,ENGLISH INT)''')
    print("done")

def insert(a):
    i=input("enter name:")
    z=int(input("enter age:"))
    r=int(input("Enter roll number:"))
    m=int(input("Enter number of maths:"))
    s=int(input("Enter number of science:"))
    e=int(input("Enter number of english:"))

    a.execute("INSERT INTO STUDENT(NAME,AGE,ROLL_NUM,MATHS,SCIENCE,ENGLISH) VALUES(?,?,?,?,?,?)",(z,i))
    print("inserted")

o=connection()
insert(o)
o.commit()
o.close()
