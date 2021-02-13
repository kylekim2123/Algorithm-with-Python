# 1493. 수의 새로운 연산
numbers = [1]
for i in range(1, 150):
    numbers.append(i + numbers[i-1])

def get_location(number):
    count = 0
    while number not in numbers:
        number -= 1
        count += 1
    x = count + 1
    y = numbers.index(number)+1 - count
    return x, y

for t in range(1, int(input())+1):
    p, q = map(int, input().split())
    px, py = get_location(p)
    qx, qy = get_location(q)
    newX, newY = px+qx, py+qy

    jump = 2
    result = 1
    for _ in range(newX-1):
        result += jump
        jump += 1
    jump = newX
    for _ in range(newY-1):
        result += jump
        jump += 1

    print(f'#{t} {result}')
