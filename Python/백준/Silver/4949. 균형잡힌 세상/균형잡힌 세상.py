while True:
    
    data = input()
    stk =[]
    status = True
    if data == '.':
        break
    temp = [char for char in data if char in "()[]"]
    if len(temp) ==0:
        status = True

    for i in range(len(temp)):
        if temp[i] == '(':
            stk.append(temp[i])
        elif temp[i] =='[':
            stk.append(temp[i])
        elif temp[i] == ')':
            if len(stk)==0:
                status = False
            elif stk[-1]=='(':
                stk.pop()
            elif stk[-1] =='[':
                status = False
        elif temp[i] ==']':
            if len(stk)==0:
                status = False
            elif stk[-1] == '[':
                stk.pop()
            elif stk[-1] == '(':
                status = False
    if len(stk) != 0:
        status = False
    if status == True:
        print("yes")
    else : print("no")
