import sqlite3

def stu():
    a=sqlite3.connect('stu_task.db')
    return a
def create_t(a):
    a.execute('''CREATE TABLE STUDENT(NAME TEXT,ROLL_NUM INT)''' )
    print("done")
def insert(a):

    a.execute('''INSERT INTO STUDENT(NAME,ROLL_NUM)VALUES('ROHAN',42)''')
    print("Inserted")
o=connection()
insert(o)
o.commit()
o.close()