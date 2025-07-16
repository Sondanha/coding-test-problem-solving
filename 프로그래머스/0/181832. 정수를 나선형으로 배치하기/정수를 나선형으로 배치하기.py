# def solution(n):
#     graph = [[0 for i in range(n)] for i in range(n)]
    
#     dx = [1,0,-1,0] # 우하좌상
#     dy = [0,1,0,-1]
    
#     x, y, idx, num = 0, 0, 0, 1
#     while (num<=n**2) :
#         graph[x][y] = num
#         nxtX, nxtY = x+dx[idx], y+dy[idx]
        
#         if nxtX >= n or nxtX < 0 or nxtY >= n or nxtY < 0:
#             if idx == 3: idx = 0
#             else: idx += 1
#         elif graph[nxtX][nxtY] != 0:
#             if idx == 3: idx = 0
#             else: idx += 1
            
#         num += 1    
#         x, y = x+dx[idx], y+dy[idx]   
        
#     return graph

def solution(n):
    graph = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y, idx = 0, 0, 0
    for num in range(1, n * n + 1):
        graph[x][y] = num
        nxtX, nxtY = x + dx[idx], y + dy[idx]
        if 0 <= nxtX < n and 0 <= nxtY < n and graph[nxtX][nxtY] == 0:
            x, y = nxtX, nxtY
        else:
            idx = (idx + 1) % 4
            x, y = x + dx[idx], y + dy[idx]
    return graph