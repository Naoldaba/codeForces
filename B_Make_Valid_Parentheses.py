brackets = input()
stack = []
Max = 0

for c in brackets:
    if c == '(':
        stack.append(c)
    elif stack  and c == ')':
        stack.pop()
        Max += 2

print(Max)