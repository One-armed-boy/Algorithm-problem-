import sys
from collections import deque #bfs 를 위한 queue 자료구조 이용을 위한 라이브러리

input=sys.stdin.readline

M,N,H=map(int,input().split()) 


tomato=[[list(map(int,input().split())) for j in range(N)] for i in range(H)] # 토마토가 놓인 상자를 3차원 리스트로 구현

visited=[[[True for i in range(M)] for j in range(N)] for k in range(H)] # 각 토마토의 위치에 방문한 적이 있는지 여부를 파악하기 위한 3차원 리스트
dh=[0,0,0,0,1,-1]
dy=[0,0,1,-1,0,0]
dx=[1,-1,0,0,0,0]
# 어떤 토마토가 인접한 토마토에 영향을 끼칠 수 있는 방향에 대한 리스트

def bfs():
    que=deque()
    day=0
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[h][y][x]==1:
                    que.append([h,y,x,0]) # 3차원 리스트에서 익은 토마토의 위치를 파악하여 이를 que에 [h,y,x,day] 리스트로 삽입 
    while que:
        tmp=que.popleft() # 빠른 날짜 순으로 뽑아내고 뒤의 날짜를 후순위에 두기 위해(FIFO) queue의 가장 앞의 요소 반환
        if day<tmp[3]: # 토마토가 익은 날짜 중 최대값을 파악하기 위함
            day=tmp[3]
        visited[tmp[0]][tmp[1]][tmp[2]]=False 
        # visited의 값을 True(방문 x)에서 False(방문 o)로 바꿈, 만약 토마토가 놓이지 않은 위치였다면 다시 방문할 일이 없고, 
        # 만약 놓여있었다면 이미 토마토는 익었기 때문에 마찬가지로 방문할 일이 없음
        
        for i in range(6): # 익은 토마토가 영향을 줄 수 있는 방향은 총 6방향
            th=tmp[0]+dh[i]
            ty=tmp[1]+dy[i]
            tx=tmp[2]+dx[i]
            if 0<=th<H and 0<=ty<N and 0<=tx<M:
                if tomato[th][ty][tx]==0 and visited[th][ty][tx]:
                    tomato[th][ty][tx]=1
                    que.append([th,ty,tx,tmp[3]+1])
                    # 다음 이동 위치가 상자 안이고, 익지 않은 토마토가 존재하며 아직 방문하지 않았다면, tmp[3]+1일 째 익은 토마토로 간주하고 que에 삽입
    a=True
    b=True
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[h][y][x]==0: # 만약 익지 않은 토마토가 있다면 -1 출력, 그렇지 않다면 마지막 토마토가 익은 날짜를 
                    day=-1
                    a=False
                    b=False
                    break
            if a==False:
                break
        if b==False:
            break
    return day
print(bfs())
