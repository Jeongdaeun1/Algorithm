n = int(input())
numli = []
numli = list(map(int,input().split()))
numli.sort()

m = int(input())

ans = 0
start =0
end = n-1
curr_sum =0

while start < end:
    curr_sum = numli[start] + numli[end]
    if curr_sum == m:
        ans += 1
        start +=1
        end -=1
    elif curr_sum < m:
        start += 1
    elif curr_sum > m:
        end -=1

# 1 2 3 5 7 9 10 11 12


print(ans)