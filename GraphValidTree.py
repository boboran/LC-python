"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""
class GraphValidTree:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def findRoot(roots, node):
            while roots[node]!=node:
                node = roots[node]
            return node

        roots = dict()
        for edge in edges:
            if edge[0] not in roots:
                roots[edge[0]] = edge[0]
            root0 = findRoot(roots,edge[0])
            if edge[1] not in roots:
                roots[edge[1]] = edge[1]
            root1 = findRoot(roots,edge[1])
            if root0==root1:
                return False
            roots[root0] = root1
            n -= 1
        return n==1
