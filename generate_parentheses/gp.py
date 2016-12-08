def unit_function(lefts, rights, vp, now_string):
    if (len(lefts) + len(rights)) == 0:
        vp.append(now_string)
        return 0
    if (len(lefts) > len(rights)):
        return 0

    else:
        if (len(lefts) > 0):
            unit_function(lefts[:-1], rights, vp, now_string + "(")
        if (len(rights) > 0):
            unit_function(lefts, rights[:-1], vp, now_string + ")")


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        lefts = n*"("
        rights = n*")"

        valid_parenthesis = []

        unit_function(lefts, rights, valid_parenthesis, "")

        return valid_parenthesis
