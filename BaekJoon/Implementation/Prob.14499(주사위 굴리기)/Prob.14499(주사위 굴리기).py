import sys
input=sys.stdin.readline

N,M,Y,X,K=map(int,input().split()) # 지도의 세로,가로, 초기 주사위의 위치, 이동 명령의 수 입력

board=[list(map(int,input().split())) for i in range(N)] # 지도 구성

move=list(map(int,input().split()))

dice=[0]*6 # 주사위의 육면을 len=6 리스트로 구현

def dice_move(status,mov,x,y):
    new_status=[0]*6 # 이동 명령을 수행한 후의 주사위 상태를 
    if mov==1: # 동쪽으로 이동
        if x+1>=M:
            return status,x,y
        x+=1
        if board[y][x]==0:
            board[y][x]=status[1]
        else:
            status[1]=board[y][x]
            board[y][x]=0
        new_status[0] =status[3]
        new_status[1] =status[0]
        new_status[2] =status[1]
        new_status[3] =status[2]
        new_status[4] =status[4]
        new_status[5] =status[5]

    elif mov==2: # 서쪽으로 이동
        if x-1<0:
            return status,x,y
        x-=1
        if board[y][x]==0:
            board[y][x]=status[3]
        else:
            status[3]=board[y][x]
            board[y][x]=0
        new_status[0] = status[1]
        new_status[1] = status[2]
        new_status[2] = status[3]
        new_status[3] = status[0]
        new_status[4] = status[4]
        new_status[5] = status[5]

    elif mov==3: # 북쪽으로 이동
        if y-1<0:
            return status,x,y
        y-=1
        if board[y][x]==0:
            board[y][x]=status[4]
        else:
            status[4]=board[y][x]
            board[y][x]=0
        new_status[0] = status[5]
        new_status[1] = status[1]
        new_status[2] = status[4]
        new_status[3] = status[3]
        new_status[4] = status[0]
        new_status[5] = status[2]
    else: # 남쪽으로 이동
        if y+1>=N:
            return status,x,y
        y+=1
        if board[y][x]==0:
            board[y][x]=status[5]
        else:
            status[5]=board[y][x]
            board[y][x]=0
        new_status[0] = status[4]
        new_status[1] = status[1]
        new_status[2] = status[5]
        new_status[3] = status[3]
        new_status[4] = status[2]
        new_status[5] = status[0]
    print(new_status[0])
    return new_status,x,y

for i in move: # 이동 명령 리스트를 순회하며 주사위를 문제 조건에 따라 
    dice,X,Y=dice_move(dice,i,X,Y)
