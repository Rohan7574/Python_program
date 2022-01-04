st=int(input("Enter Student Number :"))
total=0
for i in range(st):
    name=input("Enter Student Name :")
    sub=int(input("Enter student's subject :"))
    for j in range(sub):
        marks=int(input("Enter Marks :"))
        total=total+marks
        pr=total/sub
    print("Total is :",total)
    print("pr is :",pr)