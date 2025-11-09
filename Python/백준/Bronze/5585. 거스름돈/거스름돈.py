n = int(input())
coins=[500,100,50,10,5,1]
count =0
n=1000-n
while n !=0:
    for coin in coins:
        remain = n%coin
        quo = n//coin
        count +=quo
        n=remain
print(count)