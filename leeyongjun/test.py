import collections


def solution(n, edge):
    #     dists = {i:0 for i in range(1, n+1)}
    #     ed = collections.defaultdict(list) # dictionary 의 기본 value 를 list(빈배열) 로 지정해준다.

    #     for v, n in edge:
    #         ed[v].append(n)
    #         ed[n].append(v)

    #     q = collections.deque(ed[1])
    #     dist = 1
    #     while q:
    #         #현재 깊이 만큼 반복
    #         for i in range(len(q)):
    #             v = q.popleft()

    #             if dists[v] == 0:
    #                 dists[v] = dist

    #                 #새로운 depth의 노드를 추가해 준다.
    #                 for w in ed[v]:
    #                     if w != 1 : q.append(w)
    #         dist += 1

    #     max_length = max(dists.values())

    #     answer = 0
    #     for v in dists.values():
    #         if v == max_length:
    #             answer += 1

    dic = collections.defaultdict(list)
    dists = [0 for _ in range(n+1)]
    for v, n in edge:
        dic[v].append(n)
        dic[n].append(v)

    q = collections.deque(dic[1])
    dist = 1
    while q:
        for i in range(len(q)):
            p = q.popleft()
            print(p, dists)
            if dists[p]:
                continue

            if not dists[p]:
                dists[p] = dist

                for _p in dic[p]:
                    print(_p)
                    if dists[_p] == 0 and _p != 1:
                        q.append(_p)
        dist += 1
    print(dists)
    mv = max(dists)

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])