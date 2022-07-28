import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(n)]

# if len(arr) < 2:
#     print(arr[0][0])
#     exit(0)
#
# dp[0] = arr[0][0]
# dp[1] = max(dp[0] + arr[1][0], dp[0] + arr[1][1])
#
# for i in range(2, n):
#     for j in range(i):
#         dp[i] = max(dp[i-2] + arr[i-1][j] + arr[i][j], dp[i-2] + arr[i-1][j] + arr[i][j+1], dp[i])
#         print(dp[i-2] , arr[i-1][j] , arr[i][j])
#         print(dp[i-2] , arr[i-1][j] , arr[i][j+1])
#         print(i, dp[i])
# print(dp[n-1])

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i-1][j]
        elif j == len(arr[i]) - 1:
            arr[i][j] = arr[i-1][j-1] + arr[i][j]
        else:
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + arr[i][j]

print(max(arr[n-1]))
