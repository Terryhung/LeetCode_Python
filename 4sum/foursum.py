class Solution(object):
    def fourSum(self, nums, target):

        nums.sort()
        foursums = {}
        dict = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] not in dict:
                    dict[nums[i] + nums[j]] = [(i, j)]
                else:
                    dict[nums[i] + nums[j]].append((i, j))

        for index_1 in range(len(nums)):
            for index_2 in range(index_1+1, len(nums)):
                new_target = target - nums[index_1] - nums[index_2]

                if new_target in dict:
                    for _set in dict[new_target]:
                        if _set[0] > index_2:
                            foursums.add((nums[index_1], nums[index_2], nums[_set[0]], nums[_set[1]]))

        foursums = [list(i) for i in foursums]
        return foursums
