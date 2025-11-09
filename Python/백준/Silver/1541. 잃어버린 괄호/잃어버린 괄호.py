s = input()

numbers = []
signs = []
current = ''


for ch in s:
    if ch.isdigit():
        current += ch
    else:  # + or -
        numbers.append(int(current))
        current = ''
        signs.append(ch)

# 마지막 숫자도 넣어줘야 함
if current:
    numbers.append(int(current))

count = 0 
idx=0
index=[]
minus = "-"
plus = "+"
    
if "-" not in signs:
    #+만 있는 상태
    for i in range(len(numbers)):
        count += numbers.pop()
elif "+" not in signs:
    #-만 있는 상태
    count = numbers[0]
    for num in numbers[1:]:
        count -= num
else : 
    #섞여있는 상태
    # 첫번째 - sign의 index 찾기
    for i in range(len(signs)):
        if signs[i] == "-":
            idx = i
            break
    #첫 - 뒤에 있는 기호 다 - 로 바꾸기
    for i in range(len(signs)):
        if i >= idx:
            signs[i] = "-"

    for i in range(len(signs)):
        if signs[i] == "-":
            numbers[i+1] = -numbers[i+1]
    for i in numbers:
        count += int(i)
print(count)