def minSquenceDiff(list1, list2):
    c = list1+list2
    c.sort()

    n = len(c)
    a, b = [], []

    for i in range(n):
        if sum(a) >= sum(b):
            b.append(c[-1])
        else:
            a.append(c[-1])
        c.pop()

        if len(a) == n/2:
            b += c
            break
        if len(b) == n/2:
            a += c
            break
    return abs(sum(a)-sum(b)), a, b

if __name__ == '__main__':
    a = [1, 2, 6, 12, 5]
    b = [6, 20, 8, 9, 10]
    print minSquenceDiff(a, b)


