# import collections
# import sys
#
# r, c, k = map(int, input().split(' '))
# arr = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(3)]
# ans = 0
#
# def check(y, x):
#     if arr[y][x] == k:
#         return True
#     return False
#
#
# def _print():
#     for i in range(len(arr)):
#         print()
#         for j in range(len(arr[0])):
#             print(arr[i][j], end=' ')
#
#     print()
#
# def r():
#     m, n = len(arr[0]), len(arr)
#     new_board = [[] for _ in range(n)]
#
#     for y in range(n):
#         dic = collections.defaultdict(int)
#         for x in range(m):
#             if arr[y][x] != 0:
#                 dic[arr[y][x]] += 1
#         items = sorted(list(dic.items()), key=lambda x:(x[1], x[0]))
#         for _y, _x in items:
#             new_board[y].append(_y)
#             new_board[y].append(_x)
#
#         for i in range(len(items), m):
#             new_board[y].append(0)
#             new_board[y].append(0)
#
#     return new_board
#
#
# def c():
#     m, n = len(arr[0]), len(arr)
#     new_board = [[0]*m for _ in range(2*n)]
#
#     for x in range(m):
#         dic = collections.defaultdict(int)
#         column = []
#         for y in range(n):
#             if arr[y][x] != 0:
#                 dic[arr[y][x]] += 1
#         items = sorted(list(dic.items()), key=lambda x: (x[1], x[0]))
#
#         for _y, _x in items:
#             column.append(_y)
#             column.append(_x)
#
#         for i in range(len(items), n):
#             column.append(0)
#             column.append(0)
#
#         for y in range(2*n):
#             new_board[y][x] = column[y]
#
#     return new_board
#
# arr = r()
# _print()
# arr = c()
# _print()
# arr = r()
# _print()


