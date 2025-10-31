n= int(input())
rainbow =['ChongChong']
for i in range(n):
    people1, people2 = map(str,input().split())
    
    if people1 in rainbow:
        if people2 not in rainbow:
            rainbow.append(people2)
    elif people2 in rainbow:
        if people1 not in rainbow:
            rainbow.append(people1)
    
    
print(len(rainbow))