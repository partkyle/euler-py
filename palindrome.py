import itertools

def is_palindrome(s):
    for f, b in itertools.izip(s, reversed(s)):
        if f != b:
            return False

    return True
