numbers = xrange(1, 21)

i = 2520
print 'starting from', i

def div_by_all(i, seq):
    return all(i % n == 0 for n in seq)

while not div_by_all(i, numbers):
    i += 1

print i
