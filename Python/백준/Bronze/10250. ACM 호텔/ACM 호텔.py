casenum = int(input())
for i in range(casenum):
    h, w, n = map(int, input().split())
    temp = n%h
    temp2 = n//h +1
    if (temp==0):
        temp = h
        temp2 -=1
    answer = temp*100 + temp2
    print(answer)