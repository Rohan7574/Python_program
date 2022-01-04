import sqlite3

d={'name':None,'subjects':None,'marks':None,'total':None,'percentage':None}
def connection():
    a=sqlite3.connect('second.db')
    return(a)

def create(a):
    a.execute('''CREATE TABLE IF NOT EXISTS REPORT(NAME TEXT,SUBJECT TEXT,MARKS TEXT,TOTAL INT, PERCENTAGE INT)''')

def insert(a):
    a.execute('''INSERT INTO REPORT(NAME,SUBJECT,MARKS,TOTAL,PERCENTAGE) VALUES (?,?,?,?,?)''',(d['name'],d['subjects'],d['marks'],d['total'],d['percentage']))
    a.commit()
    

def student(z):
    n=int(input('enter the no.of student : ')) 
    name(n,z)

def name(x,z):
    for i in range(x):
        n=input('\nenter name : ')
        d['name']=n
        sub=int(input('enter no.of subjects :'))
        subject(sub)
        insert(z)       

def subject(sub):
    total=0
    ss=''
    a=''
    for i in range(sub):
        subname=input('enter subject name : ')
        ss=ss+subname+","
        m=marks()
        a=a+str(m)+','
        total=total+m
    
    d['subjects']=ss
    d['marks']=a
    d['total']=total
    totl(i,total)            

def marks():
    score=int(input('enter marks : '))
    return(score)

def totl(i,t):
    percentage(i+1,t)


def percentage(s,t):
    p=t/s
    d['percentage']=str(p)+'%' 

z=connection()
create(z)
student(z)
z.close()