n = int(input())
for i in range(n):
    N, M = map(int, input().split())
    temp = 1
    for j in range(N):
        temp= temp*M
        M-=1
    for j in range(N):
        temp = temp//N
        N-=1
    print(temp)