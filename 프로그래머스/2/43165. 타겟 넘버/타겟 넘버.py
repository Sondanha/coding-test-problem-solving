def search_tree(graph, path, start, end, result):
    if start == end:
        result.append(sum(path))
        return

    path.append(graph[start][0])
    search_tree(graph, path, start+1, end, result)
    path.pop()

    path.append(graph[start][1])
    search_tree(graph, path, start+1, end, result)
    path.pop()

def solution(numbers, target):
    result = []
    search_tree([(i, -i) for i in numbers], [], 0, len(numbers), result)
    return result.count(target)