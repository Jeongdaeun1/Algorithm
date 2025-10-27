import heapq
import sys

input = sys.stdin.readline

n = int(input())
numli = []

for i in range(n):
    num = int(input())
    
    if num == 0:
        if len(numli) == 0:
            print(0)
        else:
            print(heapq.heappop(numli))
    else:
        heapq.heappush(numli, num)