N = int(input())

# 5kg 봉지를 최대한 많이 사용하여 시작
for i in range(N // 5, -1, -1):
    remaining = N - i * 5
    # 남은 설탕이 3kg 봉지로 나누어 떨어지는지 확인
    if remaining % 3 == 0:
        # 최소 봉지 개수 계산
        print(i + (remaining // 3))
        break
else:
    # 어떤 방법으로도 정확히 N kg을 만들 수 없는 경우
    print(-1)
