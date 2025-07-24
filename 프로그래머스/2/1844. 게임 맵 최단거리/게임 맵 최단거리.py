from collections import deque

def solution(maps):
    dx = [-1, 0, 1, 0]  # 상, 좌, 하, 우
    dy = [0, -1, 0, 1]
    n, m = len(maps), len(maps[0])
    
    visited = [[False for j in i] for i in maps]
    dq = deque([(0,0)])   
    
    while visited[n-1][m-1] == False:
        if not dq:
            return -1
        x,y = dq.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1 and visited[nx][ny] == False:
                    maps[nx][ny] += maps[x][y]
                    dq.append((nx,ny)) 
                    
    return maps[n-1][m-1]
