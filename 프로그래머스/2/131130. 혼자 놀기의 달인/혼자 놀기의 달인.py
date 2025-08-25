def solution(cards):
    N = len(cards)
    visited = [False] * N
    graph_list = []
    
    def find_cir(start): # 인덱스
        visited[start] = True
        nxt_n = cards[start] -1
        cnt_N = 1
        
        while not visited[nxt_n]: # True 일때 멈추기
            visited[nxt_n] = True
            cnt_N += 1
            nxt_n = cards[nxt_n]-1
        graph_list.append(cnt_N)
            
    for i in range(N):
        if not visited[i]:
            find_cir(i)
    
    if len(graph_list) <= 1:
        return 0
    else:
        graph_list.sort()
        return graph_list[-1]*graph_list[-2]