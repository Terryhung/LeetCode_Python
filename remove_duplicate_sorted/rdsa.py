class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        if _len == 0:
            return 0
        flag = nums[0]
        _index = 1

        while (_index <= (_len - 1)):
            if nums[_index] == flag:
                nums.pop(_index)
                _len = _len - 1
            else:
                flag = nums[_index]
                _index = _index + 1

        return _len
