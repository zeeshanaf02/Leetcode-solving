class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=list(s)
        for i in range(len(s)):
            if i>=2 and s[i]==s[i-1]==s[i-2]:
                lst[i-2]=""
        return "".join(lst)