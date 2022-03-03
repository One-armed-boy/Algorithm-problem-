import sys
input=sys.stdin.readline

n,m=map(int,input().split())

array=[i for i in range(n+1)]

# disjoint set 자료구조를 위해 union-find 구현

def find(x):
    if array[x]==x:
        return x
    else:
        array[x]=find(array[x]) # 경로 압축
        return array[x]

def union(x,y):
    parents_x=find(x)
    parents_y=find(y)
    if parents_x>parents_y: ## 이게 왜 시간을 줄여주는거지????, rank 리스트를 구현한 것도 아닌데 의문
        array[parents_y]=parents_x
    else:
        array[parents_x]=parents_y

for i in range(m):
    t,a,b=map(int,input().split())
    if t==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
