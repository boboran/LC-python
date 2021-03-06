"""
There are n different online courses numbered from 1 to n.
Each course has some duration(course length) t and closed on dth day.
A course should be taken continuously for t days and must be finished before or on the dth day.
You will start at the 1st day.

Given n online courses represented by pairs (t,d),
your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation:
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day,
    and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day,
    and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.


Note:
1. The integer 1 <= d, t, n <= 10,000.
2. You can't take two courses simultaneously.
"""
class Solution:
    def scheduleCourse(self, courses: 'List[List[int]]') -> 'int':
        pq = []
        start = 0
        for t, end in sorted(courses, key=lambda x:[x[1],x[0]]):
            #print(t,end,pq)
            if start+t<=end:
                start += t
                heapq.heappush(pq, -t)
                continue
            if len(pq)>0 and -pq[0]>t:
                start += heapq.heappop(pq)
                start += t
                heapq.heappush(pq, -t)
        return len(pq)
