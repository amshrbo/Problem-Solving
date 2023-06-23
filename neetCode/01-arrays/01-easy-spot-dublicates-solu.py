class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        ###---- my solution -----###
        # sortedNums = sorted(nums)
        # for i in range(len(sortedNums) - 1):
        #     if sortedNums[i] == sortedNums[i+1]:
        #         return True
        # return False


        ###---- most voted -----###
        # hset = set()
        # for idx in nums:
        #     if idx in hset:
        #         return True
        #     else:
        #         hset.add(idx)

        ###----- one liner (easy to grasp) ----###
        return len(nums) != len(set(nums))

