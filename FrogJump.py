"""
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone.
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units.
Note that the frog can only jump in the forward direction.

Note:

1. The number of stones is ≥ 2 and is < 1,100.
2. Each stone's position will be a non-negative integer < 231.
3. The first stone's position is always 0.

Example 1:
[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping
1 unit to the 2nd stone, then 2 units to the 3rd stone, then
2 units to the 4th stone, then 3 units to the 6th stone,
4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:
[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as
the gap between the 5th and 6th stone is too large.
"""
class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        mm = dict()
        for each in stones:
            mm[each] = set()
        mm[0].add(1)
        for i in range(len(stones)-1):
            for k in mm[stones[i]]:
                nxt = stones[i]+k
                if nxt==stones[-1]:
                    return True
                if nxt in mm:
                    mm[nxt].add(k+1)
                    mm[nxt].add(k)
                    if k-1>0:
                        mm[nxt].add(k-1)
        return False


class Solution2:
    def canCross(self, stones: 'List[int]') -> 'bool':
        def jump(stones, idx, last, mm):
            if idx==len(stones)-1:
                return True
            if idx in mm and last in mm[idx]:
                return mm[idx][last]
            for off in range(-1,2):
                nxtIdx = bisect.bisect_left(stones, stones[idx]+last+off, lo=idx+1)
                if nxtIdx<len(stones) and stones[nxtIdx]==stones[idx]+last+off:
                    if jump(stones, nxtIdx, last+off, mm):
                        mm[idx][last] = True
                        return True
            mm[idx][last] = False
            return False

        if len(stones)==1:
            return True
        if stones[1]-stones[0]!=1:
            return False
        mm = collections.defaultdict(dict)
        return jump(stones, 1, 1, mm)
