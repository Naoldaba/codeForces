from collections import defaultdict


n, m = map(int, input().split())
graph=defaultdict(list)
for i in range(m):
    u, v =map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
# print(graph)
two_edged_nodoes=0
one_edged_nodes=0
center_node=False
for node, neigbour in graph.items():
    if len(neigbour)==len(graph)-1:
        center_node=True
    elif len(neigbour)==2:
        two_edged_nodoes+=1
    elif len(neigbour)==1:
        one_edged_nodes+=1
if center_node and one_edged_nodes==len(graph)-1:
    print("star topology")
else:
    if two_edged_nodoes==len(graph)-2 and one_edged_nodes==2:
        print("bus topology")
    elif two_edged_nodoes==len(graph):
        print("ring topology")
    else:
        print('unknown topology')

