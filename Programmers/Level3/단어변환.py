# DFS/BFS 단어 변환 (Level 3)


def solution(begin, target, words):
    def dfs(depth, now):
        if now == target:
            nonlocal min_depth
            min_depth = min(min_depth, depth)
            return

        for i in range(len(now)):
            for j, word in enumerate(words):
                if (
                    not visited[j]
                    and now[:i] + now[i + 1 :] == word[:i] + word[i + 1 :]
                ):
                    visited[j] = True
                    dfs(depth + 1, word)
                    visited[j] = False

    if target not in words:
        return 0

    min_depth = len(words)
    visited = [False] * len(words)

    dfs(0, begin)

    return min_depth
