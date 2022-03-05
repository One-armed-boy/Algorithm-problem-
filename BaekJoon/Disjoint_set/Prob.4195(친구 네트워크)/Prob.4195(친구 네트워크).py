import sys
input=sys.stdin.readline

T=int(input()) # 테스트 케이스 수 입력

def find(x): # disjoint set 문제를 위해 find 함수 구현
    if friend[x]==x:
        return x
    friend[x]=find(friend[x])
    return friend[x]

def union(x,y): # ,disjoint set 문제를 위해 union 함수 구현
    parents_x=find(x)
    parents_y=find(y)
    if cnt[parents_x]>cnt[parents_y]: # 친구 네트워크의 수가 적은 쪽을 많은 쪽에 붙임
        friend[parents_y]=parents_x
        cnt[parents_x]+=cnt[parents_y]
    else:
        friend[parents_x]=parents_y
        cnt[parents_y]+=cnt[parents_x]
    return

for _ in range(T):
    F=int(input())
    friend={} # 서로소 집합
    cnt={} # 집합 내 요소들의 수를 조상을 key 값으로 갖는 딕셔너리로 표현
    for i in range(F):
        a,b=input().split()
        if a not in friend:
            friend[a]=a
            cnt[a]=1
        if b not in friend:
            friend[b]=b
            cnt[b]=1
        if find(a)!=find(b): # 만약 둘의 조상이 다르다면(서로 다른 집합에 속한다면), union 작업 수행
            union(a,b)
        print(cnt[find(a)]) # 해당 집합의 요소 수 
