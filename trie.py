class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.is_end_of_word = True
        curr_node.word = word

    def search(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.is_end_of_word

    def _getPrefixNode(self, prefix):
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return None
            curr_node = curr_node.children[char]
        return curr_node

    def _getWordsFromNode(self, curr_node, prefix):
        words = []
        if curr_node.is_end_of_word:
            words.append(prefix)
        for char, child in curr_node.children.items():
            words.extend(self._getWordsFromNode(child, prefix + char))

        return words

    # return list of all words that start with a given prefix
    def getWordsThatStartWith(self, prefix):
        curr_node = self._getPrefixNode(prefix)
        if not curr_node:
            return []
        return self._getWordsFromNode(curr_node, prefix)

if __name__ == '__main__':
    cool_trie = Trie()
    cool_trie.insert('anon')
    cool_trie.insert('guanabana')
    print(cool_trie.search('anon')) # expected: True
    print(cool_trie.search('papaya')) # expected: False
    print(cool_trie.search('guanabana')) # expected: True
    print(cool_trie.search('guanabanas')) # expected: False
    cool_trie.insert('guanabanas')
    print(cool_trie.search('guanabanas')) # expected: True
    print(cool_trie.getWordsThatStartWith('gua'))