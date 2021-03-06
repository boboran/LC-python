"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2

Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

"""
class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def findRoot(roots, node):
            while roots[node]!=node:
                node = roots[node]
            return node

        roots = [i for i in range(n)]
        ret = n
        for edge in edges:
            root0 = findRoot(roots, edge[0])
            root1 = findRoot(roots, edge[1])
            roots[edge[0]] = root0
            roots[edge[1]] = root1
            if root0!=root1:
                roots[root0] = root1
                ret -= 1
        return ret
