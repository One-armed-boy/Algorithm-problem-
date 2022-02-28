import sys
input=sys.stdin.readline
import copy # DFS 탐색 시 리스트 참조 문제를 해결하기 위한 깊은 복사를 위해 선언

N=int(input())
board=[list(map(int,input().split())) for i in range(N)] # 초기 보드를 선언받기 위한 입력 구문
result=0 # 결과 값을 입력하기 위함
best=sum(map(sum,board)) # 가지치기를 위해, 초기 입력 상태에서 도출될 수 있는 최고 결과값을 저장 

def board_change(stat,dir): # board의 상태와, 이동시킬 방향을 입력하면 문제 조건 대로 board를 이동 시킨 뒤 반환하는 함수 선언
    visit = [[False for i in range(N)] for j in range(N)] # 한 번의 이동에서 수가 합쳐지는 것은 두개의 수만 가능하므로 이를 확인하기 위한 visit 배열
    status=copy.deepcopy(stat) # 참조 문제를 해결하기 위한 deepcopy
    if dir==0:
        for y in range(1,N):
            for x in range(N):
                if status[y][x]!=0:
                    step=0
                    while N>y-step-1>=0 and status[y-step-1][x]==0:
                        step+=1
                    if N>y-step-1>=0 and status[y-step-1][x]==status[y][x] and visit[y-step-1][x]==False:
                        step+=1
                        visit[y-step][x]=True
                    if step!=0:
                        status[y-step][x]+=status[y][x]
                        status[y][x]=0
    elif dir==1:
        for y in range(N):
            for x in range(N-1,-1,-1):
                if status[y][x]!=0:
                    step=0
                    while N>x+step+1>=0 and status[y][x+step+1]==0:
                        step+=1
                    if N>x+step+1>=0 and status[y][x+step+1]==status[y][x] and visit[y][x+step+1]==False:
                        step+=1
                        visit[y][x+step]=True
                    if step!=0:
                        status[y][x+step]+=status[y][x]
                        status[y][x]=0
    elif dir==2:
        for y in range(N-1,-1,-1):
            for x in range(N):
                if status[y][x]!=0:
                    step=0
                    while N>y+step+1>=0 and status[y+step+1][x]==0:
                        step+=1
                    if N>y+step+1>=0 and status[y+step+1][x]==status[y][x] and visit[y+step+1][x]==False:
                        step+=1
                        visit[y+step][x]=True
                    if step!=0:
                        status[y+step][x]+=status[y][x]
                        status[y][x]=0
    else:
        for y in range(N):
            for x in range(1,N):
                if status[y][x]!=0:
                    step=0
                    while N>x-step-1>=0 and status[y][x-step-1]==0:
                        step+=1
                    if N>x-step-1>=0 and status[y][x-step-1]==status[y][x] and visit[y][x-step-1]==False:
                        step+=1
                        visit[y][x-step]=True
                    if step!=0:
                        status[y][x-step]+=status[y][x]
                        status[y][x]=0
    return status
  
def solve(stat,cnt): # dfs 탐색 구문
    global result
    tmp=max(result,max(map(max,stat)))
    if tmp>=best:
        global stop
        result=tmp
        stop=False # 만약 board에서 나올 수 있는 best 값을 이미 현 상태에서 가지고 있다면, 그 이후 탐색을 모두 skip하기 위해 stop=False 
        return
      
    if cnt==5:
        result=max(result,tmp)
        return

    for i in range(4):
        if stop:
            solve(board_change(stat,i),cnt+1)
        else:
            break
stop=True
solve(board,0)
print(result)
