def solution(board, skill):
    answer = 0
    N=len(board[0])
    M=len(board)
    skills=[[0]*N for i in range(M)] 
    #누적합을 이용하기 위해 모든 스킬에 대한 변화를 하나의 0 보드에 모조리 적용시킨 후, 이를 실제 보드에 한번 적용시켜 문제를 해결하는 방식
    while skill: 
        type,r1,c1,r2,c2,degree=skill.pop()
        degree=-degree if type==1 else degree
        skills[r1][c1]+=degree
        if 0<=r2<M-1:
            if 0<=c2<N-1:
                skills[r2+1][c1]-=degree
                skills[r1][c2+1]-=degree
                skills[r2+1][c2+1]+=degree
            else:
                skills[r2+1][c1]-=degree
        else:
            if 0<=c2<N-1:
                skills[r1][c2+1]-=degree
            else:
                pass
    # 0보드의 내용을 토대로 누적합 방식 이용
    for y in range(M):
        for x in range(1,N):
            skills[y][x]+=skills[y][x-1]
    for x in range(N):
        for y in range(1,M):
            skills[y][x]+=skills[y-1][x]
    # 모든 스킬의 내용을 적용시킨 skill 보드와 실제 보드를 비교하여 파괴되지 않은 건물의 수를 
    for y in range(M):
        for x in range(N):
            if board[y][x]+skills[y][x]>0:
                answer+=1
    return answer
