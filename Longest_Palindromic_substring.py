def longestPalindrome(s):
    palindrome = []
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(palindrome) >= j - i:
                break
            elif s[i:j] == s[i:j][::-1]:
                palindrome = s[i:j]
                break
    return palindrome
s = "ddetermine"
print(longestPalindrome(s))