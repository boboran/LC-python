"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.

Note:
1. You may assume that n is always positive.
2. Factors should be greater than 1 and less than n.

Example 1:
Input: 1
Output: []

Example 2:
Input: 37
Output:[]

Example 3:
Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

Example 4:
Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n, mm):
            if n in mm:
                return mm[n]
            ret = []
            for i in range(2,n):
                if n//i<i:
                    break
                if n%i==0:
                    for each in dfs(n//i, mm)+[[n//i]]:
                        if len(each)>0 and each[0]>=i:
                            ret.append([i]+each)
            mm[n] = ret
            return ret

        mm = dict()
        dfs(n, mm)
        return mm[n]
