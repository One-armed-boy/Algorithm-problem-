from collections import deque
def solution(enroll, referral, seller, amount): 
  # enroll: 고용되어 있는 판매원, referral: enroll의 각 판매원들의 추천인, seller: 칫솔을 판매한 판매원, amount: 각 seller의 원소들이 판매한 칫솔의 수 
  
    referral_dict={} # 각 key의 직원들이 value의 직원을 추천인으로 두는 것을 의미하는 딕셔너리
    for e,r in zip(enroll,referral):
        referral_dict[e]=r
       
    salary_dict={i:0 for i in enroll} # 각 직원들이 가져가는 최종 이익
    
    que=deque() # 어떤 한 사람이 기록하는 수익을 처리하기 위한 queue
    
    for s,a in zip(seller,amount):
        que.append((s,a*100)) # 직접 판매로 기록한 수익을 모두 queue에 집어 넣음
        
    while que: # 모든 수익 흐름이 종료될 때까지 반복
        tmp=que.popleft() # (수익을 기록한 사람, 수익)
        
        bbozzi=tmp[1]//10 # 만약 추천인이 존재한다면 그에게 수익의 10%의 인센티브를 떼주어야함
        
        if referral_dict[tmp[0]]=="-": # 만약 추천인이 '-' 표시가 되어있다면 해당 인센티브는 센터로 배분되기 때문에 따로 기록을 할 필요가 없이 본인의 수익만 기록
            salary_dict[tmp[0]]+=(tmp[1]-bbozzi)
        else:
            if bbozzi!=0: # 만약 인센티브가 0이 아니라면 이를 추천인의 수익으로 처리하고 queue에 
                que.append((referral_dict[tmp[0]],bbozzi))
            salary_dict[tmp[0]]+=(tmp[1]-bbozzi)
            
    return list(salary_dict.values())
