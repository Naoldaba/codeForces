import sys, threading
from collections import deque

input = lambda: sys.stdin.readline().strip()

def main():
    test = int(input())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    chessboard = [input() for _ in range(test)]

    visited = set()
    queue = deque([(ax, ay, 0)]) 

    while queue:
        x, y, moves = queue.popleft()
        
        if (x, y) == (bx, by):
            print(moves)
            break
        
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for dx, dy in directions:
            for d in range(1, test+1):
                nx, ny = x + d*dx, y + d*dy
                
                if not (1 <= nx <= test and 1 <= ny <= test) or chessboard[nx - 1][ny - 1] == '#':
                    break
                        
                valid_move = True
                for l in range(1, d):
                    if chessboard[x + l*dx - 1][y + l*dy - 1] == '#':
                        valid_move = False
                        break
                if valid_move and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
        
    else:
        print(-1)
    
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
