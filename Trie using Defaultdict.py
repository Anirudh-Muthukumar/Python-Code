import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        marker = self.root 
        for ch in word:
            marker = marker.children[ch]
        marker.isWord = True
    
    def search(self, word):
        marker = self.root 
        for ch in word:
            marker = marker.children.get(ch)
            if not marker:
                return False 
        return marker.isWord 
    
    def startsWith(self, prefix):
        marker = self.root 
        for ch in prefix:
            marker = marker.children.get(ch)
            if not marker:
                return False 
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print("Search apple : ", trie.search('apple'))
    print("Search app : ", trie.search('app'))
    print("Starts with app : ", trie.startsWith("app"))
    trie.insert("app")
    print("Search app : ", trie.search('app'))
            