class TrieNode:

    def __init__(self, count=0):
        self.children = [None] * 26
        self.count = count

    def add_count(self):
        self.count += 1

    def toString(self):
        return str(self.children)+"  count:"+ str(self.count)


class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self) -> TrieNode:
        return TrieNode()

    def char_index(self, ch) -> int:
        return ord(ch) - ord('a')

    def insert(self, word):

        curr = self.root
        length = len(word)
        for level in range(length):
            index = self.char_index(word[level])

            if not curr.children[index]:
                curr.children[index] = self.get_node()
            curr.add_count()
            curr = curr.children[index]

    def search(self, word: str) -> int:
        # return freq if present in the trie else 0
        result = 0
        curr = self.root
        length = len(word)

        # search from root level
        for level in range(length):
            print(curr.toString())
            index = self.char_index(word[level]) # the #level char in word

            if not curr.children[index]:
                # if not defined, it is the end of search
                return False
            curr = curr.children[index]

        if curr is not None:

            result = curr.count
        return result


if __name__ == '__main__':
    t = Trie()

    t.insert("word")
    t.insert("wo")


    print(t.search("word"))
