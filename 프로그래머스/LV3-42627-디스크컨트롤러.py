'''
(번호/요청 시각/소요 시각)

# 우선순위
1. 소요시각 짧은 순
2. 요청시각 빠른 순
3. 번호 작은 순

(요청 시각 / 소요 시간)

# solution
heap정렬 사용해 '현재 시점'에서 가장 소요시각 짧은 작업 수행

1. jobs 정렬 (요청 시간순 정렬)
2. 현재시점(초기는 0)에 수행 가능한 작업들 heap에 추가
3. heap에서 꺼내서 작업 수행
4. 수행시간만큼 현재시점에 +
5. 2부터 다시 반복

# 회고
heap 자료구조를 안써보다가 오랜만에 써봤다. 함수같은것도 다 기억나지 않아서 찾아보며 사용했지만, 확실히
어떤 자료구조가 있는지를 알고 있어 문제 접근이 가능했다. 다양한 자료구조를 익혀놓는게 도움이 될것 같다

'''

import heapq

def solution(jobs):
    jobs.sort()             
    heap = []               
    job_idx = 0             # 다음에 확인할 작업 인덱스
    current_time = 0        # 현재 시각
    total_time = 0          # 전체 반환 시간 합
    n = len(jobs)

    while job_idx < n or heap:
        # 현재 시각 이하로 요청된 작업을 모두 힙에 추가
        while job_idx < n and jobs[job_idx][0] <= current_time:
            heapq.heappush(heap, (jobs[job_idx][1], jobs[job_idx][0]))
            job_idx += 1

        if heap:
            # 소요시간이 가장 짧은 작업 처리
            need_time, request_time = heapq.heappop(heap)
            current_time += need_time
            total_time += current_time - request_time
        else:
            current_time = jobs[job_idx][0]

    return total_time // n