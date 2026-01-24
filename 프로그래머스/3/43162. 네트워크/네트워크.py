def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(v):
        visited[v] = True
        for i in range(n):
            if computers[v][i] == 1 and not visited[i]:
                print(visited)
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer
