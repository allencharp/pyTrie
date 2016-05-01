
from pyTrie import PyTrie

import unittest

class TestPyTrie(unittest.TestCase):

	def setUp(self):
		pass

	def test_pytrie_add(self):
		pytrie = PyTrie()
		pytrie.add("abc")
		self.assertEquals(pytrie.root.nodes[0].key, 'a')
		pytrie.add("abd")
		self.assertEquals(pytrie.root.nodes[0].nodes[0].key, 'b')

	def test_pytrie_get(self):
		pytrie = PyTrie()
		pytrie.add("abc")
		self.assertEqual(pytrie.get("ab"), ["abc"])


if __name__ == '__main__':
	unittest.main()

