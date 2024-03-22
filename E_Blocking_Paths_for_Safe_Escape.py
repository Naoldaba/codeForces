import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        maze=[]
        for j in range(n):
            row=list(input())
            maze.append(row)
        print(maze)

    direction_vec=[(-1,0),(1,0),(0,-1),(0,1)]
    visited=set()

    def dfs(row, col):
        if row<0 or col<0 or row>=len(maze) or col>=len(maze[0]) or (row, col) in visited:
            return 

        visited.add((row, col))
        if maze[row][col]=="B":
            for r,c in direction_vec:
                new_row, new_col = row+r, col+c
                if maze[new_row][new_col]=='.':



    for i in range(len(n)):
        for j in range(len(m)):
            if maze[i][j]=="#":
                if dfs(row, col):
                    return True
    return False

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


