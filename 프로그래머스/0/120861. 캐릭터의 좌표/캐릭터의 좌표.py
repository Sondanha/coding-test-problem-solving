def solution(keyinput, board):
    direction = {'up':(0,1), 'down':(0,-1), 'left':(-1,0), 'right':(1,0)}
    max_W, max_H = (board[0]-1)//2, (board[1]-1)//2
    x, y = 0, 0
    for key in keyinput:
        dx, dy = direction[key]
        if -max_W<=(x+dx)<=max_W and -max_H<=(y+dy)<=max_H:
            x, y = x+dx, y+dy

    return [x, y]

