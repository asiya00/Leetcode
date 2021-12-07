def check_palindrome(s):
    if len(s) < 2:
        return True
    return False if s[0] != s[-1] else check_palindrome(s[1:-1])


print(check_palindrome("MOM"))
