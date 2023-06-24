class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == "":
            return [[""]]

        d = {}

        for ele in strs:
            sorted_ele = ''.join(sorted(ele))
            if sorted_ele in d:
                d[sorted_ele].append(ele)
            else:
                d[sorted_ele] = [ele]

        # print(d.values())
        return d.values()


