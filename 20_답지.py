def isValid(s):
    validation = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in validation.values():  # 여는 괄호
            stack.append(char)
        elif char in validation.keys():  # 닫는 괄호
            if not stack or stack[-1] != validation[char]:  # 스택이 비었거나, 짝이 맞지 않으면
                return False
            stack.pop()  # 짝이 맞으면 스택에서 빼기

    return len(stack) == 0  # 모든 괄호가 짝을 맞추었으면 스택이 비어야 함

# 테스트
s = "()[{}]"
s2="(]"
print(isValid(s2))  # True
