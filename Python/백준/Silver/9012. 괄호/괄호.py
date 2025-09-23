n = int(input())
li=[]


for i in range(n):
    li = list(input())
    temp=0
    answer=True
    stk =[]
    for j in range(len(li)):
        if li[temp] == '(':

            stk.append('(')
            temp+=1
        elif li[temp] == ')':
            if stk.count('(') >0 :
                stk.pop()
                temp +=1
            else :
                answer=False
                temp +=1
    if answer == True and stk.count('(') ==0 :
        print("YES")
    else : print("NO")