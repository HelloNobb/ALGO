'''
- n개의 숫자의 부호(+, -)를 바꿔 target이 되도록 할 수 있는 '경우의 수'를 리턴
- numbers : n개의 숫자 배열
- target : 계산결과 되어야하는 수

* 조건
- 2 <= numbers의 크기 <= 20
- 1 <= target <= 1000

# solution
- BFS
    numbers의 수를 +, -일때를 각각 더해가며 탐색

leaves = [0]
    
for num in numbers:
    tmp = []
    for parent in leaves:      
        tmp.append(parent + num)
        tmp.append(parent - num)
    leaves = tmp
for result in leaves:
    if(result == target):
        answer += 1
'''

def solution(numbers, target):
    answer = 0
    
    leaves = [0]        # leaves에 각 depth 결과 저장

    for num in numbers:
        tmp = []
        for parent in leaves:      
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for result in leaves:
        if(result == target):
            answer += 1

    return answer
