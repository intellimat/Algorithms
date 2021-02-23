def isPalindrome(s):
    s = s.lower()
    i = 0

    while i < len(s)//2:
        if s[i] != s[len(s)-1-i]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    s = input('Is palindrome? ')
    print(isPalindrome(s))