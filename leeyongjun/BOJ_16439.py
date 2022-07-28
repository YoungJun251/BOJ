import itertools
import sys

n, m = map(int, input().split())

ans = 0
val_list = [i for i in range(m)]
chicken_values = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

combinations = itertools.combinations(val_list, 3)
for comb in combinations:
    val = 0
    p1, p2, p3 = comb
    for i in range(n):
        val += max(chicken_values[i][p1], chicken_values[i][p2], chicken_values[i][p3])
    ans = max(val, ans)

print(ans)