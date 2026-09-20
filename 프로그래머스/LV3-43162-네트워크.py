'''
n대의 컴퓨터를 순회하며
미방문 컴퓨터일 경우 : 
    computers를 순회하며 연결된 컴퓨터들이 있는지 확인
    연결된 컴퓨터들은 visited 처리

# pseudo code
visited 배열 선언
for i in range (n):
    if not visited[i]:
        answer += 1

        que = deque([i])
        visited[i] = True

        while que:
            now = que.popleft()

            for j in range(n):
                if computers[now][j] == 1 and not visited[j]:
                    visited[j] = True
                    que.append(j)       # j에 연결된 애들도 찾으러감


'''

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range (n):
        if not visited[i]:
            answer += 1

            que = deque([i])
            visited[i] = True

            while que:
                now = que.popleft()

                for j in range(n):
                    if computers[now][j] == 1 and not visited[j]:
                        visited[j] = True
                        que.append(j)       # j에 연결된 애들도 찾으러감
                        
    return answer
