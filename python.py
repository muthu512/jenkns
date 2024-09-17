def is_palindrome(s):
    # Removing any spaces and converting to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]
