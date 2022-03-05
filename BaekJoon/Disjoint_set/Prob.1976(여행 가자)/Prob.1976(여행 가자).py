import sys
input=sys.stdin.readline

N=int(input())

M=int(input())

city=[list(map(int,input().split())) for i in range(N)] # 도시 사이의 길이 존재하는지 여부를 adjacent matrix 형태로 입력 받음

trip=list(map(int,input().split()))

for i in range(len(trip)):
    trip[i]-=1 # 도시의 이름과 인덱스를 일치시켜 문제를 단순화 하기 위한 -1

parents=[i for i in range(N)]

def find(a): # 분리 집합 문제 해결을 위한 find 함수 구현
    if parents[a]==a:
        return a
    parents[a]=find(parents[a])
    return parents[a]

def union(a,b): # 분리 집합 문제 해결을 위한 union 함수 구현
    pa_a=find(a)
    pa_b=find(b)
    if pa_a!=pa_b:
        if pa_a>pa_b:
            parents[pa_a]=pa_b
        else:
            parents[pa_b]=pa_a
    return

for y in range(N):
    for x in range(y+1,N): # 애초에 입력 받은 matrix city는 diagonal matrix이므로 중복을 피하기 위해 range(y+1,N) 설정
        if city[y][x]==1:
            union(x,y) # 두 도시 사이에 길이 존재하면 같은 집합에 속하는 것으로 여김

result=set(map(find,trip))
if len(result)==1: # 만약 trip의 모든 도시들의 조상이 일치할 경우, 문제 조건을 만족시키는 것으로 YES, 그렇지 않을 경우 NO 
    print('YES')
else:
    print('NO')
