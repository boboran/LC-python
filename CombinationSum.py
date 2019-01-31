"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

1. All numbers (including target) will be positive integers.
2. The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, start, cur, total, target, ret):
            if total>target:
                return
            if total==target:
                ret.append(cur)
                return
            for i in range(start, len(candidates)):
                dfs(candidates, i, cur+[candidates[i]], total+candidates[i], target, ret)

        ret = []
        dfs(candidates, 0, [], 0, target, ret)
        return ret
