class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordlist=s.strip().split()
        if not wordlist:
            return 0
        return len(wordlist[-1])
