import sys
input=sys.stdin.readline

X,Y=map(int,input().split()) # 각각 게임 수와 승리 수
Z=(100*Y//X) # 승률, 소수점 아래 수는 버림
if Z>=99: # 만약 승률이 99%나 100%라면 앞으로 모든 경기를 이기더라도 승률을 올릴 수 없다. 99%일 경우 실제 승률은 99.99999999999.....%에 근접하여 소수점을 버릴 경우 그대로 99%가 된다.
    print(-1) # 따라서 -1 출력
else:
    start=1
    end=1000000000 # 이분 탐색을 위한 start, end 설정. 이 때 X의 입력 가능 최대 값인 1000000000을 end로 놓아줌
    
    while start<=end: # 이분 탐색, 만약 승률을 변화시키는 최소 값을 찾을 시 break
        mid=(start+end)//2
        next_Z=100*(Y+mid)//(X+mid)
        #print(Z,next_Z)
        if Z>=next_Z:
            start=mid+1
        else:
            if Z==100*(Y+mid-1)//(X+mid-1):
                print(mid)
                break
            else:
                end=mid-1
