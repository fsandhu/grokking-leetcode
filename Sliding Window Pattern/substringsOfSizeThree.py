'''
Substrings of Size 3 with Distinct Characters


Given string s, return the number of good substrings of length three in s.
A substring is 'good' if there are no repeating characters in it.

Leetcode 1876
'''

class Solution:
    def coundGoodSubstrings(self, s : str) -> int:
        result = 0

        #if entire string smaller than 3
        if len(s)<=2:
            return 0

        windowSize = 3
        for i in range((len(s)-windowSize)+1):
            #set automatically checks for duplicacy
            result += 1 if (len(set(s[i:i+windowSize]))==3) else 0

        return result