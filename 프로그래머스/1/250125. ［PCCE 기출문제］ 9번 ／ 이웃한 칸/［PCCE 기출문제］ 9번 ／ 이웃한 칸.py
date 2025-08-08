def solution(board, h, w):
    answer = 0
    N, M = len(board), len(board[0])
    
    dx = [-1, 0, 1, 0] # 상 우 하 좌
    dy = [0, 1, 0, -1]
    
    for i in range(4):
        nx, ny = dx[i]+h, dy[i]+w
        
        if 0<=nx<N and 0<=ny<M and board[nx][ny] == board[h][w]:
            answer += 1
    return answer