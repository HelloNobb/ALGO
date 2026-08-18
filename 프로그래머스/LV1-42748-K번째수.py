'''
- input : array, commands
    commands : [i,j,k] 여러개

- array의 i부터 j까지 잘라내 정렬 후 k번째 숫자

# solution
1. array를 순회하다가 i이상 j 사이일 경우 temp 배열에 append
    -> O(1)
2. temp 배열 sort
-> O(nlogN)

# psuedo code
for i in range command:
    temp = []
    for i in range(0, len(array)):
        if i >= command[0]-1 and i <= command[1]-1:
            temp.append(array[i])
        elif i > command[1] - 1:
            break
    temp.sort()
    answer.append(temp[command[2]])
'''

def solution(array, commands):
    answer = []
    
    for command in commands:
        # temp = []
        # for i in range(0, len(array)):
        #     if i >= command[0]-1 and i <= command[1]-1:
        #         temp.append(array[i])
        #     elif i > command[1] - 1:
        #         break
        temp = array[command[0]-1 : command[1]] # 슬라이싱 적용하면 훨씬 간결한 코드 가능
        temp.sort()
        answer.append(temp[command[2] - 1])
    
    return answer
