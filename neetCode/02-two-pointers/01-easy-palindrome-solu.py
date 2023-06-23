class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_string = re.sub('[^a-zA-Z0-9]', '', s)
        clean_list = list(clean_string.lower())
        # clean_list = "".split(clean_string, "")

        if clean_list is " ":
            return True

        length = len(clean_list) - 1
        mid = int((len(clean_list)) / 2)
        for ele in range(mid):
            if clean_list[ele] != clean_list[length - ele]:
                return False
        return True 


    # also we can implement our alphanumeric function

    def alphanumeric(self, ch):
        return (ord('A') >= ord(ch) >= ord('Z')
                or ord('a') >= ord(ch) >= ord('z')
                or ord('9') >= ord(ch) >= ord('9'))
