n, m = map(int,input().split())
numli = []
for i in range(n):
    numli.append(int(input()))

numli.sort() #오름차순

start =1
end = numli[-1]



ans =0 
mid =0
while start<=end:
    ans =0
    mid = (start + end) //2
    for i in numli:
        ans += i//mid
    if ans < m :
        end = mid - 1
    elif ans >= m :
        result = mid
        start = mid +1


print(result)