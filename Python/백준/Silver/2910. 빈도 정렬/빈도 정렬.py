import sys

n, m = map(int, input().split())
dic = {}
nums = list(map(int, input().split( )))
for num in nums:
    current_count = dic.get(num, 0)
    dic[num] = current_count+1
sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

#print(sorted_dic)
for i in range(len(sorted_dic)):
    repeat = sorted_dic[i][1]
    for j in range(repeat):
        print(sorted_dic[i][0], end=" ")