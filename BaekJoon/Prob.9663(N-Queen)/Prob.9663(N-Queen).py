import sys

input=sys.stdin.readline

n=int(input()) # 체스판의 사이즈(N X N), 체스판 위에 놓일 Queen의 수

# Queen은 체스판 내에서 동일 행, 열, 좌,우 대각성분에 존재하는 체스 말을 공격 가능하다.
# 따라서 문제 조건을 만족시키기 위해서는 각 줄에 하나 이상의 Queen이 놓여서는 안되기 때문에, 체스판 사이즈에 따른 True,False 리스트를 생성하여 이를 관리하면 탐색이 가능하다.
row=[True for i in range(n)]
column=[True for i in range(n)]
l_dia=[True for i in range(2*n-1)]
r_dia=[True for i in range(2*n-1)]

result=0 # N-Queen이 놓일 수 있는 경우의 수
def solve(row):
    if row==n: # 마지막 row까지 탐색이 진행되었다면 경우의 수 +1
        global result
        result+=1
    else:
         for x in range(n):
            if column[x] and l_dia[row-x+n-1] and r_dia[row+x]: # 좌표 평면 상에서 row는 y값을, x는 x값을 의미하며 그에 따른 column, l_dia, r_dia 상의 인덱스 값으로 반환
                column[x]=False
                l_dia[row-x+n-1]=False
                r_dia[row+x]=False
                solve(row+1) # 다음 단계의 재귀 호출을 기준으로 방문 표시를 했다가 다시 방문 표시를 지움 -> 
                column[x]=True
                l_dia[row-x+n-1]=True
                r_dia[row+x]=True

solve(0) # 첫번째 row부터 탐색 시작
print(result)
