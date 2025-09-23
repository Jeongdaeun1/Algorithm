n = int(input())
space =n-1
star =1
for i in range(n):
    print(" "*space,end='')
    print("*"*star)
    space-=1
    star+=1