class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        d = {}

        if nums == []:
            return []

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        most_freq = []
        for i in range(k):
            max_ele = 0
            idx = None
            for key, val in d.items():
                if val >= max_ele:
                    max_ele = val
                    idx = key
            most_freq.append(idx)
            del d[idx]
        return most_freq