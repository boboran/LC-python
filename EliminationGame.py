"""
There is a list of sorted integers from 1 to n. Starting from left to right,
remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left,
remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left,
until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""
class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, total, step = 1, n, 1
        flag = 0
        while True:
            if total==1:
                break
            if flag==0:
                start, total, step = start+step, total//2, step*2
            else:
                if total%2==1:
                    start = start+step
                total, step = total//2, step*2
            flag = 1-flag
            #print(start, step, total)
        return start
