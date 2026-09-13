# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    
    SET = set(phone_book) #접두사 후보들 넣은 SET
    
    for num in phone_book:
        for i in range(len(num)):
            pre = num[:i]
            if pre in SET:
                return False
            
    return answer



'''
## 조건
[ 전화번호들 중 한 번호가 다른 번호의 접두어인 경우 확인해 True/False 리턴 ]
	* 번호개수: 1~100만
	* 각 길이: 1~20
	* 같은 번호 중복 없음
 
## 접근
[ 길이 1~20만큼 잘라가면서 set에 모두 넣고 중복체크 &  ]
	* set이용 (중복제거되므로, 넣었을때 개수 줄어들면 동일번호 판별 가능)
 
	== [계획1]
	1: 루프 돌며 각 번호를 접두사로 설정해 모두 같은 길이로 잘라 set에 넣기
	-->2: 개수 줄어들면 return False
 
	==> 100만 * 100만이라 안됨.
 
	== [계획2]
	: 미리 후보 접두사들 전부 set에 집어넣어두고, 각 번호들 1~20자리까지 잘라가며 set에 해당숫자 있는지 체크
	
 

'''










'''
## 접근 (접두사 존재 안해야 True)
1: for로 전체 순회하며 하나씩 접두사로 설정하여 길이 구하기
2: 나머지 모두 기준 접두사 길이만큼 잘라 hash set에 넣음 
    //자르지않고 startswith() 사용
3: set 길이가 기존 배열 길이와 다르면 false



## 풀이
- 길이 20이 최대니 1~20으로 모두 자르고 그게 실제 전화번호에 있는지확인
    > 확인할땐 set에 넣어두고 in 써서
'''