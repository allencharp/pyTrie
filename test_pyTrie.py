from pyTrie import  TrieNode
from pyTrie import PyTrie

rootnode = TrieNode(None, '')
anode = TrieNode(rootnode,'a')
bnode = TrieNode(rootnode,'b')
rootnode.addchild(anode)
rootnode.addchild(bnode)

acnode = TrieNode(anode, 'c')
anode.addchild(acnode)

accnode = TrieNode(acnode, 'c')
acnode.addchild(accnode)

bdnode = TrieNode(bnode,'d')
bnode.addchild(bdnode)

def test_trienode():
	for i in rootnode:
		print i.path

def test_pytrie_add():
	pytrie = PyTrie()
	pytrie.add("abc")
	print pytrie.root.nodes[0].nodes[0].nodes[0].key
	pytrie.add("abd")
	print pytrie.root.nodes[0].nodes[0].nodes[1].key

def test_pytrie_get():
	pytrie = PyTrie()
	pytrie.add("abc")
	pytrie.add("abb")
	pytrie.add("adz")
	print pytrie.get("ab")

#test_trienode()
#test_pytrie_add()
test_pytrie_get()
