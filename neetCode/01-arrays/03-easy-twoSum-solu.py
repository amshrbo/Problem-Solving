class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # length = len(nums)
        # for i in range(length):
        #     for j in range(length):
        #         if i != j:
        #             if (nums[i] + nums[j]) == target:
        #                 return [i, j]


        # my second solution
        d = {}
        for idx, val in enumerate(nums):
            diff = target - val

            if diff in d:
                return [d[diff], idx]
            
            d[val] = idx
