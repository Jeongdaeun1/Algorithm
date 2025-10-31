import sys

n = int(input())
for i in range(n):
    m = int(input())

    item_list=[]
    item_count = {} #이게 딕셔너리임
    for j in range(m):
        item, itemtype = map(str, input().split())
        item_list.append((item,itemtype))

        current_count = item_count.get(itemtype, 0)
        # 이거는 item_count에서 방금 받은 itemtype이랑 같은게 몇개인지 가져오는것. 
        # 만약에 지금 받은게 처음이라면 0 반환
        item_count[itemtype] = current_count +1
    #print(item_count)
    counts_list = list(item_count.values())
    result=1
    for j in range(len(counts_list)):
        result *= (counts_list[j]+1)

    print(result -1)