import collections
import itertools
import sys
from copy import deepcopy
n, m = map(int, input().split())

board = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
points = []
ans = float('inf')
blanks = 0

#바이러스 시작 좌표 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            points.append((i, j))
        elif board[i][j] == 0:
            blanks += 1


def check(board):
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                return False

    return True


def print_board(board):
    for i in range(n):
        print()
        for j in range(n):
            print(board[i][j], end=' ')
    print()


#bfs를 이용한 구현
def solution(points, blanks):
    visited = [[False] * n for _ in range(n)]

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    t = 0
    while True:
        length = len(points)
        if blanks == 0 or length == 0:
            if blanks == 0:
                return t
            else:
                return float('inf')

        t += 1
        for i in range(len(points)):
            y, x = points.popleft()
            if visited[y][x] == False:
                visited[y][x] = True

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < n:
                    if visited[ny][nx] == False:  # 아직 방문하지 않은 칸에 대해
                        if board[ny][nx] == 0:  # case 1: 빈 칸을 만난 경우
                            points.append((ny, nx))
                            visited[ny][nx] = True
                            blanks -= 1
                        elif board[ny][nx] == 2:  # case 2: 비활성된 바이러스를 만난 경우
                            points.append((ny, nx))
                            visited[ny][nx] = True


_points = itertools.combinations(points, m)

for p in _points:
    _p = collections.deque()
    for i in p:
        _p.append(i)
        # new_board[y][x] = 1


    # 비활성 바이러스좌표를 다 0으로 바꿔주는 작업을 not in 연산을 통해서 진행했는데 시간 초과 발생
    # for i in points:
    #     if i not in _p:
    #         y, x = i
    #         board[y][x] = 0
    tmp = solution(_p, blanks)

    ans = min(ans, tmp)

if ans == float('inf'):
    print(-1)
else:
    print(ans)

