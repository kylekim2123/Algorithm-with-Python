# 16165. 걸그룹 마스터 준석이 (실버3)

n, m = map(int, input().split())
groups = {input(): {input() for _ in range(int(input()))} for _ in range(n)}

for _ in range(m):
    name, quiz = input(), input()

    if quiz == "0":
        print(*sorted(groups[name]), sep="\n")
    else:
        for group in groups:
            if name in groups[group]:
                print(group)
                break
