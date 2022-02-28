import sys
input=sys.stdin.readline

T=int(input()) # 테스트 케이스 수
for _ in range(T):
    x1,y1,x2,y2 = map(int,input().split())
    n=int(input())
    result=0
    for i in range(n):
        cx,cy,r=map(int,input().split())
        cnt=0
        cnt = cnt + 1 if (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2 else cnt
        cnt = cnt + 1 if (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2 else cnt
        # 꼭 지나가야하는 행성계는 다음과 같은 조건을 만족하는 행성계이다.
        # 시작점, 출발점 중 한 점은 행성계 내에 존재해야한다.
        # 또 다른 점은 행성계 밖에 존재해야한다.
        # 즉, 두 지점 중 하나의 지점만 어떤 행성계에 포함되는 경우, 해당 행성계는 무조건 지날 수 밖에 없다.
        if cnt==1:
            result+=1
    print(result)
