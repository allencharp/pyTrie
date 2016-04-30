from pyTrie import  TrieNode




rootnode = TrieNode(None, '')
anode = TrieNode(rootnode,'a')
bnode = TrieNode(rootnode,'b')
rootnode.setchildren([anode, bnode])

acnode = TrieNode(anode, 'c')
anode.setchildren([acnode])

accnode = TrieNode(acnode, 'c')
acnode.setchildren([accnode])

bdnode = TrieNode(bnode,'d')
bnode.setchildren([bdnode])

for i in rootnode:
	print i.path

print acnode.path