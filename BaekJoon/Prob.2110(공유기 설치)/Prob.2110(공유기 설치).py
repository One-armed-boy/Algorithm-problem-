import sys
import heapq # 집의 위치를 입력받은 후 정렬하기 위해 힙 정렬 이용
input=sys.stdin.readline # 빠른 입력을 위한 sys.stdin.readline

N,C=map(int,input().split()) # 집의 수, 공유기의 수 입력

tmp_heap=[] # 집의 좌표를 임시로 입력 받을 힙
for _ in range(N):
    heapq.heappush(tmp_heap,int(input()))
    
array=[] # 힙 정렬을 이용하여 정렬한 집의 좌표를 입력할 리스트
for _ in range(N):
    array.append(heapq.heappop(tmp_heap))
    
def solve(start=1,end=array[-1]-array[0]): # 문제 해결을 위한 solve 함수
  # 가능한 최소 거리 탐색을 위해 1부터 최대 거리까지 순차적으로 탐색하는 방법도 있으나, 
  # 해당 방식은 몹시 비효율적이기 때문에 이진 탐색을 이용
    result=0
    while start<=end:
        mid=(start+end)//2 # mid 값을 각 반복 단계에서 공유기 사이의 최소 거리로 상정
        cur=array[0]
        cnt=1
        for i in range(1,len(array)): # 앞서 상정한 mid 값을 최소 거리로 삼고 공유기를 앞에서부터 놓아보면서 탐색
            if array[i]-cur>=mid: # 만약 집 간 거리가 mid 값보다 크거나 같으면 해당 차례의 집에 공유기를 놓음
                cnt+=1
                cur=array[i]
        if C>cnt: # 놓은 공유기의 수가 놓아야 할 공유기의 수보다 적다면 해당 단계의 mid 값(공유기 간 최소 거리)이 줄어들어야하기 때문에 end 값을 업데이트 후 다시 이분 탐색
            end=mid-1
        else: # 놓은 공유기의 수가 놓여야 할 공유기의 수보다 크다면 mid 값이 더 커져야하고, 서로 같다면 이 또한 더 커질 수 있는 경우가 존재하기 때문에 mid 값을 역시 키워야한다
            start=mid+1
            result=max(result,mid) # 해당 경우는 문제 조건에 위배되지 않는 경우이기 때문에 result 값 갱신
    return result
  
print(solve())
