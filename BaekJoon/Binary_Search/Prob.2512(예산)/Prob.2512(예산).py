import sys
input=sys.stdin.readline # 빠른 입력을 위한 sys.stdin.readline

N=int(input()) # 도시의 수
City=list(map(int,input().split())) # 각 도시 별 요청 예산
Max=max(City)
Min=min(City)
limit=int(input()) # 전체 도시에 할당할 수 있는 예산 한도
start=1
end=Max # 탐색해야할 각 도시 별 최대 할당 예산은 결국 1~Max 값 사이에 존재, 이를 효율적으로 탐색하기 위한 이분 탐색 적용
result=0
while start<=end:
    Mid=(start+end)//2
    tmp_sum=0
    for i in City:
        if i>Mid:
            tmp_sum+=Mid
        else:
            tmp_sum+=i
    if tmp_sum>limit:
        end=Mid-1
    else:
        if Mid>=Max:
            result=Mid
            break
        start=Mid+1
        result=max(result,Mid)
print(result)
