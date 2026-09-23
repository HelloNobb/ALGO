# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def bfs_amount(computers):
    Q = deque()
    visited = [0] * len(computers)
    COUNT = 0
    
    for i in range(len(computers)):
        if visited[i]: 
            continue
        Q.append(i)
        visited[i] = 1
        while Q:
            NOW = Q.popleft()
            
            for f in range(len(computers[NOW])):
                if not visited[f] and computers[NOW][f] == 1:
                    visited[f] = 1
                    Q.append(f)
            
        COUNT += 1
    
    return COUNT      
    

def solution(n, computers):
    count = bfs_amount(computers)
    return count

'''
## 조건
	[ 네트워크 개수 return (연결된 망 개수) ]
	* 컴: 1~200개
	
	1 1 0
	1 1 0
	0 0 1
	--> 0번-1번 연결된 상태 (자신은 자기자신과 항상 연결된 상태로 표시: 1)
 
## 접근
	** BFS **
	0: 0번부터 쭉 큐에 연결된 애들 넣고, 그 애들하나씩 꺼내며 걔랑 연결된 애들도 다 넣기 (visited처리 필수)
	1: 연결된애들 다 큐에서 꺼내면 다음 애 !visited이면 체크
 
 
	==> 알고리즘 카테고리 봐버려서 쉽게 생각해냄. 
'''
