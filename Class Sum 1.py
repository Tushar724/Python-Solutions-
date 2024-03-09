def sum_of_not6(m,n):
    sumnot = 0
    sumd = 0
    for i in range(1,n+1):
        if i%m != 0:
            sumnot += i
        if i%m == 0:
            sumd +=  i
        d = sumnot - sumd
        return sumd
    
  



        
        
            


'''n = int(input())
m = int(input())
sum1 = 0
sum_not = 0
for i in range(1,n+1):
    if i%m != 0:
        sum1 += i
    if i%m == 0:
        sum_not += i
print(sum1)
print(sum_not)
print(sum1 - sum_not)'''
            
