numbers = xrange(1, 1000)

print sum([n for n in numbers if n % 3 == 0 or n % 5 == 0])
