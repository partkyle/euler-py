from prime import is_prime

result = None
n = 13
count = 5
while count < 10001:
    if is_prime(n):
        result = n
        count += 1
    n += 1

print result
