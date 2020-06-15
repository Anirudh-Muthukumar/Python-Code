import collections

class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.n = 0

    def visitNode(self, q, visited, other_visited):
        current_word, level = q.popleft()
        for i in range(len(current_word)):
            intermediate_word = current_word[:i] + '*' + current_word[i+1:]
            for word in self.graph[intermediate_word]:
                if word in other_visited:
                    return level + other_visited[word]
                if word not in visited:
                    visited[word] = level+1
                    q += (word, level+1),
        return None

    def wordLadder(self, beginWord, endWord, wordList):
        self.n = len(beginWord)
        for word in wordList:
            for i in range(self.n): 
                self.graph[word[:i] + '*' + word[i+1:]].append(word)

        queue_start = collections.deque([(beginWord, 1)])
        queue_end = collections.deque([(endWord, 1)])
        visited_start = {beginWord: 1}
        visited_end = {endWord: 1}

        while queue_start and queue_end:
            ans = self.visitNode(queue_start, visited_start, visited_end)
            if ans:
                return ans 
            ans = self.visitNode(queue_end, visited_end, visited_start)
            if ans:
                return ans



if __name__ == '__main__':
    wordList = ["hot","dot","dog","lot","log","cog"]
    beginWord = 'hit'
    endWord = 'cog'
    solution = Solution()
    print("Length = ", solution.wordLadder(beginWord, endWord, wordList))