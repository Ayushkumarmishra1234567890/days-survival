from datetime import date
print("WELCOME TO THE MINI PROJECT")
print("YOU NEED TO ENTER YOUR DATE OF BIRTH AND CURRENT DATE AND GET NUMBER OF DAYS YOU SURVIVED")
bda=input("enter your date of birth in DD/MM/YYYY format :")
cda=input("enter current date in DD/MM/YYYY format :")
d1=int(bda[0:2])
m1=int(bda[3:5])
y1=int(bda[6:])
d2=int(cda[0:2])
m2=int(cda[3:5])
y2=int(cda[6:])
ini=date(y1,m1,d1)
last=date(y2,m2,d2)
k=str(last-ini).split(",")
if k[0]>"0":
    print(k[0])
else:
    print("you have entered wrong dates")
if m1==m2 and d1==d2:
    print("HAPPY BIRTHDAY")

