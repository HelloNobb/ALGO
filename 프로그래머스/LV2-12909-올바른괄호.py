'''
( 수만큼 )가 와야 한다.

# solution
(가 들어올 때 마다 스택에 저장. )가 들어오면 스택에서 pop
)가 들어왔을 때 스택이 비어있으면 False
'''

def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                stack.pop()
            
    if stack:
        return False
        
    return True
