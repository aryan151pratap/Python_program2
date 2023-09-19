import random
s=10
b=random.randint(1,100)
while True:
    a=int(input())
    if a==b:
        print("You wins")
        break
    elif a>b:
        print("You are so far")
    elif a<b:
        print("You are so near")
    s-=1
print(s)
    
