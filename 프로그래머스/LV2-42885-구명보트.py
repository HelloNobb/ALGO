# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    count = 0
    
    P = deque(sorted(people, reverse=True))
    
    while P:
        if len(P) == 1:
            count += 1
            break
        
        FATTEST = P.popleft()
        SKINNIEST = P[-1]
        
        if FATTEST + SKINNIEST <= limit:
            P.pop()
        
        count += 1
    
    return count

'''
## 조건
    - limit 이하인 한해서 한번에 최대 "2명" 뽑기
    - 총 뽑은 횟수 최소화하기
    
    * 원소: 1~5만
    * 값: 40~240
    * limit: 40~240

## 접근
    [ 횟수만 구하면 되니까 limit 길이의 배열에 더한 원소수 기록하는 식 ]

	120 70 50 80 80  / limit: 200
	
	[계획]: 무거운 애들끼리 먼저 짝지어 보내기
	0: 내림차순정렬 - 120 80 80 70 50
	1: 하나씩 뽑고, 나머지 앞에서부터 더해서 아직 방문안했고 limit이내인 애로 하나 뽑아 보내기 (없으면 혼자보내기)
	
	==> [시간초과 힌트]
 	최적의 매칭은 가장 무거울수록 가장 가벼운 애를 매칭! (선택 폭 제일 좁기 때문에)
		>> 가장 가벼운애랑 매칭안되면 다른애들이랑도 안되는거니까 걍 거기서 끝.
		매칭되더라도 그보다 무서운애랑 매칭할 필요없음. 어차피 나머진 지금보다 가벼우니.
'''
