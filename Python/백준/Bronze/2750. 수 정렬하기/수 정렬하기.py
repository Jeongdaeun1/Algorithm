n = int(input())
numlist = []
for i in range(n):
    numlist.append(int(input()))
numlist.sort(reverse=True)
for i in range(n):
    print(numlist.pop())