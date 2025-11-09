n = int(input())
numli=[]
for i in range(n):
    numli.append(int(input()))

numli.sort()

max_weight = 0
for i in range(n):
    if (numli[i])*(n-i)>= max_weight:
        max_weight = (numli[i])*(n-i)

print(max_weight)