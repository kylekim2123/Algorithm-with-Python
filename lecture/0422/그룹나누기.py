def find_root(element):
    if element != group[element]:
        group[element] = find_root(group[element])
    return group[element]

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    group = [i for i in range(n+1)]
    for i in range(0, m+m, 2):
        group[find_root(A[i+1])] = find_root(A[i]) # union

    result = set(find_root(element) for element in group[1:])
    print('#%s %s' % (t, len(result)))