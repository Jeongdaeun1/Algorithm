n = int(input())
dp = [1]*n #뭔가 앞에서도 다 배열을 만들어서 만들어봄

seq = list(map(int, input().split()))
for i in range(n):#시퀀스 전체를 돌자
    for j in range(i): #i인 상태에서 0~i까지 돌자
        if seq[j]<seq[i] and dp[i]<=dp[j]: #자기 보다 작은 seq인데, dp가 자기보다 크면 자신의 dp를 업데이트
            dp[i] = dp[j]+1
print(max(dp))