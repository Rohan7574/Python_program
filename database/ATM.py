import sqlite3
from sqlite3.dbapi2 import Cursor
penny=[]
GG=[]
def connection():
    a = sqlite3.connect('ATM03.db')
    return a

def createTab(a):
    a.execute('''CREATE TABLE ATM03(AC INTEGER  PRIMARY KEY, NAME TEXT,PASSWORD INT,AMOUNT INT)''')

def Insert(a):
    n = int(input("Enter How Many People :"))
    for i in range(n):
        AA0 = input("Enter your account number :")
        AA1 = input("Enter Your Name :")
        AA2  = int(input("Create Your 4 Digit Password Here :"))
        AA3 = int(input("Enter Amount :"))
        a.execute("INSERT INTO ATM03(AC,NAME,PASSWORD,AMOUNT) VALUES(?,?,?,?)",(AA0,AA1,AA2,AA3))

def retrieve(a):
    cursor = a.cursor()
    id = int(input("Enter Your AC :"))
    User = int(input("Enter Your PIN :"))
    penny.append(id)
    B1 = "SELECT * FROM ATM03 WHERE AC =?"
    A1 = "SELECT * FROM ATM03 WHERE PASSWORD=?"
    if A1 and B1 :
        cursor.execute(A1,(User,))
        cursor.execute(B1,(AC,))
        rows =  cursor.fetchall() 
    for row in rows:
        continue  
    if row[0]==AC and row[2]==User:
        print("**\tWelcome To Online ATM :)")
        class atm():
            def amount(self,a):
                self.a=a
                return self.a
            def deposit(self,b):
                self.b=b
                self.a=self.a+self.b
                return self.a
            def withdraw(self,c):
                self.c=c
                self.a=self.a-self.c
                return self.a
            def finalamount(self):
                return self.a

        x=atm()
        n=row[3]
        print(x.amount(n))
        while True:
            print("\n1 --> deposit")
            print("2 --> withdraw")
            z=int(input("Please enter 1 or 2 :"))
            if z==1:
                nn=int(input("Enter Amount To Deposit :"))
                print(x.deposit(nn))
            elif z==2:
                nnn=int(input("Enter Amount To Withdraw :"))
                print("Remaining Balance :",x.withdraw(nnn))
            else:
                print("Final Balance in your Account :",x.finalamount())
                GG.append(x.finalamount())
                break

    else:
        print("\tData Match Not Found :(")
        print("<<< Try Again >>>")
        retrieve(a)

def update(a):
    cursor=a.cursor()
    hq=penny[0]
    fc=GG[0]
    zef="UPDATE ATM03 SET AMOUNT=? WHERE AC=?"
    cursor.execute(zef,(fc,hq))
    
X = connection()
createTab(X)
A1 = Insert(X)
retrieve(X)
update(X)
X.commit()
X.close()



