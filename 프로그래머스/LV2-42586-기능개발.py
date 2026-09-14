# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []
    
    LEFT = deque()
    for i in range(len(progresses)):
        left = (100 - progresses[i] - 1) // speeds[i] + 1 # 정수나눗셈에선 항상 엣지케이스 생각
        LEFT.append(left)
    
    start = LEFT.popleft()
    count = 1
    while LEFT:
        next = LEFT.popleft()
        if next > start:
            start = next
            answer.append(count)
            count = 1
        else:
            count += 1
    
    answer.append(count)
    
    return answer


'''
## 문제조건
[ 왼쪽부터 순서대로 처리해야한다면, 한번 배포마다 몇개 기능씩 배포되는지 확인 ]
	- 작업 개수: 1~100
	- 진도: 100미만
	- 속도: 100이하

## 접근흐름
	[ 큐의 각 자리에 맞게 완료까지 며칠걸리는지 각각 넣어놓고, 조건충족까지 뽑고 몇개뽑았는지 기록하고 반복하기 ]
	
	== EDGE
		* 정수나눗셈 시 실제와 괴리 조심: 예) 7일 걸리는 작업을 2 속도로 하면 3일이 아닌 4일 걸림. (7//2 = 3)
'''