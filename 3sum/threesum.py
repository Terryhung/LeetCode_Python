class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        threesums = []
        used_set = []
        # pick point
        for _index in range(len(nums)):
            ref_nums = nums[:]
            ref_nums.pop(_index)
            check_val = - nums[_index]

            start_point = 0
            end_point = len(ref_nums) - 1

            while(start_point < end_point):
                head_val = ref_nums[start_point]
                tail_val = ref_nums[end_point]
                _sum = head_val + tail_val

                if _sum == check_val:
                    if set([-check_val, head_val, tail_val]) not in used_set:
                        threesums.append([-check_val, head_val, tail_val])
                        used_set.append(set([-check_val, head_val, tail_val]))
                    start_point = start_point + 1
                    end_point = end_point - 1

                elif _sum < check_val:
                    start_point = start_point + 1

                else:
                    end_point = end_point - 1

        return threesums
