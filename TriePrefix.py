# Print all words with given Prefix

# Efficient information reTRIEval data structure 
# insert and search cost = O(key_length)

class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.wordEnd = False
    

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()
    
    def charToIndex(self, ch):
        return ord(ch)-ord('a')
    
    def insert(self, key):
        marker = self.root
        length = len(key)

        for level in range(length):
            index = self.charToIndex(key[level])

            if not marker.children[index]:
                marker.children[index] = self.getNode()
            
            marker = marker.children[index] 
        
        marker.wordEnd = True

    def search(self, key):
        marker = self.root
        length = len(key)

        for level in range(length):
            index = self.charToIndex(key[level])

            if not marker.children[index]:
                return False 
            
            marker = marker.children[index]
        
        return marker!=None and marker.wordEnd
    
    def prefix(self, key):
        marker = self.root
        length = len(key)

        for level in range(length):
            index = self.charToIndex(key[level])

            if not marker.children[index]:
                return
            
            marker = marker.children[index]

        ct = 0
        for index in range(26):
            if marker.children[index]:
                print(key+('a'+index), end = '')
                temp = marker
                while not temp.wordEnd:
                    for k in range(26):
                        
                
        

if __name__ == '__main__':

    keys = [ 'there', 'the', 'is', 'as', 'man', 'go']
    result = ["Not present", "present"]

    trie = Trie()

    for key in keys:
        trie.insert(key)

    print("\'there\'", result[trie.search("there")])
    print("\'their\'", result[trie.search("their")])
    print("\'the\'", result[trie.search("the")])
    print("\'man\'", result[trie.search("man")])
    print("\'go\'", result[trie.search("go")])
    print("\'mango\'", result[trie.search("mango")])



    