'''
# solution
- '남아있는 사람중' 가장 무거운 사람과 가장 가벼운 사람을 순차적으로 태운다
    -> 못태우면 그사람은 같이 탈 수 있는 사람 없음 => 혼자 태워 보냄
    -> 그렇게 한칸씩 떙기다가 제일 가벼운 사람이랑 타진다 => 왼쪽도 한칸 땡기고 오른쪽도 한칸 땡김 => +1
    -> 그렇게 검사하다가 포인터가 만나면 중지

# psuedo code
1. 사람들 배열 정렬
2. 가장 가벼운 사람의 인덱스(left) = 0, 가장 무거운 사람의 인덱스(right) = 배열의 마지막 인덱스
3. while left <= right :
    if 가장 가벼운사람 + 가장 무거운사람 <= 무게제한 :
        left += 1
        right -= 1
    else :
        right -= 1
    
    answer += 1

'''

def solution(people, limit):
    answer = 0
    people.sort() 
    
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        
        answer += 1
        
    return answer
