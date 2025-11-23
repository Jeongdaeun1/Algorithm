from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M =  map(int, input().split())
# N : 정점 수, M : 간선 수

graph = [[False]*(N+1) for i in range(N+1)]
#전부다 False 상태인 행렬

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
#인접 행렬 생성 완료


visited = [False]*(N+1)
#방문 여부 담기

#DFS
def DFS(v):
    visited[v]=True #첫번째 노드는 무조건 방문하고 시작하기 때문에 방문 처리
    #print(v, end=" ") #방문한 즉시 출력
    for i in range(1, N+1):
        if not visited[i] and graph[v][i]==1:
            DFS(i)



#BFS
def BFS(v):
    q = deque([v])
    visited[v] = True

    while q: #queue안에 데이터 없을 때 까지 실행
        v = q.popleft()
        #print(v, end=" ")
        for i in range(1, N+1):
            if not visited[i] and graph[v][i] == 1:
                q.append(i)
                visited[i] = True
cnt = 0
for i in range(1, N + 1): # 정점 번호 1부터 N까지 순회하며 검사
    if not visited[i]: # 아직 방문하지 않은 정점을 찾으면
        BFS(i)    # DFS/BFS 시작 (새로운 연결 요소 발견)
        cnt += 1

print(cnt)