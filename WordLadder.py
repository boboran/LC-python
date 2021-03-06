"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

1. Return 0 if there is no such transformation sequence.
2. All words have the same length.
3. All words contain only lowercase alphabetic characters.
4. You may assume no duplicates in the word list.
5. You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # BFS from start to end
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        q = collections.deque()
        q.append(beginWord)
        level = 1
        while len(q):
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                for i in range(len(cur)):
                    for c in letters:
                        if c!=cur[i]:
                            temp = cur[:i]+c+cur[i+1:]
                            if temp in wordSet:
                                if temp==endWord:
                                    return level+1
                                q.append(temp)
                                wordSet.remove(temp)
            level += 1
        return 0

class Solution2:
    # BFS from both end
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        mm = dict()
        for word in wordList:
            mm[word] = 0
        mm[beginWord] = 1
        if endWord not in mm:
            return 0
        mm[endWord] = -1
        q = collections.deque()
        q.append(beginWord)
        q.append(endWord)
        while len(q):
            #print(q,mm)
            cur = q.popleft()
            for i in range(len(cur)):
                for c in letters:
                    if c!=cur[i]:
                        nxt = cur[:i]+c+cur[i+1:]
                        if nxt in mm:
                            if mm[nxt]*mm[cur]<0:
                                return abs(mm[nxt]-mm[cur])
                            if mm[nxt]==0:
                                if mm[cur]>0:
                                    mm[nxt] = mm[cur]+1
                                else:
                                    mm[nxt] = mm[cur]-1
                                q.append(nxt)
        return 0
