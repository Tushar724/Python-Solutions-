n = 100

while n>0:
    b = input("Choose between attack or heal: ")
    if b == "attack":
        n = n-20
        print(n)
    if b == "heal":
        n = n+10
        print(n)
    if n<=0:
        print("dead")
        

