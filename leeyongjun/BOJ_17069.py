import itertools

n = int(input())

romas = [1, 5, 10, 50]
ans = set()


# 재귀를 통한 구현에서는 시간 초과 발생
# def solution(num, depth):
#     if depth == n:
#         ans.add(num)
#         return
#
#     solution(num + romas[0], depth+1)
#     solution(num + romas[1], depth+1)
#     solution(num + romas[2], depth+1)
#     solution(num + romas[3], depth+1)


for comb in itertools.combinations_with_replacement(romas, n):
    ans.add(sum(comb))

print(len(ans))

