import sqlite3

d={'name':None,'subject':None,'marks':None,'total':None}
def connection():
    a=sqlite3.connect('practice.db')
    return(a)
def create(a):
    a.execute('''CREATE TABLE IF NOT EXISTS REPORTCARD(NAME TEXT,SUBJECT TEXT,MARKS TEXT,TOTAL INT)''')
def insert(a):
    a.execute('''INSERT INTO REPORTCARD(NAME,SUBJECT,MARKS,TOTAL)VALUES(?,?,?,?)''',(d['name'],d['subject'],d['marks'],d['total']))
    a.commit()
def student(z):
    n=int(input("Enter Number of Students :"))
    name(n,z)
def name(x,z):
    for i in range(x):
        n=input("Enter name :")
        d['name']=n
        sub=int(input("Enter subject :"))
        subject(sub)
        insert(z)
def subject(sub):
    total=0
    ss=''
    a=''
    for i in range(sub):
        subname=input("Enter subject name:")
        ss=ss+subname+","
        m=marks()
        a=a+str(m)+","
        total=total+m

    d['subjects']=ss
    d['marks']=m
    d['total']=total

def marks():
    score=int(input("Enter marks:"))
    return(score)
z=connection()
create(z)
student(z)
z.close()