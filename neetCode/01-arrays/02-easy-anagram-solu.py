class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # -------------1st solution--------------- #
        # less space
        
        # if len(s) != len(t):
        #     return False

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # return sorted_s == sorted_t




        # -------------2nd solution--------------- #
        # log(n) time solution 

        if len(s) != len(t):
            return False

        # creating two arrays with the number of chars
        letters_s = [0] * 26 
        letters_t = [0] * 26
        for i in range(len(s)):
            # using ord func to get the letter as index from  to 26
            letters_s[ord(s[i]) - ord('a')] += 1  
            letters_t[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            if letters_s[i] != letters_t[i]:
                return False

        return True
