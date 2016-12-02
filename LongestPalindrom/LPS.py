def Check_Palindrome(s):
    if s == s[::-1]:
        return True
    return False


class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s

        maxLen = 1
        start_point = 0

        for _index in xrange(1, len(s)):
            if _index - maxLen >= 1 and Check_Palindrome(s[_index-maxLen-1:_index+1]):
                start_point = _index-maxLen-1
                maxLen = maxLen + 2
                continue

            if _index - maxLen >= 0 and Check_Palindrome(s[_index-maxLen:_index+1]):
                start_point = _index-maxLen
                maxLen = maxLen + 1

        return s[start_point: start_point+maxLen]
