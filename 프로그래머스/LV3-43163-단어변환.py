# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    answer = 0
    
    LEN = len(begin) #모든 단어의 길이 같음
    
    Q = deque()
    Q.append((begin,0))
    
    visited = [False] * len(words)
    while Q:
        now, step = Q.popleft()
        for i, w in enumerate(words):
            if visited[i]:
                continue
            
            # [다음 단어후보의 조건확인] 한글자 빼고 다 같은지
            count_same = 0
            for j, letter in enumerate(w):
                if now[j] == letter:
                    count_same += 1
            
            if count_same == LEN-1:
                if w == target: # 정답 도달시,
                    return step+1
                
                visited[i] = True
                Q.append((w, step+1))
                    
    return answer


'''
## 조건
	- b -> t 한글자씩 바꿔서 변환하는 최단과정 찾기
	- 그 과정이든 결과든 words집합에 있는 단어로만 변환 가능
 
	* words 길이: 3~50
	* 단어: 소문자만
	* 단어 길이: 3~10
 
	/ 모든 단어 길이 같음
	/ begin != target
	/ 변환 못하면 0 리턴
 
 
## 접근
	** 각 자리 하나씩 안맞는애들 맞춰가면 됨. (이때 관건은 words에 바꿀단어 존재여부)
	==> [EDGE]그게 아니고 쌩뚱맞게 돌아가는 경우도 있을 수 있음 !!!

	-순차적으로 바꾼다고하면,
		> 최악: O(n!)
  
	0: words 순회하며, target의 각 자리 단어가 같은 애들을 맵에 넣음
		b: hit	/ t: cog
		>> map [ 1: cog, / 2: dot,dog,log,cog / 3: dog,log,cog ]
  
	hit
	hot
	dot lot 
	log
	cog
 
	0: 시작점부터 후보들 순회하며 하나씩 걍 바꿀수있는거 찾아서 큐에 넣음 + 방문처리 (BFS)
		>> O( n^2 * L )  # L: 글자개수

'''
