# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def get_max_prior(COUNT):
    for i in range(9,0,-1):
        if COUNT[i] != 0:
            return i

def solution(priorities, location):
    answer = 0
    
    Q = deque()
    COUNT = [0]*10
    
    for i, p in enumerate(priorities):
        COUNT[p] += 1
        Q.append((p, i))
    
    M = get_max_prior(COUNT)
    done = 0
    while Q:
        now = Q.popleft()
        if (now[0] == M): #max우선순위면,
            done += 1
            #찾던애면, 그만
            if now[1] == location:
                answer = done
                break
            
            COUNT[M] -= 1
            if COUNT[M] == 0:
                M = get_max_prior(COUNT)
        else:  
            Q.append(now)
    
    return answer

'''
## 문제 조건
    - 배열 각각의 값 크기 클수록 우선순위 높음
    - 큐에서 하나씩 꺼내며, 걔보다 큰 애 있음 패스/없으면 꺼냄(실행)

## 접근법
[ 우선순위가 1~9 고정이므로, 빈도 배열만 유지하여 현재 최대값 바로 알 수 있도록 함 ]

	1: 큐에 (우선순위, 원래위치)쌍 넣으며, 동시에 빈도배열(COUNT)에 각 우선순위별 개수 기록 (1~9)
	2: 빈도배열에서 현재 max우선순위 미리 구해둠
	3: 큐에서 하나씩 빼서,
		- max랑 같으면 > 실행처리 (done++, 빈도배열 갱신, max우선순위 갱신)
		- max 아니면 > 큐 뒤로 다시 넣음
	4: 실행한게 찾던 위치(location)이면 즉시종료

'''