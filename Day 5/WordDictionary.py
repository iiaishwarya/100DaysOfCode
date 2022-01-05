class WordDictionary:

    def __init__(self):
        self.trie = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.trie[len(word)].add(word)

    def search(self, word: str) -> bool:
        m = len(word)
        for w in self.trie[m]:
            i = 0
            while i < m and ( w[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False
