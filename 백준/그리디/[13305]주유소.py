# 13305. 주유소(실버4)

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = costs[0]
index = 0
sum_road = 0
total_cost = 0
while index < n-1:
    if min_cost <= costs[index]:
        sum_road += roads[index]
    else:
        total_cost += sum_road * min_cost
        min_cost = costs[index]
        sum_road = roads[index]
    index += 1
total_cost += sum_road * min_cost
print(total_cost)