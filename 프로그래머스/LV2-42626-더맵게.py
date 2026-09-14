
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    count = 0
    
    SCOV = []
    for s in scoville:
        heapq.heappush(SCOV, s)
    

    while SCOV and len(SCOV) >= 2: # [EDGE] 루프 내 원소 두개 뽑을거면 그 조건도 고려
        if SCOV[0] >= K:
            break
        
        MIN = heapq.heappop(SCOV)
        MIN2 = heapq.heappop(SCOV)
        
        NEW = MIN + (MIN2 * 2)
        count += 1
        heapq.heappush(SCOV, NEW)
        
    # [EDGE] 원소 1개 남아 루프 나왔는데 조건 충족 못한 경우
    if SCOV[0] < K:
        count = -1
    
    return count


'''
## 문제조건
    - 모든 지수가 K 이상 될때까지 공식 (min + 두번째min * 2) 반복
    - 횟수 return
    
    * 지수: 2~100만 개
    * 값: 0~100만
    * K: 0~10억
    

## 접근흐름
    == [계획] 걍 순서대로 해보는수밖에없지않나? 
    * 걸리는건 지수가 100만개라, 매번 sort()할 수 없음.
    * 매번 최소값 두개 뽑아야하니까, heap 또는 매번 버블정렬 필요
    
    0: heap에 모두 넣는다. (-> 이진트리형태로 이미 정렬 완)
    1: 최소값 2번 뽑고, 공식 돌려 다시 heap에 넣는다.
        - 공식 돌릴때 count++
        --> 첫번째 최소값이 K 이상이면 바로 count 리턴
        
    == [예외] while문 조건을 <원소가 존재한다면>으로 해놔서, 만약 하나일 경우 MIN을 2개 뽑는 과정에서 예외가능
	* 
'''