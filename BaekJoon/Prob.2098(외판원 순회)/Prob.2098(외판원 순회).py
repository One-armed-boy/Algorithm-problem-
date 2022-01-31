import sys
input=sys.stdin.readline

N=int(input()) # 도시의 수 입력

graph=[list(map(int,input().split())) for i in range(N)] # 도시 간 이동에 소요되는 비용 행렬 입력

dp=[[sys.maxsize]*(1<<N) for i in range(N)] # 비트 연산자를 이용한 이유는 각 도시의 방문 여부를 리스트가 아닌 하나의 수(visited)로 기록하여 메모리를 절약하기 위함

def DFS(n,r=0,visited=1): # 초기 visited 값은 시작 도시 하나를 방문한 상태를 나타내어야 하므로 1(2) = 1 의 값을 가짐 
    if visited==(1<<n)-1: # visited 값이 1<<(도시의 수) -1 과 같아진다는 것의 의미는 결국 모든 도시를 방문했다는 것
        if graph[r][0]!=0: # 만약 모든 도시를 방문한 상태에서 시작점으로 돌아가는 비용이 0이 아니라는 것은 시작점으로 갈 수 있다는 것
            return graph[r][0]
        else:
            return sys.maxsize # 만약 현 위치에서 시작점으로 갈 수 없다면 해당 경우의 비용을 무한대로 줌으로서 해당 경로 폐기
    if dp[r][visited]!=sys.maxsize: # 만약 이전에 이미 탐색한 경로라면 이전에 구한 값을 그대로 이용
        return dp[r][visited]

    for i in range(n):
        if visited & (1<<i): # 만약 다음 목적지 i를 이미 방문했다면 해당 경우는 skip
            continue
        if graph[r][i]==0: # 만약 다음 목적지 i로 가는 경로가 없을 경우 해당 경우는 skip
            continue

        dp[r][visited]=min(dp[r][visited],DFS(n,i,visited|(1<<i))+graph[r][i]) 
        # dp[r][visited]: visited를 방문했고 현재 r에 있을 때 나머지 도시들을 모두 방문하는데 드는 최소 비용
    return dp[r][visited]

print(DFS(N))
