import math
casenum = int(input())
primenum = 0
count =0
numlist = list(map(int,input().split()))
for i in range(casenum):
    num = numlist[count]
    temp =2
    if num==1:
        primenum += 0
    elif num == 2:
        primenum +=1
    else :
        is_prime = True
        while temp <= math.sqrt(num)+1 :
            if num % temp == 0:
                is_prime = False
                break
            temp += 1 
               
        if is_prime == True:
            primenum +=1
    count+=1
print(primenum)