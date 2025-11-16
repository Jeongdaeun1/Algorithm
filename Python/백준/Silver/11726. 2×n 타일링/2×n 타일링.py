n = int(input())
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    temp = [0 for i in range(n)] #이렇게 0 n개 채우기
    temp[0] = 1
    temp[1] = 2
    i=2
    while i<n:
        temp[i]  = (temp[i-1]+ temp[i-2])%10007
        i+=1
    print(temp[n-1])