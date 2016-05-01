class TrieNode:
	def __init__(self, parent = None, key = None):
		self.parent = parent    # TrieNode value
		self.key = key          # char/string value
		self.nodes = []       # [TrieNode, TrieNode, ....]
		pass

	# yield the tree node one by one with recursive way....
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

			if loc == len(str)-1:
				if len([n for n in cur_node.nodes if n.key == '']) == 0:
					new_child = TrieNode(cur_node, '')
					cur_node.addchild(new_child)
					cur_node = new_child

	def delete(self, str):
		cur_node = self.root
		for loc, key in enumerate(str):
			cur_node = self.__exist(cur_node, key)
		if cur_node is not None:
			empty_node = [node for node in cur_node.nodes if node.key == '']
			if(len(empty_node) > 0):
				cur_node.nodes.remove(empty_node[0])
			while len(cur_node.nodes) == 0:
				parent = cur_node.parent
				parent.nodes.remove(cur_node)
				cur_node = parent


	# generator
	def get(self, str):
		cur_node = self.root
		for loc, key in enumerate(str):
			node = self.__exist(cur_node, key)
			if node is None:
				return
				yield
			else:
				cur_node = node

		# get leaf nodes
		for n in self.__leafnodes(cur_node):
			yield n.path

	# recursive yield to get the final leaf node
	def __leafnodes(self, node):
		cur_node = node
		if len(cur_node.nodes) == 0:
			yield node
		else:
			for cn in cur_node.nodes:
				cur_node = cn
				for n in self.__leafnodes(cur_node):
					yield n

	def __exist(self, trie_node, s):
		for n in trie_node.nodes:
			if n.key == s:
				return n
		return None


