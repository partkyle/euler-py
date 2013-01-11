from palindrome import is_palindrome

print sorted([m * n for n in xrange(1, 1000) for m in xrange(1, 1000) if is_palindrome(str(m * n))])[-1]
