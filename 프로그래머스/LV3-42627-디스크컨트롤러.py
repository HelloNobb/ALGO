# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq
from collections import deque

def solution(jobs):
    jobs.sort(key=lambda x:x[0]) # ! 2차배열에서 [0] 기준으로 정렬하는 방법
    jobsQ = deque(jobs)
    waitQ = []
    
    time = 0
    done = []
    
    while jobsQ or waitQ:
        # 대기큐 업데이트
        while jobsQ and jobsQ[0][0] <= time: ### [EDGE] 인덱스 접근할때 항상 엣지케이스 생각!
            REQ, DUR = jobsQ.popleft()
            heapq.heappush(waitQ, (DUR, REQ)) #소요시간 기준 정렬하기위해 순서 바꿔넣기
        
        # 실행
        if waitQ:
            DUR, REQ = heapq.heappop(waitQ)
            time += DUR
            done.append(time-REQ)
        elif jobsQ: #대기큐 빈 상태 (=현재 실행가능한 작업 없으니 시간점프 필요)
            time = jobsQ[0][0]
        
    avr = sum(done) // len(done)
    
    return avr

'''
## 문제 조건
    - 우선순위 처리(소요시간 짧음-> 요청시각 빠름-> 작업번호 작음 순)
    - 한번 고르면 끝날때까지 작업
    
    * 작업 개수: 1~500
    * 요청 시점: 0~1000
    * 소요 시간: 1~1000
    
    * I: [[요청시각, 소요시간], [..]]
    * O: 모든 요청 작업의 반환 시간의 평균

## 접근 흐름
    0: 작업모음덱에 Q[0](=요청시점) 기준으로 오름차순 정렬, time=0 초기화, dones = []
    1: 맨앞 뽑아 처리 (time += 맨앞의소요시간, dones에 "time-요청시각 값" 넣기)
    ----
    2: 요청시각이 처리완료시간 이하인 작업들 중 소요시간 최소인 애 뽑아 처리
    3: 처리 후 또 원래큐에서 가능한 작업 뽑아 대기큐에 넣고 소요시간 최소인 애 뽑아 처리
    ----> 대기큐와 작업큐 빌때까지 반복
    4: dones값들의 평균 구해 리턴
    
    == [MISSED POINT]: 처리완료된 시점에 실행할 수 있는 작업 없을 수 있음 (edge case)
		- 대기큐 업데이트 했는데도 비었다면 남은 작업 중 요청 빠른 애 대기큐에 넣고 time += 요청시각 처리(시간 점프)


'''