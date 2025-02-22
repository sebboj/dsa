'''
Implementation without TrieNode Class
'''

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                curr_node[char] = {}
            curr_node = curr_node[char]
        curr_node['*'] = ''

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                return False
            curr_node = curr_node[char]
        return '*' in curr_node

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char not in curr_node:
                return False
            curr_node = curr_node[char]
        return True

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