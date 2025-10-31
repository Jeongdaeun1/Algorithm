n, m = map(int, input().split())
s_list=[]
for i in range(n):
    string = str(input())
    s_list.append(string)
count=0

for i in range(m):
    string = str(input())

    if string in s_list:
        count+=1


print(count)