import collections
class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.node = collections.defaultdict(TrieNode)
        self.char = ""
        self.is_word = False
    
    @property
    def data(self):
        return self.node
    
    def __getitem__(self, key):
        return self.node[key]
    
    def __str__(self) -> str:
        return self.char
    
    __repr__ = __str__
    
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
 
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for chars in word:
            temp = node.char
            node = node[chars]
            node.char = temp + chars
        node.is_word = True
    

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        temp = ""
        for chars in word:
            if chars not in node.data.keys():
                return False
            node = node[chars]
            print(node.char)

        # 判断单词是否是完整的存在在trie树中
        return node.is_word    
 
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for chars in prefix:
            if chars not in node.data.keys(): 
                return False
            node = node[chars]
        return True
    
    def get_all_words(self):
        q = [self.root]
        while q:
            node = q.pop(0) 
            for child in node.data.values():
                if child.is_word:
                    yield child.char
                q.append(child)
    
        
if __name__ == '__main__':
    test = Trie()
    test.insert("hello")
    test.insert("nihao")
    print(test.search("hell"))
    print(test.startsWith("hel"))
    print(list(test.get_all_words()))
