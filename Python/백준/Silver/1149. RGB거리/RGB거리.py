n = int(input())
houselist=[0]*n #여기에 비용 정보 저장
dp=[] 
for i in range(n):
    houselist[i] = list(map(int, input().split()))

for i in range(1, n):
    houselist[i][0] = min(houselist[i-1][1],houselist[i-1][2]) + houselist[i][0]
    houselist[i][1] = min(houselist[i-1][0],houselist[i-1][2]) + houselist[i][1]
    houselist[i][2] = min(houselist[i-1][1],houselist[i-1][0]) + houselist[i][2]

print(min(houselist[n-1][0], houselist[n-1][1], houselist[n-1][2]))