class TrieNode:
    def __init__(self):
        """
        Initialize your node here
        """
        self.child_node = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr_node = self.root
        for char in word:
            node = curr_node.child_node.get(char, TrieNode())
            curr_node.child_node[char] = node
            curr_node = node
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def util(curr_node, word):
            if len(word) == 0:
                return curr_node.is_end
            elif word[0] == ".":
                ans = False
                for child in curr_node.child_node:
                    ans = ans or util(curr_node.child_node[child], word[1:])
                return ans
            elif curr_node.child_node.get(word[0]):
                return util(curr_node.child_node[word[0]], word[1:])
            else:
                return False

        return util(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("a")
obj.addWord("a")
# obj.addWord("mad")
print(obj.search("."))
print(obj.search("a"))
print(obj.search("aa"))
print(obj.search("a"))
print(obj.search(".a"))
print(obj.search("a."))
