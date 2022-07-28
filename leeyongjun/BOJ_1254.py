str = list(input())
length = len(str)


def ispalindrome(str):
    p1, p2 = 0, len(str)-1

    while p1 < p2:
        if str[p1] != str[p2]:
            return False

        p1, p2 = p1 + 1, p2 - 1
    return True


_str = list(reversed(str))

for i in range(length+1):
    if ispalindrome(str[:]+_str[length-i: length]):
        print(length + i)
        exit(0)



