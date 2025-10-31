n = int(input())
age_list =[]
name_list =[]
student_list=[]
for i in range(n):
    age, name = input().split()
    student_list.append((int(age),i,name))
student_list.sort()


for i in range(n):
    print(student_list[i][0], end="")
    print(" ", end="")
    print(student_list[i][2])