from collections import defaultdict

test= int(input())
for _ in range(test):
    vertices=int(input())
    letters=input()

    graph=defaultdict(tuple)
    for i in range(vertices):
        left, right = map(int, input().split())
        graph[i+1]=(left, right)

    Stack=[(1,0)]
    Min_ops=vertices

    while Stack:
        cur_node, ops = Stack.pop()
        if not cur_node:
            continue
        
        l_child, r_child = graph[cur_node]

        if not l_child and not r_child:
            Min_ops=min(Min_ops, ops)
            continue
        
        if l_child:
            Stack.append((l_child, ops + 1 if letters[cur_node-1]!='L' else ops))
        if r_child:
            Stack.append((r_child, ops + 1 if letters[cur_node-1]!='R' else ops))
    print(Min_ops)


    


