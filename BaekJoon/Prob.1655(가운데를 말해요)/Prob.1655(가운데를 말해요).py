import sys
import heapq # heap 자료구조 이용을 위한 라이브러리 선언
input=sys.stdin.readline # 시간 제한이 매우 작기 때문에(Python 3 기준 0.6초), 빠른 입력을 위한 sys.stdin.readline() 이용

N=int(input()) # 문제에서 입력 받을 수의 개수
left_heap=[] # max heap
right_heap=[] # min heap
# 매우 tight한 시간 제한 때문에 heap 자료 구조의 push와 pop 만을 이용하여 구현, O(NlogN) 
# 이 때 heapify를 이용할 경우 O(N^2logN)의 시간 복잡도를 가지게 되어 시간 초과 발생
# left_heap을 max heap으로 구현하여 heap에서 첫번째 요소가 중간값이 되도록 구현

for i in range(1,N+1):
    Input=int(input()) # 순차적으로 입력 받는 수
    if i==1:
        heapq.heappush(left_heap,-Input)
    else:
        tmp=-left_heap[0]
        if tmp<=Input:
            heapq.heappush(right_heap,Input)
        else:
            heapq.heappush(left_heap,-Input)
    while len(left_heap)<len(right_heap):
        heapq.heappush(left_heap,-heapq.heappop(right_heap))
    while len(left_heap)-len(right_heap)>1:
        heapq.heappush(right_heap,-heapq.heappop(left_heap))
    print(-left_heap[0]) # 최대 힙을 구현했기 때문에 출력 시엔 -부호를 붙여야 
