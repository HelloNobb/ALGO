# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    
    citations.sort()
    LEN = len(citations)
    
    L = 0
    R = LEN
    while L < R:
        MID = (L + R + 1) // 2 #무조건 내림됨 주의 (예: 5//2 = 2 -> 6//2 = 3)
        
        count = 0
        for c in citations:
            if c >= MID:
                count += 1
        
        if count >= MID:
            L = MID #mid도 가능하니, 더 큰 쪽 탐색
        else:
            R = MID-1 #mid 불가능
        
    answer = L
    
    return answer

'''
## 조건
	- 배열 길이 n 중 값이 h 이상인게 h개 이상인 h의 최대값 구하기 (= h-index)
 
	* 배열길이 n: 1~ 1천
	* 값: 0~1만

## 풀이
	[ 정렬 후 이진탐색 ]
	
'''