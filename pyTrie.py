class TrieNode:
	def __init__(self, parent, key, nodes):
		self.parent = None # TrieNode value
		self.key = "" # char/string value
		self.nodes = [] # [TrieNode, TrieNode, ....]
		pass

	def path(self):
		rtn = ""
		n = self
		while n.parent is not None:
			rtn += (n.key)
			n = n.parent

		return rtn[::-1] #reserve a string

class PyTrie:
	def loadData(self):

		pass

	def getPrefixData(self, prefix):
		pass


print ("aaa"+"bbb")[::-1]

a = iter(list(range(10)))
for i in a:
	print(i)
	next(a)