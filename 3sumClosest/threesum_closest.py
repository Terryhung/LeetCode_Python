class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        closeset = {}

        for _index in range(len(nums)):
            ref_nums = nums[:]
            selected_value = ref_nums[_index]
            ref_nums.pop(_index)

            check_value = target - selected_value

            start_point = 0
            end_point = len(ref_nums) - 1

            while(start_point < end_point):
                head_value = ref_nums[start_point]
                tail_value = ref_nums[end_point]
                _sum = head_value + tail_value

                if _sum == check_value:
                    return _sum+selected_value

                elif _sum < check_value:
                    start_point = start_point + 1
                    if start_point == end_point:
                        closeset[_sum + selected_value] = abs(target - _sum - selected_value)

                else:
                    end_point = end_point - 1
                    if end_point == start_point:
                        closeset[_sum + selected_value] = abs(target - _sum - selected_value)

        closeset = sorted(closeset.items(), key=lambda x: x[1])
        return closeset[0][0]
