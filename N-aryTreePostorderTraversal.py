"""
Given an n-ary tree, return the postorder traversal of its nodes' values.


For example, given a 3-ary tree:



Return its postorder traversal as: [5,6,3,2,4,1].


Note: Recursive solution is trivial, could you do it iteratively?
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root, ret):
            if root is None:
                return
            for each in root.children:
                dfs(each, ret)
            ret.append(root.val)

        ret = []
        dfs(root, ret)
        return ret
