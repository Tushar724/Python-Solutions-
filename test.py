l=[1,2,3,1,5,3,5,1,9,0, 1,2,3,1,5,3,5,1,9,0]
number = int(input())
i=0
while i<len(l):
    if i == number:
        print(l.index(i))
    i+=1
    
        
