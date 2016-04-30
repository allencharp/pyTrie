

class TrieNode:
	def __init__(self, parent = None, key = None):
		self.parent = parent    # TrieNode value
		self.key = key          # char/string value
		self.nodes = None       # [TrieNode, TrieNode, ....]
		pass
	
	# the way to yield the tree node with recursive way....
	def __iter__(self):
		if self.nodes != None:
			for node in self.nodes:
				for n in node:
					yield n
		yield self

	def setchildren(self, nodes):
		self.nodes = nodes

	@property
	def path(self):
		rtn = ""
		n = self
		while n.parent is not None:
			rtn += n.key
			n = n.parent
		return rtn[::-1]  # reserve a string



class PyTrie:
	def __init__(self):
		pass

	def add(self, str):
		pass

	def delete(self, str):
		pass

	def get(self, str):
		pass

