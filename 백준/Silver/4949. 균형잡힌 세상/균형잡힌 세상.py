import sys

while True:
    S = input()
    if S == '.':
        break

    stack = []

    for i in S:
        if i =='(' or i =='[' :
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break   

    if len(stack) == 0:
        print('yes')
    else:
        print('no')
