from heapq import heappop, heappush

def solution(N, road, K):
    INF = int(1e9)
    distance = [INF] * (N+1)
    
    graph = [[] for _ in range(N+1)]
    for e in road:
        v1, v2, w = e
        graph[v1].append((v2, w))
        graph[v2].append((v1, w))
    
    # pq = []
    # for v, w in graph[1]: # 시작점 1
    #     heappush(pq, (w, v)) 
    
    pq = [(0,1)] # 시작점은 가중치 0, 노드 1
    distance[1] = 0
    
    while pq:
        w, v = heappop(pq)
        
        if w > distance[v]: # 크거나 같은 경우 
            continue
        
        for node, cost in graph[v]:
            new_cost = w + cost 
            if new_cost < distance[node]:
                distance[node] = new_cost
                heappush(pq, (new_cost, node))

    answer = 0
    for i in distance:
        if i <= K:
            answer += 1
    
    return answer