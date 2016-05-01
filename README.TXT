A simple Trie structure with python language.
About Trie, please refer to https://en.wikipedia.org/wiki/Trie, very useful to organize data and get the prefix words

The Node in pyTrie would be:
class TrieNode:
	def __init__(self, parent = None, key = None):
		self.parent = parent    # TrieNode value
		self.key = key          # char/string value
		self.nodes = []         # [TrieNode, TrieNode, ....]

When generate the structure, we could do...
pytrie = PyTrie()
pytrie.add("abc")

Delete operation, which delete the node from tree structure would be as,
pytrie.delete("abcd")

Finally, when we want to get the specific prefix words
for word in pytrie("ab"):
	print word
