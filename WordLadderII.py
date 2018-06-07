import collections
"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # help function to find words with one diff in wordlist
        def getWords(word, wordSet):
            ret = []
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c!=word[i]:
                        temp = word[:i]+c+word[i+1:]
                        if temp in wordSet:
                            ret.append(temp)
            return ret

        # BFS to find shorstest distance
        def bfs(beginWord, endWord, wordSet, dist, neighbors):
            q = collections.deque()
            level = 0
            q.append(beginWord)
            dist[beginWord] = level
            found = False
            while len(q):
                size = len(q)
                for _ in range(size):
                    cur = q.popleft()
                    neighbors[cur].extend(getWords(cur,wordSet))
                    for each in neighbors[cur]:
                        if each not in dist:
                            q.append(each)
                            dist[each] = level+1
                        if each==endWord:
                            found = True
                if found:
                    return level+1
                level += 1
            return -1

        # DFS to find all path of shorstest distance
        def dfs(path, endWord, dist, ret, neighbors):
            curWord = path[-1]
            if curWord==endWord:
                ret.append(path)
                return
            print(curWord)
            for word in neighbors[curWord]:
                if dist[word]==dist[curWord]+1:
                    dfs(path+[word], endWord, dist, ret, neighbors)

        ret = []
        dist = dict()
        neighbors = collections.defaultdict(list)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return ret
        shortest = bfs(beginWord, endWord, wordSet, dist, neighbors)
        #print(neighbors)
        #print(dist)
        #print(shortest)
        if shortest==-1:
            return ret
        dfs([beginWord], endWord, dist, ret, neighbors)
        return ret
