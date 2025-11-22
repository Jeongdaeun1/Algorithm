from collections import deque

N, M, V = map(int, input().split()) 
# N : 정점 수, M : 간선 수 , V : 시작 노드 번호

graph = [[False]*(N+1) for i in range(N+1)]
#전부다 False 상태인 행렬

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
#인접 행렬 생성 완료

visited = [False]*(N+1)
visited2 = [False]*(N+1)
#방문 여부 담기

#DFS
def DFS(v):
    visited[v]=True #첫번째 노드는 무조건 방문하고 시작하기 때문에 방문 처리
    print(v, end=" ") #방문한 즉시 출력
    for i in range(1, N+1):
        if not visited[i] and graph[v][i]==1:
            DFS(i)



#BFS
def BFS(v):
    visited = [False]*(N+1)
    q = deque([v])
    visited[v] = True

    while q: #queue안에 데이터 없을 때 까지 실행
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N+1):
            if not visited[i] and graph[v][i] == 1:
                q.append(i)
                visited[i] = True

DFS(V)
print()
BFS(V)