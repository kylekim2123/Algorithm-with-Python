def solution(a, edges):
    total, zero = 0, 0
    for i in a:
        total += i
        if not i:
            zero += 1
    if total:
        return -1

    length = len(a)
    if zero == length:
        return 0
    tree = [[i] for i in range(length)]
    for s, e in edges:
        tree[s].append(e)
        tree[e].append(s)
    temp = sorted(tree, key=lambda x: len(x))
    
    answer = 0
    for node in temp:
        root = node[0]
        if not a[root]:
            continue
        for next_node in node[1:]:
            next_weight = a[next_node]
            if not next_weight:
                continue
            if len(tree[next_node]) > len(tree[root]):
                a[next_node] += a[root]
                if not a[next_node]:
                    zero += 1
                answer += abs(a[root])
                a[root] = 0
                zero += 1
                break
            a[root] += next_weight
            if not a[root]:
                zero += 1
            answer += abs(next_weight)
            a[next_node] = 0
            zero += 1
            if zero == length:
                return answer
    return answer

a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))