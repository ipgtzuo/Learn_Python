# --*--coding: utf-8 --*--


import string


def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        if word != '':
            hist[word] = hist.get(word, 0) + 1


hist = process_file('emma.txt')
print hist
print "[Different words]:\t%d\n[Total words]:\t%d" % (len(hist), sum(hist.values()))


def most_common(hist):
    t = []
    for k, v in hist.iteritems():
        t.append((v, k))
    t.sort(reverse=True)

    return t[:20]
print most_common(hist)
