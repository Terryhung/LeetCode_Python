class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        my_stack = []

        for _index in range(len(s)):
            _chr = s[_index]

            if _chr == "(" or _chr == "{" or _chr == "[":
                my_stack.append(_chr)

            elif (_chr == ")" or _chr == "}" or _chr == "]") and len(my_stack) == 0:
                    return False

            elif _chr == ")" and my_stack[-1] == "(":
                    my_stack.pop()

            elif _chr == "}" and my_stack[-1] == "{":
                    my_stack.pop()

            elif _chr == "]" and my_stack[-1] == "[":
                    my_stack.pop()

            else:
                return False

        if len(my_stack) == 0:
            return True

        else:
            return False
