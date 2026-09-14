'''
소요되는 시간을 지정하면 처리 가능한 인원을 알 수 있어, 가능/불가능 여부를 알 수 있다
-> 최소 / 최대 시간을 범위로 지정해 이분탐색

# solution
최소 : 1초
최대 : 가장 느린 심사관이 혼자 처리했을 경우

반복문 left > right:
    // 걸리는 시간
    mid = (left + right) // 2
    
    // 해당 시간동안 처리할수 있는 인원
    total = 0

    for time in times:
        total += mid // time

    if total >= n:
        right = mid
    else:
        left = mid + 1
    
return left

'''

def solution(n, times):
    left = 1
    right = max(times) * n  

    while left < right:
        # 걸리는 시간
        mid = (left + right) // 2
        
        # 해당 시간동안 처리할수 있는 인원
        total = 0

        for time in times:
            total += mid // time

        if total >= n:
            right = mid
        else:
            left = mid + 1
        
    return left
