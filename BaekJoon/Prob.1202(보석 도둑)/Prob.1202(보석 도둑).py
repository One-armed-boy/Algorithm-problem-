import sys
import heapq # 힙 구조의 특성을 이용한 그리디 알고리즘 풀이를 위함
input=sys.stdin.readline

n,k=input().split() 
n=int(n) # 보석의 수
k=int(k) # 가방의 수

jew=[]
for i in range(n):
    m,v=input().split()
    m=int(m)
    v=int(v)
    heapq.heappush(jew,[m,v]) # 각 보석의 특성인 [무게,가치]로 jew 힙에 담음

bag=[]
for i in range(k):
    bag.append(int(input())) # 각 가방의 무게 한도를 bag 리스트에 담은 후 오름차순 정렬
bag.sort()
result=0 # 털 수 있는 보석의 최대 가치

tmplist=[] # 털 수 있는 후보 보석을 담을 최대 힙
for i in bag:
    while jew and i>=jew[0][0]:
        jewtmp=heapq.heappop(jew)
        heapq.heappush(tmplist,-jewtmp[1]) # 현재 고려되는 가방의 무게 한도보다 무게가 가벼운 보석들을 최대 힙에 넣음
    if tmplist:
        result-=heapq.heappop(tmplist) 
        # 해당 가방에 넣을 수 있는 보석 들 중 가치가 가장 높은 보석의 가치를 result에 더해줌(최대 힙은 pop 결과가 실제 값과 부호가 반대로 나오기 때문에 빼줌)
print(result)
