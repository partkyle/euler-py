def fibonacci_sequence(limit=1000):
    n, n_1 = 1, 1
    yield n

    while n < limit:
        n, n_1 = (n + n_1), n

        if n < limit:
            yield n


print sum([n for n in fibonacci_sequence(limit=4000000) if n % 2 == 0])
