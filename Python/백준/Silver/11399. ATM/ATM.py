n = int(input())
numli = []
numli = list(map(int, input().split()))

numli.sort() # 오름차순으로 변경
sum=0
for i in range(n):
    sum+=numli[i]*(n-i)

print(sum)