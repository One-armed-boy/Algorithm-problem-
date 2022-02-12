import sys
input=sys.stdin.readline

from collections import deque # queue 자료형을 이용하기 위해 선언

N,M=map(int,input().split()) # 줄세워야할 사람 수 N, 키를 비교한 회수 M 입력

graph={i:[] for i in range(1,N+1)} # 딕셔너리 형태로 그래프 선언, key 가 value보다 앞에 있어야한다

for i in range(M): # 그래프에 사람들의 키를 비교한 결과 입력
    A,B=map(int,input().split())
    graph[A].append(B)

visited=[True for i in range(N+1)] # 이미 줄을 세운 사람인지 확인

result=deque() # 줄 세운 결과를 입력하는 queue

def DFS(v):
    visited[v]=False # 그래프 상에서 방문한 사람에게 방문 표시
    for i in graph[v]: # v보다 뒤에 서야하는 사람들 중 다음 탐색
        if visited[i]:
            DFS(i)
    result.appendleft(v) # 가장 아래 층부터 result의 제일 앞에 채워넣음으로써 문제 조건을 만족

for i in graph: # 문제 조건을 만족한다면 다른 순서는 상관없으므로 for문으로 순차적으로 
    if visited[i]:
        DFS(i)
for i in range(N):
    print(result[i],end=" ")
