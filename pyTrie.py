

class TrieNode:
	def __init__(self, parent = None, key = None):
		self.parent = parent    # TrieNode value
		self.key = key          # char/string value
		self.nodes = []       # [TrieNode, TrieNode, ....]
		pass

	# the way to yield the tree node with recursive way....
	def __iter__(self):
		if len(self.nodes) != 0:
			for node in self.nodes:
				for n in node:
					yield n
		yield self

	def addchild(self, nodes):
		self.nodes.append(nodes)

	@property
	def path(self):
		rtn = ""
		n = self
		while n.parent is not None:
			rtn += n.key
			n = n.parent
		return rtn[::-1]  # reserve a string


class PyTrie(object):
	_instance = None
	root = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(PyTrie, cls).__new__(
				cls, *args, **kwargs)
			cls._instance.root = TrieNode(parent=None, key="")
		return cls._instance

	def add(self, str):
		cur_node = self.root
		for loc, key in enumerate(str):
			node = self.__exist(cur_node, key)
			if node is not None:
				cur_node = node
			else:
				new_child = TrieNode(cur_node, key)
				cur_node.addchild(new_child)
				cur_node = new_child

	def __exist(self, trie_node, s):
		for n in trie_node.nodes:
			if n.key == s:
				return n
		return None

	def delete(self, str):
		pass

	def get(self, str):
		pass

