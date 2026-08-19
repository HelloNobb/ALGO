# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for c in commands:
        arr = array[c[0]-1:c[1]]
        arr.sort()
        
        N = arr[ c[2]-1 ]
        answer.append(N)
    
    return answer

'''
## 문제조건
 - 배열을 i~j번째만 잘라 정렬 후, k번째에 있는 수 return
 
## I/O 예시

		array						commands						return
	[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]

## 팁
	* 배열 자를때 슬라이싱 범위는 i~j번째를 원하면, [i-1] ~ [j] 로 구해야함

'''
