def find_risk(x, y, graph, N):
    # 좌상, 상, 우상, 좌, 우, 좌하, 하, 우하
    dx = [-1, -1, -1, 0, 0, 1, 1, 1] 
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            
def solution(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                find_risk(i, j, board, N)
    answer = 0
    for i in range(N):
        for j in range(N): 
            if board[i][j] == 0:
                answer += 1
    return answer

