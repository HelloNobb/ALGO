# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    
    STACK = []
    for gwal in s:
        if gwal == '(':
            STACK.append(1)
        else:
            if not STACK:
                return False
            STACK.pop()
        
    if STACK:
        return False

    return True

'''
## 조건
	- 괄호 올바르게 () 순서로 들어있으면 True / 아니 False return
 
	* 문자열 길이: 10만
	* 문자: (, )
 
## 풀이
	- 스택에 개괄호 넣고 ) 나오면 빼는식. 
	- 만약 뺄게없는게 빼야되거나 끝났는데 스택이 안 비어있으면 False

'''