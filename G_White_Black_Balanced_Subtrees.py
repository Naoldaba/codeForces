from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    test= int(input())
    for _ in range(test):
        V=int(input())
        graph=defaultdict(list)
        arr=list(map(int, input().split()))
        Str=input()

        for i in range(len(arr)):
            graph[arr[i]].append(i+2)
        
        def dfs(root):
            black=white=num_balanced=0
            if Str[root-1]=='W':
                white+=1
            else:
                black+=1
            
            for child in graph[root]:
                w, b, num_bal = dfs(child)
                black+=b
                white+=w
                num_balanced+=num_bal

            if black==white:
                num_balanced+=1

            return (white, black, num_balanced)

        result = dfs(1)
        print(result[-1])

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

