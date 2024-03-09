'''#Q4
n = input()
print(n[::-1])


#Q5
for i in range(0,6):
    if i==3 or i==6:
        continue
    else:
        print(i)

#Q6
for i in range(1,51):
    if i%3==0:
        print("Frizz")
    if i%5==0:
        print("Buzz")
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)

#Q7
n = input()
count = 0
num = 0
for i in n:
    if i.isalpha():
        count+=1
    if i.isnumeric():
        num +=1

print(count)
print(num)'''

n = int(input())
if (1<=n<=9):
        print("well Guessed")
else:
    while (1>n or n>9):
        n = int(input())

