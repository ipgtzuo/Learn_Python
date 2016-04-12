


import string

s = 'The quick brown fox jumped over the lazy dog.'
# print s
# print dir(string)

print string.capwords(s)

leet = string.maketrans('abegiloprstz', '463611092572')

print s.translate(leet)