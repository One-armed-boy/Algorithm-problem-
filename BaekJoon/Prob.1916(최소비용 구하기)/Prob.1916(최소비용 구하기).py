import sys
import heapq # 다익스트라 구현을 위한 heap 이용
input=sys.stdin.readline

INF=sys.maxsize # 초기 비용을 무한대로 두기 위함
N=int(input())
M=int(input())

graph={node:{} for node in range(1,N+1)} # 탐색을 위해 인접 노드 간 비용 입력을 위한 그래프 구현 - 이중 딕셔너리
for i in range(M):
    tmp_start,tmp_end,tmp_charge=map(int,input().split())
    if tmp_end in graph[tmp_start] and graph[tmp_start][tmp_end]<tmp_charge:
        continue # 만약 이미 해당 경로의 요금을 알고 있으며 알고 있는 요금이 새로 들어온 동일 경로 요금보다 비쌀 시엔 무시한다.
    graph[tmp_start][tmp_end]=tmp_charge 

start,end=map(int,input().split())

charges={node:INF for node in range(1,N+1)} #다익스트라를 위한 요금 그래프, 일종의 메모이제이션, 시작점이 정해져있기 때문에 딕셔너리를 이중으로 구성할 필요가 없음

def Dijkstra(start,end):
    charges[start]=0 # 시작점으로 가는 비용은 0
    heap=[] # heap 구조를 이용하는 이유는 탐색 경로 중 최소 비용 경로를 작은 시간복잡도로 찾아주기 때문
    heapq.heappush(heap,[0,start])

    while heap:
        tmp=heapq.heappop(heap)

        if tmp[0]>charges[tmp[1]]: #만약 해당 차례 탐색 경로가 이미 구해져 있고 비용이 이미 구해진 비용보다 클 시엔 해당 차례를 무시 
            continue

        for next_destination,new_charge in graph[tmp[1]].items(): # 현재 위치와 연결된 노드 중 다음 경로를 선택
            charge=tmp[0]+new_charge
            if charge<charges[next_destination]:
                charges[next_destination]=charge
                heapq.heappush(heap,[charge,next_destination])
    return charges[end]
print(Dijkstra(start,end))
