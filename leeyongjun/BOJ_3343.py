# n, a, b, c, d = map(int, input().split(' '))
#
# pa, da = n // a, n % a
# pb, db = n // c, n % c
# ans = float('inf')
#
# # 가성비가 좋은 꽃 일단 최대한 구매하기
# if (b / a) >= (d / c):
#     p = n // c
#     rest, value = n - p * c, p * d
# else:
#     p = n // a
#     rest, value = n - p * a, p * b
#
# if rest == 0:
#     print(value)
#     exit(0)
#
# pa, da = rest // a, rest % a
# pb, db = rest // c, rest % c
# if da != 0:
#     pa = pa + 1
# if db != 0:
#     pb = pb + 1
#
# ans = min(value + pa*b, value + pb*d)
#
# if pa >= pb:
#     for i in range(1, pb):
#         _rest, _value = rest - i*c, d*i
#         p, _d = _rest // a, _rest % a
#         if _d == 0:
#             _value = p * b
#         else:
#             _value = (p+1) * b
#         ans = min(_value, ans)
# else:
#     for i in range(1, pa):
#         _rest, _value = rest - i*a, b*i
#         p, _d = _rest // c, _rest % c
#         if _d == 0:
#             _value = p * d
#         else:
#             _value = (p+1) * d
#         ans = min(_value, ans)
#
#
# print(ans)
n, a, b, c, d = map(int, input().split(' '))

pa, da = n // a, n % a
pb, db = n // c, n % c

if da == 0:
    max_a = pa*b
else:
    pa, max_a = pa + 1, (pa+1) * b

if db == 0:
    max_b = pb*d
else:
    pb, max_b = pb + 1, (pb+1) * d

ans = min(max_a, max_b)

if pa >= pb:
    for i in range(1, pb):
        rest, value = n - i * c, d * i
        p, _d = rest // a, rest % a
        if _d == 0:
            value += p * b
        else:
            value += (p + 1) * b
        ans = min(value, ans)

else:
    for i in range(1, pa):
        rest, value = n - i*a, b*i
        p, _d = rest // c, rest % c
        if _d == 0:
            value += p * d
        else:
            value += (p+1) * d
        ans = min(value, ans)


print(ans)