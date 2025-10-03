n = int(input())
numli = []
for i in range(n):
    numli.append(int(input()))#입력받은 값 리스트에 추가
numli.sort()#오름차순 정렬

ans = 0
maxans =0
for i in range(n):
    ans = numli[i]*(n-i)
    if ans >= maxans:
        maxans = ans

print(maxans)
# 3 - 10 20 30 이면 3개 다 사용시 30, 상위 두개만 사용시 40 그러면 40