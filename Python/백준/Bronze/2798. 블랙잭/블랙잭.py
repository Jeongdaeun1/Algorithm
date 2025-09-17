N, M = map(int,input().split())
cards = []
cards = list(map(int, input().split()))
max_sum =0
# 1. 첫 번째 카드를 선택하는 반복문 (n은 0부터 N-3까지)
for n in range(N - 2):
    # 2. 두 번째 카드를 선택하는 반복문 (m은 첫 번째 카드 다음부터 N-2까지)
    for m in range(n + 1, N - 1):
        # 3. 세 번째 카드를 선택하는 반복문 (k는 두 번째 카드 다음부터 끝까지)
        for k in range(m + 1, N):
            
            # 세 카드의 합 계산
            current_sum = cards[n] + cards[m] + cards[k]
            
            # M을 넘지 않으면서, 이전에 찾은 최댓값보다 크면 업데이트
            if current_sum <= M and current_sum > max_sum:
                max_sum = current_sum

# 최종 결과 출력
print(max_sum)