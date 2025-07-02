class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.freq = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts the given string in the Trie
        :param word: string to be inserted
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.freq += 1
        node.end = True

    def visualize(self):
        def dfs(node, prefix="", indent=""):
            for char, child in sorted(node.children.items()):
                marker = "*" if child.end else ""
                print(f"{indent}{char}{marker}")
                dfs(child, prefix + char, indent + " ")

        dfs(self.root)

    def searchAsWholeWord(self, word):
        """
        Checks if the given string exists in the Trie as a whole word
        :param word: string to be searched
        :return: Boolean indicating whether the word exists or not
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end

    def searchFreqAsPrefix(self, pfx):
        """
        Checks how frequent the given pattern appears as prefixes
        in other words in Trie
        :param pfx: string to be searched
        :return: Integer denoting the frequency of the parameter
        """
        node = self.root
        for c in pfx:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.freq

    def getLongestCommonPrefix(self):
        longestPfx, longestPfxLen = "", 0
        node = self.root
        # If node has more than one child, it means the trie diverges.
        # Therefore the common prefix ends there.
        while not node.end and len(node.children) <= 1:
            c = next(iter(node.children))  # node's only child
            longestPfxLen += 1
            longestPfx += c
            node = node.children[c]
        return longestPfx, longestPfxLen

    def getWordWithLowestEditDistance(self, word):
        """
        Searches the Trie for the word with the lowest edit distance
        Each substitution, insertion, deletion costs 1
        """
        # Checks if the word already exists in the Trie
        if self.searchAsWholeWord(word):
            return word

        # If not, tries to find the closest word
        # TODO:


def spellCheck(word, words):
    """
    Simple spellchecker, gives
    :param word: A string to be checked
    :param words: List of valid words
    """
    # convert all words ot letter case
    word = word.lower()
    words = [w.lower() for w in words]

    # build a Trie
    trie = Trie()
    for w in words:
        trie.insert(w)

    # check if the word exists in the Trie
    # set would be more efficient, but for the sake of demonstration...

    # if the word is not found, traverse the Trie to find

    return trie.getLongestCommonPrefix()


def testTrie():
    trie = Trie()
    trie.insert("cat")
    trie.insert("car")
    trie.insert("cart")
    print(trie.searchAsWholeWord("car"))
    print(trie.searchFreqAsPrefix("ca"))  # 3, prefix for cat car cart
    print(trie.getLongestCommonPrefix())  # 'ca' of length 2
    trie.insert("dog")
    trie.insert("dove")
    trie.visualize()


def testTrie2():
    trie = Trie()
    trie.insert("BEAR")
    trie.insert("BEAT")
    trie.insert("BIG")
    trie.insert("BULL")
    trie.insert("BUY")
    print(trie.searchAsWholeWord("BEAR"))
    print(trie.searchFreqAsPrefix("BEA"))  # 2, prefix for BEAR BEAT
    print(trie.getLongestCommonPrefix())  # 'B' of length 1
    trie.insert("SELL")
    trie.insert("STOCK")
    trie.insert("STOP")
    print(trie.searchFreqAsPrefix("S"))  # 3, prefix for SELL STOCK STOP
    print(trie.getLongestCommonPrefix())  # no common prefix anymore
    trie.visualize()


def testSpellChecker():
    print(spellCheck("Hello", ["hello", "hi", "no"]))


if __name__ == "__main__":
    testTrie()
    print("Test #2")
    testTrie2()
    print("Spell checker test")
    testSpellChecker()
