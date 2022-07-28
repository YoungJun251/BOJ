import sys
sys.setrecursionlimit(10000) #dfs 재귀 제한을 풀어줘야 한다.

n, m, k = map(int, input().split(' '))

rectangle = [[0]*m for _ in range(n)]
points = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(k)]
area = 0

for point in points:
    x1, y1, x2, y2 = point
    for i in range(y1, y2):
        for j in range(x1, x2):
            rectangle[i][j] = 1


def _print():
    for i in range(n):
        print()
        for j in range(m):
            print(rectangle[i][j], end=' ')
    print()


def dfs(y, x):
    global area
    area += 1
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for i in range(4):
        _y = y + dy[i]
        _x = x + dx[i]

        if 0 <= _y < n and 0 <= _x < m:
            if rectangle[_y][_x] == 0:
                rectangle[_y][_x] = 1
                dfs(_y, _x)


ans = 0
ans_value = []

for i in range(n):
    for j in range(m):
        if rectangle[i][j] == 0:
            rectangle[i][j] = 1
            dfs(i, j)
            ans_value.append(area)
            ans, area = ans + 1, 0

print(ans)
for i in sorted(ans_value):
    print(i, end=' ')