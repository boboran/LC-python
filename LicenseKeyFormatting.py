"""
You are given a license key represented as a string S which consists only alphanumeric character and dashes.
The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters,
except for the first group which could be shorter than K, but still must contain at least one character.
Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"
Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:
Input: S = "2-5g-3-J", K = 2
Output: "2-5G-3J"
Explanation: The string S has been split into three parts,
each part has 2 characters except the first part as it could be shorter as mentioned above.


Note:
1. The length of string S will not exceed 12,000, and K is a positive integer.
2. String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
3. String S is non-empty.
"""
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        n = 0
        for c in S:
            if c=='-':
                n += 1
        remain = (len(S)-n)%K
        cur = remain if remain>0 else K
        ret = ""
        for c in S:
            if c=="-":
                continue
            ret += c.upper()
            cur -= 1
            if cur==0:
                ret += "-"
                cur = K
        if cur==K:
            return ret[:-1]
        return ret


class Solution2:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        ret = ""
        idx = len(S)-1
        i = 0
        while idx>=0:
            if S[idx]=='-':
                idx -= 1
                continue
            ret = S[idx].upper()+ret
            idx -= 1
            i += 1
            if i==K:
                ret = '-'+ret
                i = 0
        if len(ret) and ret[0]=='-':
            return ret[1:]
        return ret
