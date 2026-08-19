'''
- 큐 에서 '우선순위가 가장 높은 프로세스' 가 나올때까지 꺼내고 넣고 반복
- 우선순위가 가장높은 프로세스일 경우 실행
-> 이때, traget 프로세스가 '몇번째로' 실행되는지 return

# input
- priorities : 중요도 순서대로 담긴 배열
- location : target 프로세스 index(0~)

# solution
- 가장 간단한 방법은 직접 반복문 돌려가면서 체크
- 반복문 돌 때, '지금 숫자가 가장 큰 수' 라는걸 어떻게 알지?
    1) max(arr) -> O(N)
    2) valArr 복제해 sort 후 뒤에서부터 값 지우면서 비교 -> arr.pop() : O(1)
- 반복문이 돌 때, location값도 같이 돌아야 한다(추적하기 위해)
- 가장 큰값이라 priority에서 빠질 때 answer++


# psuedo code
입력받은 priority 복제해 정렬    arr.copy()
입력받은 priority는 큐 자료형으로 que = deque(priority)

while !que.empty():
    tempNum = que.popleft()         // 이때 꺼냄
    if tempNum == priority[-1] :     // 꺼낸 수가 가장큰수면 그냥 지가가지만, 아니면 다시 넣어야함
        answer += 1
        
        // 꺼낸게 target이면 종료
        if location == 0:
            break
    else :
        que.append(tempNum)
    
    // 좌표 추적
    if location > 0 :
        location -= 1
    else : 
        location = len(que) - 1

'''
from collections import deque

def solution(priorities, location):
    answer = 0
    
    tempArr = priorities.copy()
    tempArr.sort()
    
    que = deque(priorities)

    while que :
        tempNum = que.popleft()          # 이때 꺼냄
        if tempNum == tempArr[-1] :     # 꺼낸 수가 가장큰수면 그냥 지가가지만, 아니면 다시 넣어야함
            answer += 1
            tempArr.pop()

            # 꺼낸게 target이면 종료
            if location == 0:
                break
        else :
            que.append(tempNum)

        # 좌표 추적
        if location > 0 :
            location -= 1
        else : 
            location = len(que) - 1
    
    return answer
