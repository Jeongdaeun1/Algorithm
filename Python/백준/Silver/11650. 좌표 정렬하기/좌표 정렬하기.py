n = int(input())
numli = []
for i in range(n):
    x, y = map(int, input().split())
    numli.append((x,y)) # 좌표형태로 list에 저장


numli.sort() # x좌표 y좌표 순서로 정렬
for i in range(n):
    print(numli[i][0], numli[i][1]) # (1,1) 형태가 아니라 숫자 하나씩 나오게
    i+=1 #하나씩 출력ㅁ