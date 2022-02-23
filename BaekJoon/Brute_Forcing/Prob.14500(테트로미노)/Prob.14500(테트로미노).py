import sys
input=sys.stdin.readline # 빠른 입력을 위한 sys.stdin.readline

N,M=map(int,input().split()) # 종이의 세로, 가로 사이즈 입력
paper=[list(map(int,input().split())) for i in range(N)]
visited=[[False for i in range(M)]for j in range(N)] # DFS 탐색에 이용할 방문 여부 체크 리스트

dy=[0,0,1,-1]
dx=[1,-1,0,0]
# 탐색 시 이용될 방향 좌표

max_val=max(map(max,paper))# 탐색 시 Early Prunning에 이용될 종이에 적힌 최대 값
# Early Prunning
# 문제를 풀면서 pypy로는 아슬아슬하게 통과하나 Python으로는 시간 초과 문제가 계속되어 해결 방법을 찾다가 발견
# 탐색 중 현재 함수 값을 최대로 개선시킨 값이 이전 탐색들에서 구한 지역 최적값보다 좋지 않다면 해당 탐색을 더 이어가지 않고 사전에 가지치기

def solve(next_y,next_x,result,cnt=1):
    global Max
    if Max>= result+(4-cnt)*max_val: # Early Prunning을 위한 if 문, 현재 상황에서 최대로 개선한 값이 사전에 구해놓은 최적값보다 열등할 시, 해당 탐색을 사전 종료
        return
    if cnt==4: # 4개를 모두 구한 상황이라면 Max 값 갱신
        Max=max(Max,result)
    else:
        for i in range(4):
            ty=next_y+dy[i]
            tx=next_x+dx[i]
            if 0<=ty<N and 0<=tx<M and visited[ty][tx]==False:
                if cnt==2: 
                  # 정사각형을 3개까지 선택한 상황에서 가장 나중에 선택된 도형에서 탐색을 하는 것이 아닌, 
                  # 그 전 단계에서 탐색을 할 경우 테트로미노 도형 중 ㅗ 모양을 구현할 수 있다
                    visited[ty][tx]=True
                    solve(next_y,next_x,result+paper[ty][tx],cnt+1) # visited=True -> 재귀 -> visited=False 구조: DFS 구조를 구현하기 위한 방식
                    visited[ty][tx]=False
                visited[ty][tx]=True
                solve(ty,tx,result+paper[ty][tx],cnt+1)
                visited[ty][tx]=False
Max=0
for y in range(N):
    for x in range(M):
        visited[y][x]=True
        solve(y,x,paper[y][x]) # visited=True -> 재귀 -> visited=False 구조: DFS 구조를 구현하기 위한 방식
        visited[y][x]=False
print(Max)
