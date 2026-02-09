def solution(numlist, n):
    distance = sorted([(abs(n-i),i) for i in numlist], key=lambda x:x[0])
    for idx, e in enumerate(distance):
        if idx <= len(distance)-2:
            if e[0] == distance[idx+1][0] and e[1] < distance[idx+1][1]:
                distance[idx], distance[idx+1] = distance[idx+1], distance[idx]
    return [i[1] for i in distance]