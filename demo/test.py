import itertools

def go(a,b):
    c = a + b
    avg = sum(c) / 2
    tmp = {abs(sum(k)-avg): list(k) for k in list(itertools.combinations(c,len(a)))}
    new_a = tmp[min([i for i in tmp])]
    for i in new_a: c.remove(i)


    print 'a:',a
    print 'b:',b
    print 'after change:'
    print 'new_a:',new_a
    print 'new_b:',c
    print 'min:',abs(sum(new_a)-sum(c))


if __name__ == '__main__':
    a = [1, 2, 6, 12]
    b = [6, 20, 8, 9, 10, 16]

    go(a, b)