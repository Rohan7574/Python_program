
paragraph='''One of princely india's most magnificent palaces. 130 years old palace was 
                built by the legendary Maharaja Sayajirao Gaekwar...!'''
print("/t/t :Select your choice of operation:")
print("1:- FOR SPLIT,LENGTH :")
print("2:- FOR REPLACE :")

ch=int(input("Enter your choice of operation :"))

if ch==1:
    a=paragraph.split( )
    print(a)
    b=len(a)
    print("Length of paragraph :",b)
    

elif ch==2:
    rep=input("Enter where you want to replace :")
    rep2=input("Enter what you want to replace :")

    a=paragraph.replace(rep,rep2)
    print(a)
        

        