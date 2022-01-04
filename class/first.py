class one():
    def __init__(self,b):
        self.b=b


    def balance(self):

        return self.b
    def deposite(self):
        a=int(input("Enter amount you want to deposite:"))
        self.b+=a
        return self.b
    def withdraw(self):
        c=int(input("Enter amount you want to withdraw:"))
        self.b-=c
        return self.b
for i in range(0,3):
    a=8623
    b=int(input("Enter your pin:"))
    if b==a:
        print("Correct pin:")
        break
    while True:
            print("\t\t:: WELCOME ::")
            print("1:- For Check Your Balance  :")
            print("2:- For Deposite Money      :")
            print("3:- For Withdrew Money      :")
            print("4:- For Exit                :")

            ch=int(input("Enter Your Choice :- "))

            obj=one(1000)
            if ch==1:
                print("Your Balance Is :",obj.balance())
            elif ch==2:
                print("You Deposite :",obj.deposite())
            elif ch==3:
                print("You Withdraw :",obj.withdraw())
            else:
                break

    else:
        print("Incorrect pin:")
    