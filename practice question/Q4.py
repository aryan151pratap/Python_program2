a=int(input("Enter any number: "))
b=0

while a>0:
    if a%2==0:
        b=b+a
    a-=1
print(b)
