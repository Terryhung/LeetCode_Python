class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start_point = 0
        max_length = 0
        index_map = {}

        for index, value in enumerate(s):
            if value in index_map and start_point <= index_map[value]:
                start_point = index_map[value] + 1
            len_sub = index - start_point + 1
            if max_length < len_sub:
                max_length = len_sub
            index_map[value] = index
        return max_length
